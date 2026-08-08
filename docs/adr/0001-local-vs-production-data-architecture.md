# ADR 0001: Local vs Production Data Architecture

- **Status:** Accepted
- **Date:** 2026-08-06
- **Decision Makers:** Project Owner / AI Engineering Team

## Context

GridWise AI needs to process historical electricity and weather data during development.

The project requires fast local experimentation while also demonstrating an architecture that can evolve toward a multi-service production environment.

Using only CSV files would make analytical workflows harder to manage at scale, while using PostgreSQL from the beginning would introduce unnecessary infrastructure during early exploration.

## Options Considered

### Option 1: CSV/Parquet + Pandas

Use files as the primary analytical storage layer.

**Advantages**
- Very simple
- No database setup
- Easy to share

**Disadvantages**
- Limited SQL workflow
- Less suitable for repeated analytical queries
- Database behavior is not represented

### Option 2: PostgreSQL from Day One

Use PostgreSQL for both exploration and application workloads.

**Advantages**
- Production-style database
- ACID transactions
- Centralized storage

**Disadvantages**
- Additional setup during exploration
- More infrastructure than currently required

### Option 3: DuckDB + PostgreSQL

Use DuckDB for local analytical exploration and PostgreSQL later when application-style persistence is required.

## Decision

We choose **Option 3: Hybrid DuckDB + PostgreSQL architecture**.

DuckDB will be used for local analytical exploration and feature engineering.

PostgreSQL may be introduced later when the project requires a centralized relational database for application services.

## Rationale

- Fast local analytical queries
- Minimal infrastructure during development
- SQL-based workflow
- Clear path toward production-style architecture
- Keeps the MVP cost-free

## Consequences

### Positive

- Faster experimentation
- Low development overhead
- Easy local setup
- Clear migration path

### Negative

- Two database technologies must eventually be maintained
- Some SQL syntax may require adaptation

## Reconsideration

This decision should be reconsidered if:

- Dataset size exceeds local analytical requirements
- Multiple application services require shared transactional storage
- Cloud deployment becomes necessary