import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    coffee_in_ml = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))

    return {"x" : coffee_in_ml, "y": hours_of_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between coffee in ml vs hours slept :-  \n--->",correlation[0,1])

def setup():
    data_path  = "py2/data/coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

    with open("py2/data/coffee vs hours of sleep.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()


setup()