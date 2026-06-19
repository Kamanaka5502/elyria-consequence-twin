from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List

MANIFEST_NAME = "DIGEST_MANIFEST.json"


class DigestVerificationError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest(bundle_dir: str | Path) -> Dict[str, Any]:
    manifest_path = Path(bundle_dir) / MANIFEST_NAME
    if not manifest_path.exists():
        raise DigestVerificationError(f"manifest not found: {manifest_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def verify_manifest(bundle_dir: str | Path) -> Dict[str, Any]:
    root = Path(bundle_dir)
    manifest = load_manifest(root)
    failures: List[Dict[str, Any]] = []
    for entry in manifest.get("artifacts", []):
        rel = entry["path"]
        path = root / rel
        if not path.exists():
            failures.append({"path": rel, "reason": "missing"})
            continue
        actual_size = path.stat().st_size
        actual_digest = sha256_file(path)
        if actual_size != entry.get("size_bytes"):
            failures.append({"path": rel, "reason": "size mismatch"})
        if actual_digest != entry.get("sha256"):
            failures.append({"path": rel, "reason": "sha256 mismatch"})
    if failures:
        raise DigestVerificationError(json.dumps(failures, indent=2, sort_keys=True))
    return {"valid": True, "artifact_count": len(manifest.get("artifacts", []))}


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Elyria review-bundle digest manifest")
    parser.add_argument("bundle_dir", nargs="?", default="review-bundle/latest")
    args = parser.parse_args()
    result = verify_manifest(args.bundle_dir)
    print(f"DIGEST MANIFEST PASS: {result['artifact_count']} artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
