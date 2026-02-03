import os
import io
import requests
import pandas as pd


def extract_data():
    urls = {
    "confirmed": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
    "deaths": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
    "recovered": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
    }
    folder_path = os.getcwd()
    path = os.path.join(folder_path,"data","extract")

    os.makedirs(path, exist_ok=True)

    for name, url in urls.items():
        r = requests.get(url)
        r.encoding = "utf-8"
        if r.status_code == 200:
            file_path= os.path.join(path, f"time_series_covid19_{name}_global.csv")
            with open(file_path, "w", encoding="utf-8") as f:
             f.write(r.text)                    
            print(f"saved: {file_path}")
        else:
            print(f"error")
extract_data()            