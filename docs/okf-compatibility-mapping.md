# OKF Compatibility Mapping

## Overview

This document defines how OKF frontmatter fields can be mapped into the OKF Royalty OS Bridge model.

OKF is treated as the portable knowledge container.
Royalty OS is treated as the trace, evidence, attribution, compute access right, and allocation governance layer.

This mapping does not modify OKF.
Instead, it defines how existing OKF metadata can be interpreted by an external bridge record.

```text
OKF frontmatter
  └─ portable knowledge metadata

OKF Royalty Bridge
  ├─ okf_document
  ├─ origin
  ├─ evidence
  ├─ attribution
  ├─ compute_access_right
  ├─ allocation
  └─ lifecycle
```

## Design Principle

The bridge must preserve OKF compatibility.

Therefore:

* OKF documents remain Markdown files with YAML frontmatter.
* Royalty OS governance data is represented as an external bridge record.
* OKF fields are not treated as complete rights records.
* OKF fields are treated as metadata signals that can support trace, evidence, lifecycle, and attribution workflows.

## OKF Field Mapping

| OKF frontmatter field | Bridge target                                                   | Mapping role                                                                |
| --------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `type`                | `okf_document.okf_type`                                         | Identifies the OKF concept type.                                            |
| `title`               | `okf_document.title`                                            | Provides the human-readable knowledge title.                                |
| `description`         | `okf_document.description`                                      | Provides a summary of the knowledge package.                                |
| `resource`            | `okf_document.resource`, `evidence.ref`, `origin.origin_uri`    | Connects the OKF document to an external source or authoritative reference. |
| `tags`                | `okf_document.tags`, `allocation.policy_tags`                   | Provides topic and policy classification hints.                             |
| `timestamp`           | `okf_document.timestamp`, `created_at`, `lifecycle.review_note` | Provides temporal context for creation, update, or review.                  |

## Mapping Semantics

### `type`

The OKF `type` field is mapped to:

```text
okf_document.okf_type
```

This field identifies the type of knowledge represented by the OKF document.

The bridge does not redefine OKF types.
It only records the type value used by the OKF document.

### `title`

The OKF `title` field is mapped to:

```text
okf_document.title
```

The title is used as the human-readable label for the referenced knowledge package.

### `description`

The OKF `description` field is mapped to:

```text
okf_document.description
```

The description provides context for review, indexing, and downstream agent interpretation.

### `resource`

The OKF `resource` field may be mapped to multiple bridge fields:

```text
okf_document.resource
evidence.ref
origin.origin_uri
```

The bridge treats `resource` as a strong evidence candidate, but not as complete proof of origin by itself.

A resource can indicate where the knowledge is documented, hosted, derived from, or externally referenced.

### `tags`

The OKF `tags` field is mapped to:

```text
okf_document.tags
allocation.policy_tags
```

Tags do not determine ownership or allocation by themselves.

However, they can support classification, policy routing, domain filtering, and later compute access decisions.

### `timestamp`

The OKF `timestamp` field may be mapped to:

```text
okf_document.timestamp
created_at
lifecycle.review_note
```

The timestamp provides temporal context.

It may indicate the creation or update time of the OKF document, but should not be treated as a complete lifecycle record without review.

## Compatibility Rules

### Rule 1: Do not require OKF modification

A valid bridge implementation must not require custom OKF frontmatter fields.

### Rule 2: Treat OKF metadata as signals

OKF metadata can support governance, but does not replace evidence, attribution, or compute access rights.

### Rule 3: Keep governance external

Royalty OS governance data should remain in a separate bridge record unless a future OKF extension explicitly supports such fields.

### Rule 4: Preserve human readability

Both OKF documents and bridge records should remain readable and reviewable by humans.

### Rule 5: Preserve agent readability

The mapping should remain simple enough for AI agents to parse, validate, and apply without proprietary tooling.

## Minimal Mapping Flow

```text
OKF document
  ├─ type
  ├─ title
  ├─ description
  ├─ resource
  ├─ tags
  └─ timestamp
        ↓
OKF Frontmatter Mapping
        ↓
OKF Royalty Bridge Record
        ↓
Trace / Evidence / Attribution / Compute Access Right / Allocation
```

## Status

This document defines the v0.2 compatibility layer.

v0.1 defined the bridge record.
v0.2 defines how OKF frontmatter fields can be interpreted by the bridge.
