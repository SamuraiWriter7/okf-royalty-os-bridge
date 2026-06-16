from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    {
        "name": "OKF Royalty Bridge",
        "schema": ROOT / "schemas" / "okf-royalty-bridge.schema.json",
        "example": ROOT / "examples" / "okf-royalty-bridge.example.yaml",
    }
]


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_target(target: dict) -> bool:
    name = target["name"]
    schema_path = target["schema"]
    example_path = target["example"]

    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_yaml(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(example), key=lambda e: list(e.path))

    if errors:
        print(f"[error] {name} validation failed")
        for error in errors:
            path = ".".join(str(p) for p in error.path) or "<root>"
            print(f"  - path: {path}")
            print(f"    message: {error.message}")
        return False

    print(f"[ok] {name} example is valid")
    return True


def main() -> int:
    all_ok = True

    for target in TARGETS:
        if not validate_target(target):
            all_ok = False

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
