from re import X
import pandas as pd
import plotly.express as px
from tabulate import tabulate

glovesArr = {
    1: "01/Teleporter_26_05_2022_15_28.csv",
    2: "02/Teleporter_27_05_2022_11_56.csv",
    3: "03/Teleporter_27_05_2022_12_35.csv",
    4: "04/Teleporter_30_05_2022_14_15.csv",
    5: "05/Teleporter_30_05_2022_15_03.csv",
    6: "06/Teleporter_30_05_2022_15_20.csv",
    7: "07/Teleporter_30_05_2022_15_52.csv",
    8: "08/Teleporter_30_05_2022_16_12.csv",
    9: "09/Teleporter_30_05_2022_17_11.csv",
    10: "10/Teleporter_30_05_2022_17_39.csv",
}

controllerArr = {
    1: "01/TeleporterController_26_05_2022_15_09.csv",
    2: "02/TeleporterController_27_05_2022_11_39.csv",
    3: "03/TeleporterController_27_05_2022_12_57.csv",
    4: "04/TeleporterController_30_05_2022_14_32.csv",
    5: "05/TeleporterController_30_05_2022_14_50.csv",
    6: "06/TeleporterController_30_05_2022_15_32.csv",
    7: "07/TeleporterController_30_05_2022_15_41.csv",
    8: "08/TeleporterController_30_05_2022_16_29.csv",
    9: "09/TeleporterController_30_05_2022_16_49.csv",
    10: "10/TeleporterController_30_05_2022_17_54.csv"
}

stuffGlove = {
        "x": [],
        "z": [],
        "person": [],
}
stuffContr = {
        "x": [],
        "z": [],
        "person": [],
}

def convertStringToFloatSeconds(string):
    return float(string.rstrip().replace(",", ".")) / 1000

def makeStuff(line, input, person):
    # (0.533, 0.000, -10.724)
    print("line")
    print(line)
    print("line")
    nums = line.replace(" ", "").split("(")[1].split(")")[0].split(",")

    x = float(nums[0])
    z = float(nums[2])

    if input == "Gloves":
        stuffGlove["x"].append(x)
        stuffGlove["z"].append(z)
        stuffGlove["person"].append(person)

    if input == "Controller":
        stuffContr["x"].append(x)
        stuffContr["z"].append(z)
        stuffContr["person"].append(person)


for i in range(1, 11):
    with open(glovesArr[i], encoding='UTF8') as file_in:
        lines = file_in.readlines()
        input = 'Gloves'

        for line in lines[1:]:
            makeStuff(line, input, i)

for i in range(1, 11):
    with open(controllerArr[i], encoding='UTF8') as file_in:
        lines = file_in.readlines()
        input = 'Controller'

        for line in lines[1:]:
            makeStuff(line, input, i)

fig = px.scatter(
        pd.DataFrame(data=stuffGlove),
        title="Glove",
        x="x",
        y="z",
        color='person',
        height=700,
        labels={
                 "x": "X-Coordinates",
                 "z": "Z-Coordinates",
                 "person": "Person"
            },
        color_continuous_scale=px.colors.diverging.Portland
        )
fig.show()


fig = px.scatter(
        pd.DataFrame(data=stuffContr),
        title="Controller",
        x="x",
        y="z",
        color='person',
        height=700,
        labels={
                 "x": "X-Coordinates",
                 "z": "Z-Coordinates",
                 "person": "Person"
            },
        color_continuous_scale=px.colors.diverging.Portland
        )
fig.show()