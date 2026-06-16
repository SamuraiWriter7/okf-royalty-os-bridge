# Trace Layer Auto-Link

## Overview

Trace Layer Auto-Link defines how OKF-compatible knowledge documents and OKF Royalty Bridge records can be automatically connected to trace records.

v0.1 introduced the bridge record.
v0.2 introduced OKF compatibility mapping.
v0.3 introduces automatic trace linking.

```text id="s3m702"
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

The purpose of this layer is to make trace connection repeatable, reviewable, and machine-readable.

## Purpose

AI agents and knowledge systems need a way to connect portable knowledge packages to their origin and evidence records.

This document defines a minimal auto-link model for:

* linking OKF documents to bridge records
* linking bridge records to origin traces
* linking resource fields to evidence traces
* linking attribution data to contributor traces
* linking timestamp data to lifecycle traces
* preserving human review boundaries before activation

## Core Concept

Trace Layer Auto-Link does not create ownership by itself.

It creates structured candidate links.

Each generated link should be treated as a reviewable trace connection.

```text id="ui690d"
metadata signal
  → auto-link rule
  → generated trace link
  → review status
  → active governance connection
```

## Trace Link Types

The v0.3 model supports the following link types:

* `okf_to_bridge`
* `bridge_to_origin_trace`
* `bridge_to_evidence_trace`
* `bridge_to_attribution_trace`
* `bridge_to_usage_trace`
* `resource_to_evidence`
* `timestamp_to_lifecycle`

## Auto-Link Sources

Auto-linking can use signals from:

* OKF document path
* OKF frontmatter fields
* Bridge record ID
* Bridge evidence records
* Bridge origin fields
* Bridge attribution records
* Git commit references
* manual review notes

## Human Review Boundary

Auto-generated trace links should not become authoritative immediately.

The recommended lifecycle is:

```text id="yy467y"
candidate
  → review
  → active
  → deprecated / rejected
```

This preserves the distinction between automatic trace discovery and confirmed governance records.

## Compatibility Principle

Trace Layer Auto-Link must preserve OKF compatibility.

Therefore:

* It must not require custom OKF fields.
* It must not modify the OKF document format.
* It must operate through external bridge and trace records.
* It must remain human-readable and agent-readable.

## Minimal Flow

```text id="ab3f4c"
1. Read OKF document metadata.
2. Read OKF Royalty Bridge record.
3. Apply auto-link rules.
4. Generate candidate trace links.
5. Require review where necessary.
6. Activate approved links.
```

## Status

This document defines the v0.3 Trace Layer Auto-Link model.

v0.3 moves the repository from compatibility mapping toward trace automation.
