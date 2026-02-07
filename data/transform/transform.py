import pandas as pd
import os

def cleanse(file_path, metric_name, value_column):
    df = pd.read_csv(file_path)

    df = df.drop(columns=["Lat", "Long"])

    df = df.rename(columns={
        "Province/State": "Province_State",
        "Country/Region": "Country_Region"
    })

    id_columns = ["Province_State", "Country_Region"]

    df_long = df.melt(
        id_vars=id_columns,
        var_name="date",
        value_name=value_column
    )

    df_long["metric"] = metric_name
    return df_long


def transform_data(extract_path, transform_path):
    confirmed_df = cleanse(
        os.path.join(extract_path, "time_series_covid19_confirmed_global.csv"),
        "confirmed",
        "cases"
    )

    deaths_df = cleanse(
        os.path.join(extract_path, "time_series_covid19_deaths_global.csv"),
        "deaths",
        "cases"
    )

    recovered_df = cleanse(
        os.path.join(extract_path, "time_series_covid19_recovered_global.csv"),
        "recovered",
        "cases"
    )

    final_df = pd.concat([confirmed_df, deaths_df, recovered_df])

    final_df["date"] = pd.to_datetime(final_df["date"], format="%m/%d/%y")
    final_df["cases"] = final_df["cases"].fillna(0)
    final_df = final_df.drop_duplicates()

    if (final_df["cases"] < 0).any():
        raise ValueError("Negative case values found")

    os.makedirs(transform_path, exist_ok=True)
    output_file = os.path.join(transform_path, "covid_metrics_long.csv")
    final_df.to_csv(output_file, index=False)

    return output_file
