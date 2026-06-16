# Agent Consumption Event

## Overview

Agent Consumption Event defines how AI agents consume OKF-linked knowledge packages under Royalty OS governance.

v0.1 introduced the bridge record.
v0.2 introduced OKF compatibility mapping.
v0.3 introduced trace-layer auto-linking.
v0.4 introduced compute access policy integration.
v0.5 introduces agent consumption event logging.

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
Agent Consumption Event
  ↓
Usage Trace / Review / Allocation Trigger
```

## Purpose

A policy-aware knowledge package still needs usage evidence.

This layer defines a record for documenting when an AI agent consumes an OKF-linked knowledge package.

The goal is to clarify:

* which agent consumed the knowledge
* which OKF document or bridge record was used
* which compute access policy was checked
* what action was performed
* whether the action was permitted, denied, or review-gated
* whether usage should be logged
* whether attribution or allocation should be triggered
* whether human review is required

## Core Concept

Compute access policy answers:

```text
What may an AI system do with this knowledge?
```

Agent Consumption Event answers:

```text
What did an AI system actually do with this knowledge?
```

v0.5 connects policy to actual usage.

```text
policy-bound knowledge
  → agent action
  → consumption event
  → usage trace
  → review status
  → allocation or governance event
```

## Supported Consumption Actions

The v0.5 model supports the following agent actions:

* `read`
* `index`
* `embed`
* `retrieve`
* `reason`
* `generate`
* `train`
* `fine_tune`
* `redistribute`

These actions are aligned with v0.4 Compute Access Policy Integration.

## Event Lifecycle

An agent consumption event should move through a reviewable lifecycle:

```text
observed
  → logged
  → reviewed
  → approved / rejected
  → allocation_triggered / closed
```

## Policy Relationship

An Agent Consumption Event must reference a policy context.

The event should record:

* the policy ID
* the policy integration record
* the action decision
* whether human review was required
* whether the action was permitted or blocked

## Trace Relationship

An Agent Consumption Event should connect to trace records.

It may reference:

* OKF document path
* bridge record ID
* trace link IDs
* source trace IDs
* generated usage trace ID
* output reference or output hash

## Human Review Boundary

Some consumption events should not become final automatically.

For example:

* generation using governed knowledge
* training
* fine-tuning
* redistribution
* commercial reuse
* cross-agent propagation

These may require review before allocation or governance actions are triggered.

## Allocation Trigger

An Agent Consumption Event may trigger allocation when:

* a governed knowledge package was used
* trace links are active or reviewed
* policy permits or review approves the usage
* attribution is required
* usage logging is recorded

The event itself does not calculate payment.

It records the condition that may trigger a later allocation or royalty event.

## Status

This document defines the v0.5 Agent Consumption Event model.

v0.5 moves the repository from policy-aware usage control toward usage-aware trace and allocation governance.
