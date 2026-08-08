# Project Charter

**Project Name:** GridWise AI

**Version:** 1.0

**Status:** Draft

**Author:** Anshu Arora

**Start Date:** August 2026

**Project Duration:** 8 Weeks

---

# 1. Vision

Enable smarter and more sustainable energy management by building an AI-powered decision support platform that forecasts electricity demand, estimates sustainability impact, and provides explainable recommendations for operational planning.

---

# 2. Mission

Develop a production-style AI engineering project that combines data engineering, machine learning, backend development, and generative AI into a single end-to-end platform.

The project aims to demonstrate engineering best practices while solving a real sustainability challenge aligned with Sustainable Development Goal (SDG) 7 (Affordable and Clean Energy) and SDG 13 (Climate Action).

---

# 3. Problem Statement

Electricity demand changes continuously due to weather conditions, seasonal patterns, holidays, and human activity.

Traditional forecasting approaches often rely on historical averages, statistical models, and manual adjustments made by analysts. While effective in many situations, these methods:

- Require significant manual effort.
- Can struggle with complex, non-linear relationships.
- Are difficult to scale across many regions or assets.
- Provide limited decision support beyond the forecast itself.

Organizations need a system that automates forecasting while helping analysts understand predictions and make better sustainability-focused decisions.

---

# 4. Proposed Solution

GridWise AI is an AI-powered decision support platform that:

- Processes historical energy consumption and weather data.
- Forecasts future electricity demand.
- Estimates sustainability-related metrics.
- Explains important forecasting factors.
- Presents insights through an interactive dashboard.
- Uses an AI assistant to translate predictions into actionable recommendations.

The platform is designed as a modular engineering system rather than a standalone machine learning notebook.

---

# 5. Objectives

## Business Objectives

- Improve energy demand planning.
- Support sustainability initiatives.
- Reduce unnecessary energy generation.
- Demonstrate practical AI applications for clean energy.

## Technical Objectives

- Build an end-to-end data pipeline.
- Develop and compare forecasting models.
- Expose predictions through a REST API.
- Create an interactive dashboard.
- Apply software engineering and MLOps practices.

---

# 6. Target Users

### Primary Users

- Energy analysts
- Grid operators
- Sustainability managers

### Secondary Users

- Students
- Researchers
- Educators

---

# 7. Project Scope

## In Scope

- Historical data ingestion
- Data validation and preprocessing
- Feature engineering
- Time-series forecasting
- Forecast evaluation
- Carbon impact estimation
- REST API
- Interactive dashboard
- Documentation
- Docker-based deployment

## Out of Scope (MVP)

- Real-time smart meter streaming
- User authentication
- Mobile application
- Multi-tenant deployment
- Commercial billing integration

---

# 8. Success Criteria

The project will be considered successful if it:

- Produces accurate demand forecasts using historical and weather data.
- Demonstrates measurable improvement over a simple baseline forecast.
- Provides an intuitive dashboard for exploring predictions.
- Includes clear engineering documentation.
- Is reproducible using Docker.
- Can be presented confidently as a portfolio project.

---

# 9. Constraints

- Zero infrastructure cost.
- Use free or open-source tools.
- Public datasets only.
- Local-first development.
- Designed to be completed within the internship timeline.

---

# 10. Risks

| Risk | Mitigation |
|------|------------|
| Poor data quality | Data validation pipeline |
| Overly complex scope | MVP-first development |
| Model underperformance | Compare multiple forecasting approaches |
| Time limitations | Weekly sprint planning |

---

# 11. Engineering Principles

This project follows these principles:

- Product before technology.
- Data before AI.
- Simplicity before complexity.
- Build modular systems.
- Document every major decision.
- Measure before optimizing.
- Prioritize explainability.
- Keep the project reproducible.

---

# 12. Expected Deliverables

- Source code
- Documentation
- ADR repository
- REST API
- Dashboard
- Forecasting models
- Docker environment
- GitHub repository
- Demonstration video


# 13. Stakeholders

## Primary

- Project Owner (Anshu Arora)
- Internship Mentors (1M1B / IBM SkillsBuild)

## Secondary

- Recruiters
- Technical Interviewers
- Open-source Contributors (future)

# 14. Key Performance Indicators (KPIs)

- Forecast generated for the next 24 hours.
- Baseline model and advanced model compared using MAE and RMSE.
- REST API responds successfully to prediction requests.
- Dashboard visualizes historical and predicted demand.
- Application runs locally using Docker.
- Repository includes complete documentation and ADRs.