# OKF Royalty OS Bridge

A bridge specification connecting OKF knowledge packages with Royalty OS trace, evidence, attribution, compute access rights, and trace-layer auto-linking.

## Overview

**OKF Royalty OS Bridge** defines a minimal governance bridge between OKF-compatible knowledge documents and Royalty OS governance structures.

OKF provides a lightweight knowledge exchange format based on Markdown files with YAML frontmatter. This repository does not replace or modify OKF. Instead, it defines external bridge records that connect OKF knowledge packages to:

* origin traceability
* evidence records
* contributor attribution
* compute access rights
* allocation basis
* lifecycle review state
* OKF frontmatter compatibility mapping
* trace-layer auto-linking

The purpose of this repository is to make knowledge files not only portable, but also traceable, attributable, reviewable, and governance-ready.

## Core Concept

```text
OKF document
  └─ knowledge package

OKF Royalty Bridge
  ├─ origin trace
  ├─ evidence record
  ├─ attribution model
  ├─ compute access right
  ├─ allocation basis
  ├─ lifecycle state
  ├─ OKF compatibility mapping
  └─ trace-layer auto-link
```

OKF defines the portable knowledge container.

Royalty OS defines the trace, evidence, attribution, and return logic around that knowledge.

This bridge connects the two without breaking OKF compatibility.

## Why This Matters

As AI agents increasingly exchange structured knowledge instead of raw text, knowledge packages need more than readability.

They also need:

* clear origin records
* evidence of source and transformation
* attribution of contributors
* permission boundaries for AI usage
* review status before reuse
* allocation logic for value return
* compatibility rules for interpreting OKF metadata
* trace-layer links between knowledge documents, bridge records, and evidence records

This repository treats knowledge as an intelligence asset that can be shared, audited, reviewed, governed, and eventually connected to value circulation.

## Version Scope

### v0.1.0-candidate: Bridge Record

The first candidate version defined the minimum bridge record:

* `okf_document`: the OKF-compatible knowledge file being referenced
* `origin`: the source or震源 of the knowledge
* `evidence`: supporting proof for attribution
* `attribution`: contributors and contribution weights
* `compute_access_right`: permitted AI/agent usage
* `allocation`: basis for value return
* `lifecycle`: review and publication state

### v0.2.0-candidate: OKF Compatibility Mapping

The second candidate version defined how OKF frontmatter fields can be interpreted by the bridge layer.

It added a compatibility mapping between OKF metadata and Royalty OS bridge targets.

This version clarified how the following OKF fields can be read by the bridge:

* `type`
* `title`
* `description`
* `resource`
* `tags`
* `timestamp`

The goal is to preserve OKF compatibility while enabling trace, evidence, attribution, compute access rights, allocation, and lifecycle governance.

### v0.3.0-candidate: Trace Layer Auto-Link

The third candidate version defines how OKF-compatible knowledge documents and OKF Royalty Bridge records can be automatically connected to trace records.

It introduces a machine-readable auto-link model for connecting:

* OKF documents to bridge records
* bridge records to origin traces
* bridge records to evidence traces
* bridge records to attribution traces
* bridge records to usage traces
* OKF resources to evidence records
* OKF timestamps to lifecycle review context

This version does not make auto-generated links authoritative by default.

Instead, it treats them as candidate trace links that may require review before activation.

## Trace Layer Auto-Link

v0.3 introduces an explicit trace-linking layer:

```text
OKF document
  ↓
OKF Compatibility Mapping
  ↓
OKF Royalty Bridge Record
  ↓
Trace Layer Auto-Link
  ↓
Origin / Evidence / Attribution / Usage Trace
```

The auto-link layer supports the following link types:

* `okf_to_bridge`
* `bridge_to_origin_trace`
* `bridge_to_evidence_trace`
* `bridge_to_attribution_trace`
* `bridge_to_usage_trace`
* `resource_to_evidence`
* `timestamp_to_lifecycle`

The recommended lifecycle for generated links is:

```text
candidate
  → review
  → active
  → deprecated / rejected
```

This preserves the distinction between automatic trace discovery and confirmed governance records.

## Repository Structure

```text
docs/
  okf-compatibility-mapping.md
  trace-layer-auto-link.md

schemas/
  okf-royalty-bridge.schema.json
  okf-frontmatter-mapping.schema.json
  trace-layer-auto-link.schema.json

examples/
  okf-royalty-bridge.example.yaml
  okf-frontmatter-mapping.example.yaml
  trace-layer-auto-link.example.yaml

scripts/
  validate_examples.py

.github/
  workflows/
    validate-examples.yml
```

## Schemas

The current schemas are:

```text
schemas/okf-royalty-bridge.schema.json
schemas/okf-frontmatter-mapping.schema.json
schemas/trace-layer-auto-link.schema.json
```

### OKF Royalty Bridge Schema

`okf-royalty-bridge.schema.json` validates the structure of an `okf_royalty_bridge` record.

It defines how an OKF-compatible knowledge document can be connected to origin, evidence, attribution, compute access rights, allocation, and lifecycle governance.

### OKF Frontmatter Mapping Schema

`okf-frontmatter-mapping.schema.json` validates the structure of an `okf_frontmatter_mapping` record.

It defines how OKF frontmatter fields can be mapped into bridge targets without modifying OKF itself.

### Trace Layer Auto-Link Schema

`trace-layer-auto-link.schema.json` validates the structure of a `trace_layer_auto_link` record.

It defines how OKF documents, bridge records, and trace records can be connected through reviewable auto-generated candidate links.

## Examples

The reference examples are:

```text
examples/okf-royalty-bridge.example.yaml
examples/okf-frontmatter-mapping.example.yaml
examples/trace-layer-auto-link.example.yaml
```

These examples demonstrate:

* how an OKF-compatible knowledge document can be connected to Royalty OS governance
* how OKF frontmatter fields can be interpreted by the bridge layer
* how candidate trace links can connect OKF documents, bridge records, and trace records
* how compatibility can be preserved without adding custom OKF fields

## Documentation

The current documentation files are:

```text
docs/okf-compatibility-mapping.md
docs/trace-layer-auto-link.md
```

## Validation

Install dependencies:

```bash
pip install pyyaml jsonschema
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected result:

```text
[validate] OKF Royalty Bridge
  schema : schemas/okf-royalty-bridge.schema.json
  example: examples/okf-royalty-bridge.example.yaml
[ok] OKF Royalty Bridge example is valid
[validate] OKF Frontmatter Mapping
  schema : schemas/okf-frontmatter-mapping.schema.json
  example: examples/okf-frontmatter-mapping.example.yaml
[ok] OKF Frontmatter Mapping example is valid
[validate] Trace Layer Auto-Link
  schema : schemas/trace-layer-auto-link.schema.json
  example: examples/trace-layer-auto-link.example.yaml
[ok] Trace Layer Auto-Link example is valid
```

## GitHub Actions

This repository includes a validation workflow:

```text
.github/workflows/validate-examples.yml
```

The workflow runs on:

* push to `main`
* pull request
* manual dispatch

It checks:

* Python syntax
* YAML example validation against JSON Schema

## Design Principles

### 1. Do not modify OKF

The bridge should not require changing the OKF core format.

OKF remains the knowledge container.

The bridge record remains the governance connector.

### 2. Keep the bridge portable

The bridge should work with plain files, Git repositories, agent workflows, and future knowledge graph systems.

### 3. Make origin visible

Every governed knowledge package should be connected to an origin record.

### 4. Separate knowledge from rights

Knowledge content and compute access rights should be related, but not collapsed into one layer.

### 5. Support human review

AI-readable governance should still preserve human review boundaries.

### 6. Treat OKF metadata as signals

OKF frontmatter fields can support governance interpretation, but they do not replace evidence, attribution, review, or allocation logic.

### 7. Preserve compatibility before extension

The bridge should first clarify compatibility before adding deeper automation, policy engines, or trace-layer integration.

### 8. Treat auto-links as candidates

Trace Layer Auto-Link should generate candidate links, not final authority.

Human review may be required before links become active governance connections.

## Status

**v0.3.0-candidate**

This version adds Trace Layer Auto-Link.

v0.1 established the first working bridge record between OKF-compatible knowledge documents and Royalty OS governance.

v0.2 added the compatibility layer that explains how OKF frontmatter fields can be interpreted by the bridge without modifying OKF.

v0.3 adds reviewable auto-linking between OKF documents, bridge records, and trace records.

## Roadmap

Planned next directions:

```text
v0.1 = Bridge Record
v0.2 = OKF Compatibility Mapping
v0.3 = Trace Layer Auto-Link
v0.4 = Compute Access Policy Integration
v0.5 = Agent Consumption Event
```

## License

TBD.
