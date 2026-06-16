# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-based development style. Early versions may evolve quickly as schemas, examples, validation scripts, and governance documents are refined.

## [v0.2.0-candidate] - 2026-06-16

### Added

* Added v0.2 compatibility layer: **OKF Compatibility Mapping**.
* Added documentation:

  * `docs/okf-compatibility-mapping.md`
* Added schema:

  * `schemas/okf-frontmatter-mapping.schema.json`
* Added example:

  * `examples/okf-frontmatter-mapping.example.yaml`

### Defined

* Defined `okf_frontmatter_mapping` as the v0.2 compatibility record.
* Defined how OKF frontmatter fields can be interpreted by the bridge layer:

  * `type`
  * `title`
  * `description`
  * `resource`
  * `tags`
  * `timestamp`

### Mapping Model

* Mapped `type` to:

  * `okf_document.okf_type`
* Mapped `title` to:

  * `okf_document.title`
* Mapped `description` to:

  * `okf_document.description`
* Mapped `resource` to:

  * `okf_document.resource`
  * `evidence.ref`
  * `origin.origin_uri`
* Mapped `tags` to:

  * `okf_document.tags`
  * `allocation.policy_tags`
* Mapped `timestamp` to:

  * `okf_document.timestamp`
  * `lifecycle.review_note`

### Compatibility Rules

* Clarified that the bridge does not modify OKF.
* Clarified that the bridge does not require custom OKF fields.
* Clarified that Royalty OS governance data remains in an external bridge record.
* Clarified that OKF metadata should be treated as governance signals, not complete rights records.
* Clarified that compatibility must preserve both human readability and agent readability.

### Validation

* Updated `scripts/validate_examples.py` to validate both:

  * `OKF Royalty Bridge`
  * `OKF Frontmatter Mapping`
* Confirmed GitHub Actions validation passes with the new v0.2 example.

### Fixed

* Removed stray Markdown code fences from the YAML example.
* Corrected YAML indentation under `mapping_rules`.
* Preserved clean YAML structure for validation through PyYAML and JSON Schema.

### Status

* v0.2 compatibility mapping is active.
* The repository now supports:

  * v0.1 Bridge Record
  * v0.2 OKF Compatibility Mapping

### Next Expected Direction

* v0.3: Trace Layer Auto-Link

---

## [v0.1.0-candidate] - 2026-06-16

### Added

* Added initial repository structure for **OKF Royalty OS Bridge**.
* Added `schemas/okf-royalty-bridge.schema.json`.
* Added `examples/okf-royalty-bridge.example.yaml`.
* Added `scripts/validate_examples.py`.
* Added GitHub Actions workflow:

  * `.github/workflows/validate-examples.yml`

### Defined

* Defined the first `okf_royalty_bridge` record structure.
* Defined the minimum bridge fields:

  * `schema_version`
  * `id`
  * `created_at`
  * `okf_document`
  * `origin`
  * `evidence`
  * `attribution`
  * `compute_access_right`
  * `allocation`
  * `lifecycle`

### Bridge Model

* Introduced `okf_document` as the reference to an OKF-compatible knowledge file.
* Introduced `origin` as the震源 / origin record of the knowledge package.
* Introduced `evidence` as the proof layer for attribution and review.
* Introduced `attribution` as the contributor and contribution-weight model.
* Introduced `compute_access_right` as the AI/agent usage permission boundary.
* Introduced `allocation` as the basis for value return.
* Introduced `lifecycle` as the publication and review state.

### Validation

* Added local validation through:

```bash
python scripts/validate_examples.py
```

* Added Python syntax check through:

```bash
python -m py_compile scripts/validate_examples.py
```

* Added GitHub Actions validation for schema/example consistency.

### Design Notes

* OKF is treated as the knowledge container.
* Royalty OS is treated as the trace, evidence, attribution, and value-return governance layer.
* This bridge does not replace or modify OKF.
* The bridge is designed as an external governance record that can be attached to OKF-compatible knowledge documents.

### Status

* Initial candidate version.
* Validated by local script and GitHub Actions.
* Foundation for v0.2 OKF Compatibility Mapping.
