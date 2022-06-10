import enum
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import pandas as pd

arr = {
   1 : "01/Wheel_26_05_2022_15_28.csv",
   2 : "02/Wheel_27_05_2022_11_56.csv",
   3 : "03/Wheel_27_05_2022_12_35.csv",
   4 : "04/Wheel_30_05_2022_14_15.csv",
   5 : "05/Wheel_30_05_2022_15_03.csv",
   6 : "06/Wheel_30_05_2022_15_20.csv",
   7 : "07/Wheel_30_05_2022_15_52.csv",
   8 : "08/Wheel_30_05_2022_16_12.csv",
   9 : "09/Wheel_30_05_2022_17_11.csv",
   10 : "10/Wheel_30_05_2022_17_39.csv"
}


main = make_subplots()



roww=1
coll=0


distance_data= {
    "Time": [],
    "Distance": [],
    "Hand": [],
    "col": [],
    "row": []
}

def singleWheel(ind):
    global roww, coll, distance_data
    count = 0
    frames = []
    distance = []

    hand = []

    coll += 1
    if coll > 2:
        coll -= 2
        roww += 1
    # Formatting
    #   1  2
    #   3  4
    #   5  6
    #   7  8
    #   9  10

    for index, value in enumerate(wheel_data['Distance']):
        ori = ""
        if wheel_data['L/R'][index] == "L":
            ori = "Left"
        else:
            ori = "Right"

        distance_data["Time"].append(count)
        distance_data["Distance"].append(float(str(value).replace(",", ".")))
        count += 1
        distance_data["Hand"].append(ori)
        distance_data["col"].append(coll)
        distance_data["row"].append(roww)

for index, o in enumerate(arr):
    global wheel_data
    wheel_data = pd.read_csv(arr[o], sep=';')
    singleWheel(o)

print(distance_data)
lineplot = px.line(
    distance_data,
    title="Gloves",
    x='Time',
    y='Distance',
    color='Hand',
    facet_row='row',
    facet_col='col',
    labels={
        "Time": "Time",
        "Distance": "Distance",
        "Hand": "Hand",
        "row": "Row",
        "col": "Column"
    }
)

lineplot.update_layout(
    scene=dict(
        xaxis=dict(nticks=4, range=[-1, 1], ),
        yaxis=dict(nticks=4, range=[-1, 1], ))
    )

lineplot.show()