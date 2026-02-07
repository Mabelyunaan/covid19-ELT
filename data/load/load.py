import os
import pandas as pd
from sqlalchemy import create_engine


def load_data(csv_path):
    engine = create_engine(
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    df = pd.read_csv(csv_path)

    df.columns = [c.lower() for c in df.columns]

    dim_location = (
        df[["province_state", "country_region"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim_location["location_id"] = dim_location.index + 1

    dim_location.to_sql(
        "dim_location",
        engine,
        if_exists="append",
        index=False
    )

    fact_df = df.merge(
        dim_location,
        on=["province_state", "country_region"],
        how="left"
    )

    fact_df = fact_df[["date", "location_id", "metric", "cases"]]
    fact_df["date"] = pd.to_datetime(fact_df["date"]).dt.date

    fact_df.to_sql(
        "fact_covid_cases",
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    return {
        "dim_location_rows": len(dim_location),
        "fact_rows": len(fact_df),
    }
