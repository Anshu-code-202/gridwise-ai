# ADR 0005: API-First Architecture

- **Status:** Accepted
- **Date:** 2026-08-08
- **Decision Makers:** Project Owner / AI Engineering Team

## Context

GridWise AI will provide forecasts through an interactive dashboard.

A tightly coupled design where Streamlit directly loads and executes the model would make the application harder to test, deploy, and extend.

## Options Considered

### Option 1: Dashboard Directly Calls Model

Streamlit loads the model and performs inference.

### Option 2: REST API Between Dashboard and Model

Streamlit communicates with a FastAPI service responsible for inference.

## Decision

Use an **API-first architecture** in which FastAPI exposes model inference functionality.

The dashboard will communicate with the API rather than directly managing model execution.

## Architecture

User

↓

Streamlit

↓

FastAPI

↓

Forecasting Service

↓

Model

↓

Prediction

## Rationale

This provides:

- Separation of concerns
- Independent testing
- Reusable prediction service
- Easier deployment
- Future support for other clients

For example, a future web application or mobile application could use the same API.

## Consequences

### Positive

- Cleaner architecture
- Better testability
- Easier extension
- Clear service boundaries

### Negative

- Additional service to maintain
- Slightly more development complexity

## Reconsideration

For very small prototypes, direct model execution may be acceptable. The API-first approach is retained because GridWise AI is intentionally being developed as a production-inspired engineering project.