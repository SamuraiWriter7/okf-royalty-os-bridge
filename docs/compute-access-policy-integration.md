# Compute Access Policy Integration

## Overview

Compute Access Policy Integration defines how OKF-compatible knowledge documents, OKF Royalty Bridge records, and trace-layer links can be connected to explicit AI/agent usage policies.

v0.1 introduced the bridge record.
v0.2 introduced OKF compatibility mapping.
v0.3 introduced trace-layer auto-linking.
v0.4 introduces compute access policy integration.

```text
OKF document
  ↓
OKF Compatibility Mapping
  ↓
OKF Royalty Bridge Record
  ↓
Trace Layer Auto-Link
  ↓
Compute Access Policy Integration
  ↓
Permitted / denied / review-gated AI usage
```

## Purpose

A traceable knowledge package still needs explicit usage boundaries.

This layer defines how a governed OKF knowledge package can be connected to compute access rules for AI and agent workflows.

The goal is to clarify:

* which AI actions are permitted
* which AI actions are denied
* which AI actions require human review
* which trace/evidence records must be checked before usage
* whether usage should be logged
* whether missing policy should block usage

## Core Concept

Compute access policy is not the same as attribution.

Attribution answers:

```text
Who contributed to this knowledge?
```

Compute access policy answers:

```text
What may an AI system do with this knowledge?
```

v0.4 connects the two.

```text
traceable knowledge
  → policy check
  → permitted action / denied action / review gate
  → usage log
  → allocation or governance event
```

## Governed Actions

The v0.4 model supports policies for the following AI/agent actions:

* `read`
* `index`
* `embed`
* `retrieve`
* `reason`
* `generate`
* `train`
* `fine_tune`
* `redistribute`

## Policy Decisions

Each action can be assigned a policy decision:

* `permit`
* `deny`
* `review_required`

## Enforcement Modes

The policy integration layer supports the following enforcement modes:

* `advisory`
* `audit_only`
* `review_gate`
* `blocking`

### `advisory`

The policy is visible to agents and reviewers, but does not block usage.

### `audit_only`

Usage is allowed, but usage events should be logged.

### `review_gate`

Usage requires human or governance review before activation.

### `blocking`

Usage should be denied unless an explicit policy permits it.

## Human Review Boundary

Some compute actions should not be automatically permitted even if a trace exists.

For example:

* training
* fine-tuning
* redistribution
* commercial reuse
* cross-agent propagation

These actions may require review before usage.

```text
policy signal
  → rule match
  → review required
  → approved / rejected
  → usage event
```

## Missing Policy Rule

A governed knowledge system should define what happens when no policy exists.

Recommended default:

```text
deny_if_no_policy: true
```

This means the system should not assume permission merely because a knowledge package is readable.

## Relationship to Previous Layers

### v0.1 Bridge Record

Defines the governed knowledge package and its origin/evidence/attribution/allocation fields.

### v0.2 OKF Compatibility Mapping

Defines how OKF frontmatter can be interpreted without modifying OKF.

### v0.3 Trace Layer Auto-Link

Defines candidate links between OKF documents, bridge records, and trace records.

### v0.4 Compute Access Policy Integration

Defines which AI/agent actions are permitted, denied, review-gated, or logged.

## Status

This document defines the v0.4 Compute Access Policy Integration model.

v0.4 moves the repository from trace-aware governance toward policy-aware AI usage control.
