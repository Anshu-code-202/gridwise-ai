# ADR 0004: Feature Engineering Strategy

- **Status:** Accepted
- **Date:** 2026-08-08
- **Decision Makers:** Project Owner / AI Engineering Team

## Context

Electricity demand depends on historical demand patterns, time of day, day of week, seasonality, and weather.

Tree-based machine-learning models require these relationships to be represented explicitly as features.

## Decision

GridWise AI will use domain-informed temporal and weather feature engineering.

## Feature Categories

### Temporal Features

- Hour of day
- Day of week
- Day of month
- Month
- Weekend indicator

### Lag Features

- Previous hour
- Previous 24 hours
- Previous 168 hours

### Rolling Features

- 24-hour rolling mean
- 24-hour rolling standard deviation
- 7-day rolling mean

### Weather Features

Where available:

- Temperature
- Humidity
- Wind speed
- Other relevant weather variables

## Rationale

Lag features capture recent demand behavior.

Daily and weekly lags represent recurring consumption patterns.

Rolling statistics provide information about recent demand levels and volatility.

Weather features allow the model to learn relationships between environmental conditions and electricity demand.

## Data Leakage Prevention

Feature engineering must only use information that would have been available at prediction time.

Future observations must never be used to construct historical features.

## Consequences

### Positive

- Better representation of temporal behavior
- Improved compatibility with tree-based models
- More interpretable feature relationships

### Negative

- Feature engineering increases pipeline complexity
- Initial observations may be lost because lag values are unavailable

## Reconsideration

Feature engineering may be expanded after exploratory analysis identifies additional useful variables.