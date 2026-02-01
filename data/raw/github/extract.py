import os
import io
import requests
import pandas as pd

urls = {
    "confirmed": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
    "deaths": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
    "recovered": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
}
folder_path = os.getcwd()
path = os.path.join(folder_path,"data","raw","github")

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
              
          
















#         df =pd.read_csv(io.StringIO(url.text))
#     print(df)    
# #check status
#     print (f"statust code:{url.status_code}")

# if r1.status_code == 200:
#     df = pd.read_csv(io.StringIO(r1.text))
#     print(df.head())
# else:
#     print("unable to fetch data")    


# r2= requests.get(global_death)
# r2.encoding = "utf-8"
# #check status
# print (f"statust code:{r2.status_code}")

# if r2.status_code == 200:
#     df = pd.read_csv(io.StringIO(r2.text))
#     print(df.head())
# else:
#     print("unable to fetch data")    

# r3= requests.get(global_recovery)
# r3.encoding = "utf-8"
# #check status
# print (f"statust code:{r3.status_code}")

# if r3.status_code == 200:
#     df = pd.read_csv(io.StringIO(r3.text))
#     print(df.head())
# else:
#     print("unable to fetch data")            

# print (os.getcwd())    

