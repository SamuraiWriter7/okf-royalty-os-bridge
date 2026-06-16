# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-based development style. Early versions may evolve quickly as schemas, examples, validation scripts, and governance documents are refined.

## [v0.5.0-candidate] - 2026-06-16

### Added

* Added v0.5 usage layer: **Agent Consumption Event**.
* Added documentation:

  * `docs/agent-consumption-event.md`
* Added schema:

  * `schemas/agent-consumption-event.schema.json`
* Added example:

  * `examples/agent-consumption-event.example.yaml`

### Defined

* Defined `agent_consumption_event` as the v0.5 usage event record.
* Defined how AI agents consume OKF-linked knowledge packages under Royalty OS governance.
* Defined how usage events connect to:

  * agents
  * OKF documents
  * bridge records
  * compute access policy integration records
  * trace links
  * decision snapshots
  * generated usage traces
  * output context
  * usage logging
  * human review

### Agent Model

* Introduced `agent` for identifying the consuming AI or workflow actor.
* Added support for agent types:

  * `llm_agent`
  * `retrieval_agent`
  * `workflow_agent`
  * `indexer`
  * `human_assisted_agent`
  * `other`

### Consumed Asset Model

* Introduced `consumed_asset` for connecting an event to:

  * `okf_document`
  * `bridge_record`
  * `policy_integration`
  * `trace_links`

### Policy Context

* Introduced `policy_context` for recording the policy state at the time of consumption.
* Added support for:

  * `policy_id`
  * `enforcement_mode`
  * `deny_if_no_policy`
  * `decision_snapshot`

### Consumption Actions

* Added support for the following consumption actions:

  * `read`
  * `index`
  * `embed`
  * `retrieve`
  * `reason`
  * `generate`
  * `train`
  * `fine_tune`
  * `redistribute`

### Trace Context

* Introduced `trace_context` for connecting agent usage to trace records.
* Added support for:

  * `source_trace_ids`
  * `generated_usage_trace_id`
  * `attribution_required`
  * `allocation_triggered`

### Output Context

* Introduced `output_context` for recording whether consumption generated an output.
* Added support for:

  * `output_generated`
  * `output_ref`
  * `output_hash`
  * `attribution_note_required`

### Usage Logging

* Introduced `usage_logging` for recording usage log requirements and status.
* Added support for log statuses:

  * `pending`
  * `recorded`
  * `skipped`
  * `failed`

### Review Model

* Added review boundary for agent consumption events.
* Clarified that review-gated actions should not trigger allocation until approved.
* Clarified that generation, training, fine-tuning, redistribution, and cross-agent propagation may require stronger review.

### Validation

* Updated `scripts/validate_examples.py` to validate:

  * `OKF Royalty Bridge`
  * `OKF Frontmatter Mapping`
  * `Trace Layer Auto-Link`
  * `Compute Access Policy Integration`
  * `Agent Consumption Event`
* Confirmed GitHub Actions validation passes with the new v0.5 example.

### Fixed

* Removed stray Markdown code fences from the YAML example.
* Corrected `trace_links` nesting under `consumed_asset`.
* Preserved strict schema enforcement using `additionalProperties: false`.
* Confirmed that schema validation catches misplaced usage-context fields and structural drift.

### Status

* v0.5 Agent Consumption Event is active.
* The repository now supports:

  * v0.1 Bridge Record
  * v0.2 OKF Compatibility Mapping
  * v0.3 Trace Layer Auto-Link
  * v0.4 Compute Access Policy Integration
  * v0.5 Agent Consumption Event

### Next Expected Direction

* v0.6: Allocation Trigger Event

---

## [v0.4.0-candidate] - 2026-06-16

### Added

* Added v0.4 policy layer: **Compute Access Policy Integration**.
* Added documentation:

  * `docs/compute-access-policy-integration.md`
* Added schema:

  * `schemas/compute-access-policy-integration.schema.json`
* Added example:

  * `examples/compute-access-policy-integration.example.yaml`

### Defined

* Defined `compute_access_policy_integration` as the v0.4 policy integration record.
* Defined how OKF-compatible knowledge documents, bridge records, and trace links can be connected to compute access policies.
* Defined how AI/agent usage actions can be governed through explicit policy decisions.

### Governed Actions

* Added support for the following governed AI/agent actions:

  * `read`
  * `index`
  * `embed`
  * `retrieve`
  * `reason`
  * `generate`
  * `train`
  * `fine_tune`
  * `redistribute`

### Policy Decisions

* Added support for the following policy decisions:

  * `permit`
  * `deny`
  * `review_required`

### Enforcement Modes

* Added support for the following enforcement modes:

  * `advisory`
  * `audit_only`
  * `review_gate`
  * `blocking`

### Policy Model

* Introduced `policy_ref` for linking a knowledge package to a compute access policy.
* Introduced `linked_assets` for connecting:

  * OKF document
  * bridge record
  * trace links
* Introduced `policy_scope` for defining which assets and actions the policy applies to.
* Introduced `access_rules` for action-level permission decisions.
* Introduced `enforcement` for usage checking, logging, and denial behavior.
* Introduced `review` for human or governance review status.

### Default Safety Boundary

* Added support for:

```text
deny_if_no_policy: true
```

* Clarified that readable or traceable knowledge should not automatically imply permission for training, fine-tuning, redistribution, or commercial reuse.
* Clarified that compute access is policy-bound, not merely trace-bound.

### Validation

* Updated `scripts/validate_examples.py` to validate:

  * `OKF Royalty Bridge`
  * `OKF Frontmatter Mapping`
  * `Trace Layer Auto-Link`
  * `Compute Access Policy Integration`
* Confirmed GitHub Actions validation passes with the new v0.4 example.

### Fixed

* Corrected `trace_links` nesting under `linked_assets`.
* Preserved strict schema enforcement using `additionalProperties: false`.
* Confirmed that schema validation catches misplaced policy fields and structural drift.

### Status

* v0.4 Compute Access Policy Integration is active.
* The repository now supports:

  * v0.1 Bridge Record
  * v0.2 OKF Compatibility Mapping
  * v0.3 Trace Layer Auto-Link
  * v0.4 Compute Access Policy Integration

### Next Expected Direction

* v0.5: Agent Consumption Event

---

## [v0.3.0-candidate] - 2026-06-16

### Added

* Added v0.3 trace automation layer: **Trace Layer Auto-Link**.
* Added documentation:

  * `docs/trace-layer-auto-link.md`
* Added schema:

  * `schemas/trace-layer-auto-link.schema.json`
* Added example:

  * `examples/trace-layer-auto-link.example.yaml`

### Defined

* Defined `trace_layer_auto_link` as the v0.3 trace-linking record.
* Defined how OKF-compatible knowledge documents and bridge records can be connected to trace records.
* Defined reviewable auto-generated candidate links between:

  * OKF documents
  * OKF Royalty Bridge records
  * origin traces
  * evidence traces
  * attribution traces
  * usage traces
  * review traces

### Trace Link Types

* Added support for the following link types:

  * `okf_to_bridge`
  * `bridge_to_origin_trace`
  * `bridge_to_evidence_trace`
  * `bridge_to_attribution_trace`
  * `bridge_to_usage_trace`
  * `resource_to_evidence`
  * `timestamp_to_lifecycle`

### Auto-Link Sources

* Added support for auto-link source signals:

  * `okf.path`
  * `okf.resource`
  * `okf.timestamp`
  * `okf.tags`
  * `bridge.origin`
  * `bridge.evidence`
  * `bridge.attribution`
  * `git.commit`
  * `manual.review`

### Review Model

* Introduced a review boundary for generated trace links.
* Defined generated link statuses:

  * `candidate`
  * `review`
  * `active`
  * `rejected`
  * `deprecated`
* Clarified that auto-generated links should not become authoritative by default.
* Clarified that human review may be required before candidate trace links become active governance connections.

### Validation

* Updated `scripts/validate_examples.py` to validate:

  * `OKF Royalty Bridge`
  * `OKF Frontmatter Mapping`
  * `Trace Layer Auto-Link`
* Confirmed GitHub Actions validation passes with the new v0.3 example.

### Status

* v0.3 Trace Layer Auto-Link is active.
* The repository now supports:

  * v0.1 Bridge Record
  * v0.2 OKF Compatibility Mapping
  * v0.3 Trace Layer Auto-Link

### Next Expected Direction

* v0.4: Compute Access Policy Integration

---

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
* Introduced `origin` as the 震源 / origin record of the knowledge package.
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

