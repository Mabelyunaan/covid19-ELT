import os
import pandas as pd
def extract_data():
    urls = {
    "confirmed": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
    "deaths": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
    "recovered": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
    }
    base_dir =os.path.dirname(os.path.abspath(__file__))
    extract_path = os.path.join( base_dir)
    os.makedirs(extract_path, exist_ok=True)

    for name, url in urls.items():
        try:
            df= pd.read_csv(url)
            file_path= os.path.join(extract_path, f"time_series_covid19_{name}_global.csv")
            df.to_csv(file_path, index="False")
        except Exception as e:
            print(f"error, failed to extract {name}: {e}")
        
extract_data()            