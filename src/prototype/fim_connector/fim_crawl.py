import json, re, time, urllib.error, urllib.request

from pathlib import Path
from prototype import fim_connector

# ---------------------------------------------------------------------
# FIM API crawler
#
# Reads the documented portal API (https://fimportal.de/openapi.json, v0.24.0).
#
# Corpus criterion: freigabe_status 5 (silber) + 6 (gold), latest version, and at least one freitextRegel.

TARGET_LOCATION = Path(__file__).parent.parent.parent.parent / "fim_data"
DELAY = 0.3 # seconds between requests to avoid overloading the server

def crawl(target_location: Path = TARGET_LOCATION, limit: int | None = None) -> dict:
    """
        Downloads every approved schema that carries rules to <target_location>/raw/<fim_id>/.

        Re-running is cheap: a schema whose meta.json already records the same fim_version
        is skipped, so an aborted run resumes instead of starting over.
    """
    raw = target_location
    raw.mkdir(parents=True, exist_ok=True)
    seen = kept = skipped = failed = 0

    for item in fim_connector.get_approved_schemas():
        if limit and seen >= limit:
            break
        seen += 1
        fim_id, version = item["fim_id"], item["fim_version"]
        meta_path = raw / fim_id / "meta.json"
        # skip if we already have this version of the schema
        if meta_path.exists() and json.loads(meta_path.read_text("utf-8")).get("fim_version") == version:
            skipped += 1
            continue

        try:
            xdf = fim_connector._GET(f"/api/v1/schemas/{fim_id}/{version}/xdf")
        except (urllib.error.URLError, TimeoutError) as e:
            failed += 1
            print(f"  fehlgeschlagen {fim_id} v{version}: {e}")
            continue
        finally:
            time.sleep(DELAY)

        rules = fim_connector.rules_of(xdf)
        if not rules:
            continue

        # write schema and meta.json to disk using the fim_id as the directory name and using the fim naming convention
        target = raw / fim_id
        target.mkdir(parents=True, exist_ok=True)
        (target / "schema.xdf.xml").write_text(xdf, encoding="utf-8")
        meta_path.write_text(json.dumps({
            "fim_id": fim_id,
            "fim_version": version,
            "name": item.get("name"),
            "bezeichnung": item.get("bezeichnung"),
            "freigabe_status": item.get("freigabe_status"),
            "freigabe_status_label": item.get("freigabe_status_label"),
            "steckbrief_id": item.get("steckbrief_id"),
            "xdf_version": item.get("xdf_version"),
            "bezug": item.get("bezug"),
            "letzte_aenderung": item.get("letzte_aenderung"),
            "n_rules": len(rules),
            "source_url": f"{fim_connector.BASE}/api/v1/schemas/{fim_id}/{version}/xdf",
            "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        kept += 1
        print(f"  {fim_id} v{version}: {len(rules)} Regeln — {item.get('name','')[:50]}")

    return {"gesehen": seen, "geladen": kept, "uebersprungen": skipped, "fehlgeschlagen": failed}

if __name__ == "__main__":
    print(crawl())
