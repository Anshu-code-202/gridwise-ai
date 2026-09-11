import duckdb

RAW_PATH = "data/raw/development/LCL-June2015v2_0.csv"

con = duckdb.connect()

result = con.execute(f"""
    SELECT COUNT(*) AS total_rows
    FROM read_csv_auto('{RAW_PATH}')


""").fetchone()


print(f"Raw rows: {result[0]}")

result = con.execute(f"""
    SELECT
        LCLid,
        DateTime,

        TRIM("KWH/hh (per half hour)")AS consumption,
  
    FROM read_csv_auto('{RAW_PATH}')
    WHERE TRIM("KWH/hh (per half hour)") = 'Null'
        
    ORDER BY DateTime
    """).fetchdf()

print(result)

result = con.execute(f"""
    SELECT
        COUNT(*) AS total_rows,
        SUM(
            CASE
                WHEN TRIM("KWH/hh (per half hour)") = 'Null'
                THEN 1
                ELSE 0
            END
        ) AS literal_null_rows
    FROM read_csv_auto('{RAW_PATH}')
""").fetchone()

print(f"Total rows: {result[0]}")
print(f"Literal Null rows: {result[1]}")
print(f"Null percentage: {(result[1] / result[0]) * 100:.4f}%")


# “Can every consumption value now be safely transformed into either a number or SQL NULL?”
result = con.execute(f"""
    SELECT
        LCLid,
        stdorToU,
        DateTime,
        CASE
            WHEN TRIM("KWH/hh (per half hour)") = 'Null'
                THEN NULL
            ELSE CAST(TRIM("KWH/hh (per half hour)") AS DOUBLE)
        END AS consumption_kwh
    FROM read_csv_auto('{RAW_PATH}')
""").fetchone()

print(f"Total rows: {result[0]}")
print(f"Numeric rows: {result[1]}")
print(f"SQL NULL rows: {result[2]}")

# ETL transformation's lidation

# Raw text consumption → numeric DOUBLE / SQL NULL
result = con.execute(f"""
    SELECT
        COUNT(*) AS total_rows,
        COUNT(consumption_kwh) AS numeric_rows,
        COUNT(*) - COUNT(consumption_kwh) AS null_rows
    FROM (
        SELECT
            CASE
                WHEN TRIM("KWH/hh (per half hour)") = 'Null'
                    THEN NULL
                ELSE CAST(TRIM("KWH/hh (per half hour)") AS DOUBLE)
            END AS consumption_kwh
        FROM read_csv_auto('{RAW_PATH}')
    )
""").fetchone()

print(f"Total rows: {result[0]}")
print(f"Numeric rows: {result[1]}")
print(f"SQL NULL rows: {result[2]}")


# op:get that, we'll have officially validated:

# 1,000,000 raw → 999,971 valid numeric → 29 missing consumption values.


result = con.execute(f"""
    SELECT
        COUNT(*) AS raw_rows,
        COUNT(DISTINCT (LCLid, DateTime)) AS unique_observations,
        COUNT(*) - COUNT(DISTINCT (LCLid, DateTime)) AS duplicate_rows
    FROM read_csv_auto('{RAW_PATH}')
""").fetchone()

print(f"Raw rows: {result[0]}")
print(f"Unique observations: {result[1]}")
print(f"Duplicate rows: {result[2]}")
# Duplicate validation is confirmed.
# Deduplicate identical observations using the complete record, while treating (LCLid, DateTime) as the observation key. Conflicting records are not silently discarded.

result = con.execute(f"""
    SELECT COUNT(*) AS cleaned_rows
    FROM (
        SELECT DISTINCT
            LCLid,
            stdorToU,
            DateTime,
            CAST(
                NULLIF(TRIM("KWH/hh (per half hour)"), 'Null')
                AS DOUBLE
            ) AS consumption_kwh
        FROM read_csv_auto('{RAW_PATH}')
        WHERE NULLIF(TRIM("KWH/hh (per half hour)"), 'Null') IS NOT NULL
    )
""").fetchone()

print(f"Cleaned rows: {result[0]}")




con.execute(f"""
    COPY (
        SELECT DISTINCT
            LCLid,
            stdorToU,
            DateTime,
            CAST(
                NULLIF(TRIM("KWH/hh (per half hour)"), 'Null')
                AS DOUBLE
            ) AS consumption_kwh
        FROM read_csv_auto('{RAW_PATH}')
        WHERE NULLIF(TRIM("KWH/hh (per half hour)"), 'Null') IS NOT NULL
    )
    TO 'data/processed/lcl_cleaned.parquet'
    (FORMAT PARQUET)
""")


result=con.execute(f"""
    SELECT COUNT(*)
    FROM read_parquet('data/processed/lcl_cleaned.parquet')

""").fetchone()
print(f"processed rows :{result[0]}")