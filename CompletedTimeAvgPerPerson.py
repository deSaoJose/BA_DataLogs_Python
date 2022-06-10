import pandas as pd
import plotly.express as px
from tabulate import tabulate

glovesArr = {
    1: "01/StepTimes_26_05_2022_15_28.csv",
    2: "02/StepTimes_27_05_2022_11_56.csv",
    3: "03/StepTimes_27_05_2022_12_35.csv",
    4: "04/StepTimes_30_05_2022_14_15.csv",
    5: "05/StepTimes_30_05_2022_15_03.csv",
    6: "06/StepTimes_30_05_2022_15_20.csv",
    7: "07/StepTimes_30_05_2022_15_52.csv",
    8: "08/StepTimes_30_05_2022_16_12.csv",
    9: "09/StepTimes_30_05_2022_17_11.csv",
    10: "10/StepTimes_30_05_2022_17_39.csv",
}

controllerArr = {
    1: "01/StepTimesController_26_05_2022_15_09.csv",
    2: "02/StepTimesController_27_05_2022_11_39.csv",
    3: "03/StepTimesController_27_05_2022_12_57.csv",
    4: "04/StepTimesController_30_05_2022_14_32.csv",
    5: "05/StepTimesController_30_05_2022_14_50.csv",
    6: "06/StepTimesController_30_05_2022_15_32.csv",
    7: "07/StepTimesController_30_05_2022_15_41.csv",
    8: "08/StepTimesController_30_05_2022_16_29.csv",
    9: "09/StepTimesController_30_05_2022_16_49.csv",
    10: "10/StepTimesController_30_05_2022_17_54.csv"
}

tasks = [
    "Prüfe, ob das Fahrzeug gebremst ist.",
    "Ziehe die Feststellbremse an.",
    "Ziehe die Druckluftbremse an.",
    "Prüfe, ob das Fahrzeug nun angebremst ist.",
    "Signalisiere der Lok, dass sie anfahren darf.",
    "Warte auf die Lok",
    "Kupple den vordersten Wagen an die Lok.",
]

stuff = {
    "time": [],
    "input": [],
    "person": [],
}


def convertStringToFloatSeconds(string):
    return float(string.rstrip().replace(",", ".")) / 1000 / 60


def makeStuff(lines, i, person):
    stuff["input"].append(i)
    stuff["person"].append("Proband " + str(person))
    stuff["time"].append(convertStringToFloatSeconds(lines[1].split(";")[1]))

    stuff["input"].append(i)
    stuff["person"].append("Proband " + str(person))
    stuff["time"].append(convertStringToFloatSeconds(lines[3].split(";")[1]))

    stuff["input"].append(i)
    stuff["person"].append("Proband " + str(person))
    stuff["time"].append(convertStringToFloatSeconds(lines[5].split(";")[1]))

    stuff["input"].append(i)
    stuff["person"].append("Proband " + str(person))
    stuff["time"].append(convertStringToFloatSeconds(lines[7].split(";")[1]))

    stuff["input"].append(i)
    stuff["person"].append("Proband " + str(person))
    stuff["time"].append(convertStringToFloatSeconds(lines[10].split(";")[1]))

    stuff["input"].append(i)
    stuff["person"].append("Proband " + str(person))
    stuff["time"].append(convertStringToFloatSeconds(lines[11].split(";")[1]))

    stuff["input"].append(i)
    stuff["person"].append("Proband " + str(person))
    stuff["time"].append(convertStringToFloatSeconds(lines[12].split(";")[1]))


for i in range(1, 11):
    with open(glovesArr[i], encoding='UTF8') as file_in:
        lines = file_in.readlines()
        input = 'Gloves'
        makeStuff(lines, input, i)

for i in range(1, 11):
    with open(controllerArr[i], encoding='UTF8') as file_in:
        lines = file_in.readlines()
        input = 'Controller'
        makeStuff(lines, input, i)

""" print("Done Data")
for i, o in enumerate(stuff["input"]):
    print(stuff["input"][i])
    print(stuff["task"][i])
    print(stuff["time"][i])
    print()
print(len(stuff["input"]))
print(len(stuff["task"]))
print(len(stuff["time"])) """

print(tabulate(stuff))
fig = px.histogram(
    pd.DataFrame(data=stuff),
    title="Time needed per Person",
    x="person",
    y="time",
    color='input',
    barmode='group',
    height=700,
    # range_y=[0, 5],
    histfunc='sum',
    labels={
        "person": "Proband",
        "time": "Time [Minutes]",
        "input": "Input (Controller/Gloves)"
    },
    text_auto=True,
)
print("Done fig")
fig.show()
print("Done show fig")
print("---------------------")
print()

sumC = 0
sumG = 0
for i, o in enumerate(stuff["input"]):
    if o == "Gloves":
        sumG += stuff["time"][i]
    if o == "Controller":
        sumC += stuff["time"][i]

print("Average Gloves: " + str(sumG / 10) + " Minutes")
print("Average Controller: " + str(sumC / 10) + " Minutes")