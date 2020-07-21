import pandas as pd
import numpy as np
import datetime
import matplotlib as plt
from pandas import DataFrame


result = pd.read_csv("http://www.agridata.tn/dataset/082abfac-7a9f-4e27-90c7-1621172737c4/resource/e93a4205-84de-47a5"

                     "-bcdb-e00520b15e10/download/pluviometrie.csv")

result['year'] = pd.DatetimeIndex(result['Date']).year

print("1/gold day\n2/gold day in year\n3/stats (top5 + other)")

user_input = input("Answer: ")

if user_input == "1":
    golden_wileya = result.groupby(['Pluvio_du_jour', 'station'])['Date']

    print(max(golden_wileya))

elif user_input == "2":

    nums = [val for val in range(len(result['year'].unique()))]

    choices = list(zip(nums, result['year'].unique()))

    print("Select the '%s' of research\n" % "year")

    for v in choices:
        print("%s.  %s" % v)

    user_input = input("Answer: ")

    filtered_makes = result.loc[result["year"] == int(user_input)]

    print(filtered_makes[["Pluvio_du_jour", "station"]].max())

else:
    summury = pd.DataFrame(result.groupby(['year', "station"]).mean().astype('int')["Pluvio_du_jour"])
    summary['total_pluie'] = result.groupby('year').Pluvio_du_jour.sum()
    summary["total_pluie"].plot()

#firas_miladi