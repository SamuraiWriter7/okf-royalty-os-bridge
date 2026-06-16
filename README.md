# OKF Royalty OS Bridge

A bridge specification connecting OKF knowledge packages with Royalty OS trace, evidence, attribution, and compute access rights.

## Overview

**OKF Royalty OS Bridge** defines a minimal governance bridge between OKF-compatible knowledge documents and Royalty OS governance structures.

OKF provides a lightweight knowledge exchange format based on Markdown files with YAML frontmatter. This repository does not replace or modify OKF. Instead, it defines an external bridge record that connects OKF knowledge packages to:

* origin traceability
* evidence records
* contributor attribution
* compute access rights
* allocation basis
* lifecycle review state

The purpose of this repository is to make knowledge files not only portable, but also traceable, attributable, and governance-ready.

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
  └─ lifecycle state
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

This repository treats knowledge as an intelligence asset that can be shared, audited, reviewed, and governed.

## v0.1.0-candidate Scope

The first candidate version defines the minimum bridge record:

* `okf_document`: the OKF-compatible knowledge file being referenced
* `origin`: the source or震源 of the knowledge
* `evidence`: supporting proof for attribution
* `attribution`: contributors and contribution weights
* `compute_access_right`: permitted AI/agent usage
* `allocation`: basis for value return
* `lifecycle`: review and publication state

## Repository Structure

```text
schemas/
  okf-royalty-bridge.schema.json

examples/
  okf-royalty-bridge.example.yaml

scripts/
  validate_examples.py

.github/
  workflows/
    validate-examples.yml
```

## Schema

The main schema is:

```text
schemas/okf-royalty-bridge.schema.json
```

It validates the structure of an `okf_royalty_bridge` record.

## Example

The reference example is:

```text
examples/okf-royalty-bridge.example.yaml
```

This example demonstrates how an OKF-compatible knowledge document can be connected to Royalty OS trace, evidence, attribution, compute access rights, allocation rules, and lifecycle review.

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
* YAML example validation against the JSON Schema

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

## Status

**v0.1.0-candidate**

Initial bridge layer between OKF-compatible knowledge documents and Royalty OS governance.

This version establishes the first working structure for connecting portable AI knowledge files with trace, evidence, attribution, compute access rights, and allocation logic.

## License

TBD.
