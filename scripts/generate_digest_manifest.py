from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

GENERATOR_VERSION = "0.1.0"
MANIFEST_NAME = "DIGEST_MANIFEST.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(bundle_dir: str | Path) -> Dict[str, Any]:
    root = Path(bundle_dir)
    artifacts: List[Dict[str, Any]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.name == MANIFEST_NAME:
            continue
        rel = path.relative_to(root).as_posix()
        artifacts.append(
            {
                "path": rel,
                "sha256": sha256_file(path),
                "size_bytes": path.stat().st_size,
            }
        )
    return {
        "manifest_type": "elyria_admission_runtime_digest_manifest",
        "generator_version": GENERATOR_VERSION,
        "generated_timestamp_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "artifacts": artifacts,
    }


def write_manifest(bundle_dir: str | Path) -> Path:
    root = Path(bundle_dir)
    manifest = build_manifest(root)
    output = root / MANIFEST_NAME
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Elyria review-bundle digest manifest")
    parser.add_argument("bundle_dir", nargs="?", default="review-bundle/latest")
    args = parser.parse_args()
    output = write_manifest(args.bundle_dir)
    print(f"DIGEST MANIFEST GENERATED: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
