# ADR 0003: Baseline Forecasting Model Selection

- **Status:** Accepted
- **Date:** 2026-08-08
- **Decision Makers:** Project Owner / AI Engineering Team

## Context

GridWise AI requires a forecasting model that can establish a strong baseline before more complex approaches are considered.

The project should avoid introducing deep learning complexity without evidence that it provides meaningful improvement.

## Options Considered

### Option 1: Historical Average

Predict demand using a historical average for a comparable time period.

### Option 2: Linear Regression

Use engineered temporal and weather features with a linear model.

### Option 3: ARIMA/SARIMA

Use classical statistical time-series modeling.

### Option 4: XGBoost

Use gradient-boosted decision trees with engineered temporal and weather features.

## Decision

The project will establish a **simple historical baseline first**, followed by **XGBoost as the primary machine-learning benchmark**.

## Rationale

The historical baseline provides a simple reference point.

XGBoost is selected as the primary ML benchmark because it:

- Performs strongly on structured/tabular data
- Captures nonlinear relationships
- Works well with engineered lag features
- Trains relatively efficiently
- Provides feature importance information

## Consequences

### Positive

- Strong benchmark for later models
- Efficient experimentation
- Explainable feature importance
- Avoids unnecessary deep-learning complexity

### Negative

- Requires careful feature engineering
- Does not inherently model temporal sequences

## Model Selection Rule

A more complex model, such as an LSTM, will only be introduced if:

1. XGBoost performance is insufficient, or
2. The experiment demonstrates meaningful improvement from sequential modeling.

Model selection will be based on validation metrics rather than model complexity.

## Reconsideration

The decision may be revisited if experiments show that another forecasting approach provides significantly better performance or operational value.