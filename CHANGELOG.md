# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-based development style. Early versions may evolve quickly as schemas, examples, validation scripts, and governance documents are refined.

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
* Ready for validation and first GitHub Actions check.
* Next expected direction:

  * README refinement
  * release notes
  * v0.2 extension toward OKF frontmatter mapping or lifecycle review model
