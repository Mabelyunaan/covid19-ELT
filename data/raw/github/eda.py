import pandas as pd  
import os     

                 #cleaning
def cleanse(file_path ,metric_name,value_column):
    df = pd.read_csv(file_path)
    df= df.drop(columns=['Lat', 'Long'])#dropping unused columns

    df=df.rename(columns={
    'Province/State' :'Province_State',
    'Country/Region' :'Country_Region'
    })

    id_columns = ['Province_State', 'Country_Region']
    df_long = df.melt(
        id_vars=id_columns,
        var_name="date",
        value_name=value_column
    )
    df_long["metric"]= metric_name
    return df_long

confirmed_df = cleanse(
    file_path="data/raw/github/time_series_covid19_confirmed_global.csv",
    metric_name="confirmed",
    value_column="cases"
)

deaths_df = cleanse(
    file_path="data/raw/github/time_series_covid19_deaths_global.csv",
    metric_name="deaths",
    value_column="cases"
)
recovered_df = cleanse(
    file_path="data/raw/github/time_series_covid19_recovered_global.csv",
    metric_name="recovered",
    value_column="cases"
)
final_df = pd.concat([confirmed_df, deaths_df, recovered_df])

# print(final_df.dtypes)

final_df["date"]=pd.to_datetime(final_df["date"], format="%m/%d/%y")
final_df.isna().sum()
final_df["cases"] = final_df["cases"].fillna(0)
final_df.duplicated().sum()
final_df = final_df.drop_duplicates()
 #sanity checks cause cases should never be negative
(final_df["cases"] < 0).sum()

#standardizing locations
final_df["Country_Region"].sort_values().unique()


import os

processed = os.path.join(os.getcwd(), "data", "processed")
os.makedirs(processed, exist_ok=True)

file_path = os.path.join(processed, "covid_metrics_long.csv")

final_df.to_csv(
    file_path,
    index=False
)

print(f"Saved processed data to: {file_path}")
