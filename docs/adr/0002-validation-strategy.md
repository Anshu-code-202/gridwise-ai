# ADR 0002: Time-Series Validation Strategy

- **Status:** Accepted
- **Date:** 2026-08-08
- **Decision Makers:** Project Owner / AI Engineering Team

## Context

GridWise AI predicts future electricity demand using historical observations.

A standard random train/test split can cause future observations to appear in the training set while earlier observations appear in the test set.

This would produce unrealistic evaluation results.

## Options Considered

### Option 1: Random Train/Test Split

Randomly divide observations into training and testing sets.

**Advantage**
- Simple to implement

**Disadvantage**
- Can introduce temporal leakage
- Does not represent real forecasting conditions

### Option 2: Single Chronological Split

Train on earlier observations and test on later observations.

**Advantages**
- Preserves temporal ordering
- Simple

**Disadvantages**
- Provides only one evaluation period
- Results may depend heavily on the selected test period

### Option 3: Walk-Forward Validation

Repeatedly train on historical data and evaluate on the next chronological period.

## Decision

We choose **Walk-Forward Validation** as the primary evaluation strategy.

## Rationale

The model will be evaluated in the same direction in which it will operate in production:

Past → Training → Future → Prediction

This reduces temporal leakage and provides a more realistic estimate of forecasting performance.

## Consequences

### Positive

- More realistic evaluation
- Reduced risk of temporal leakage
- Better representation of production behavior

### Negative

- More computationally expensive
- More complex than a random split

## Metrics

Primary metrics:

- MAE
- RMSE

MAPE may be reported where appropriate.

## Reconsideration

The validation strategy may be expanded to include rolling-window evaluation or additional backtesting periods as the system evolves.
