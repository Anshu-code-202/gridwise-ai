# Dataset Selection

## 1. Purpose

GridWise AI requires a historical electricity-demand dataset for developing and evaluating a time-series forecasting system.

The dataset will be used to:

* Understand electricity demand patterns.
* Develop forecasting features.
* Establish statistical and machine-learning baselines.
* Train and evaluate forecasting models.
* Test the project's data engineering pipeline.
* Support future integration with weather data.
* Demonstrate a realistic sustainability-oriented AI use case.

The dataset selection should prioritize **data quality, reproducibility, forecasting suitability, and alignment with the project's sustainability objective** rather than simply choosing the largest available dataset.

---

## 2. Project Data Requirements

The primary dataset should ideally provide:

1. Timestamped electricity demand/load observations.
2. A consistent time interval, preferably hourly or finer.
3. Sufficient historical coverage to capture:

   * Daily seasonality
   * Weekly seasonality
   * Seasonal/yearly variation
4. A sufficient number of observations for machine-learning experiments.
5. Publicly accessible data.
6. Clear documentation and provenance.
7. A license or usage policy suitable for an educational portfolio project.
8. Data that can be processed locally using Python and DuckDB.
9. Compatibility with future PostgreSQL-based application workflows.
10. The ability to integrate external weather information later.

---

## 3. Candidate Datasets

The initial candidates are:

### Candidate 1 — PJM Hourly Energy Consumption

A regional electricity-consumption time series suitable for forecasting experiments.

**Potential strengths:**

* Hourly electricity demand.
* Long historical time series.
* Suitable for supervised time-series forecasting.
* Suitable for lag and rolling-window feature engineering.
* Suitable for XGBoost and potentially LSTM experiments.
* Relatively straightforward forecasting problem.

**Potential limitations:**

* Weather variables may not be included directly.
* Additional weather data may need to be integrated.
* Dataset coverage is associated with a specific electricity market/region.

---

### Candidate 2 — London Smart Meter Dataset

A large smart-meter dataset containing electricity consumption measurements from households.

**Potential strengths:**

* Large-scale smart-meter data.
* Fine-grained consumption observations.
* Real-world household electricity behavior.
* Useful for demonstrating data-engineering techniques.
* Suitable for granular forecasting experiments.

**Potential limitations:**

* More complex data structure.
* Household-level data introduces additional aggregation decisions.
* Processing requirements may be higher.
* Weather integration would require an additional data source.

---

### Candidate 3 — Open Power System Data

An open electricity-system dataset containing power-system and related energy information.

**Potential strengths:**

* Strong alignment with energy-system and sustainability analysis.
* Useful for renewable-energy analysis.
* Potentially useful for combining demand and generation information.
* Provides opportunities to extend the project toward renewable integration.

**Potential limitations:**

* Dataset structure may be more complex.
* May require additional preprocessing.
* The exact forecasting target needs to be defined carefully.
* May not provide the same straightforward load-forecasting setup as a dedicated consumption dataset.

---

## 4. Evaluation Criteria

Candidates will be evaluated using the following criteria:

| Criterion                              | Importance  |
| -------------------------------------- | ----------- |
| Electricity demand/load availability   | Critical    |
| Timestamp quality                      | Critical    |
| Historical coverage                    | High        |
| Data volume                            | High        |
| Forecasting suitability                | Critical    |
| Data documentation                     | High        |
| Public accessibility                   | Critical    |
| Reproducibility                        | High        |
| Weather integration potential          | High        |
| Sustainability relevance               | High        |
| Processing complexity                  | Medium      |
| Suitability for XGBoost                | High        |
| Suitability for future LSTM experiment | Medium/High |

---

## 5. Selection Method

The final dataset will not be selected solely on dataset size.

Each candidate will be inspected for:

* Available columns
* Timestamp frequency
* Historical date range
* Number of observations
* Missing values
* Duplicate records
* Timestamp consistency
* Geographic/operational scope
* Documentation
* Access and licensing conditions
* Compatibility with the project's forecasting objective

The selected dataset will then be documented with its source, limitations, and intended use.

---

## 6. Selected Dataset

**Status: Pending evaluation**

The final dataset will be selected after comparing the candidate datasets using the criteria above.

**Selected dataset:** London dataset and document the evidence.

**Source:** TBD

**Date selected:** TBD

---

## 7. Why Historical Data Is Used

GridWise AI requires historical observations because forecasting models learn relationships between past electricity demand, time, and environmental conditions.

Collecting a sufficiently large historical dataset from scratch would require a long period of data collection before meaningful model development could begin.

Using an established public dataset allows the project to begin with sufficient historical observations while keeping the system reproducible and cost-free.

The architecture will later support the integration of newly arriving data and external weather information.

Therefore, the project follows a hybrid development strategy:

```text
Historical Public Data
        ↓
Initial Model Development
        ↓
Validation & Evaluation
        ↓
Production-Inspired Pipeline
        ↓
New/Live Data Integration
```

---

## 8. Data Usage Strategy

The selected dataset will be organized as follows:

```text
data/
├── raw/
│   └── Original downloaded dataset
│
├── processed/
│   └── Cleaned/validated datasets
│
└── external/
    └── External weather or supporting datasets
```

### Raw Data

Raw data will remain unchanged after download.

### Processed Data

Cleaned and transformed data will be generated by reproducible pipeline code rather than manually edited.

### External Data

Weather and other supporting datasets will be stored separately from the primary energy dataset.

---

## 9. Reproducibility

The repository will contain documentation describing:

* Dataset name
* Dataset source
* Access method
* Download date
* Relevant files
* Expected schema
* Processing steps
* Known limitations

Large raw datasets will not be committed to GitHub.

The repository will instead contain the code and documentation required to reproduce the data-processing workflow.

---

## 10. Future Extension

After the initial forecasting system is validated, the project may integrate additional data sources such as:

* Temperature
* Humidity
* Wind speed
* Solar generation
* Renewable-energy availability
* Calendar/holiday information

This would allow the system to evolve from basic demand forecasting toward sustainability-oriented operational analysis.

---

## 11. Decision

**Decision: Pending**

The dataset will be selected after completing the candidate evaluation.

The selection decision will be recorded in this document and, if the decision has significant architectural consequences, may also be recorded as a separate Architecture Decision Record.
