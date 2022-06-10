from draw import drawFullLengthBar, drawGroupBarChart, drawStandardBarChart

FILE_NAME = 'FragebogenData.CSV'

# Used for CSV Index to Graph Index Convertion for a Question Table
COLUMN_DICTIONARY = {
    # index, graph_index
    3: 1,
    4: 2,
    7: 1,
    8: 2,
    9: 3,
    10: 4,
    11: 5,
    12: 6,
    13: 7,
    14: 8,
    15: 9,
    16: 10,
    17: 11,
    20: 1,
    21: 2,
    22: 3,
    23: 4,
    24: 5,
    25: 6,
    26: 7,
    27: 8,
    28: 9,
    29: 10,
    30: 11,
    33: 1,
    34: 2,
    35: 3,
    36: 4,
    37: 5,
    38: 6,
    39: 7,
}

lines = []


def readFile():
    global lines
    with open(FILE_NAME, encoding='UTF8') as file_in:
        lines = file_in.readlines()
        evaluteContent()


def evaluteContent():
    for line in lines:
        parts = line.split(';')
        for index, column in enumerate(parts):
            if (column == '' or (column == "9" and parts[0] != "9")) and index not in [6, 31, 40, 41]:
                print("!!!Unknown Wrong Column[%d] at person %s!!!" % (index, parts[0]))
        if len(parts) != 42:
            print('!!!Wrong Column[%d] Count at person %s!!!' % (index, parts[0]))


def groupBarChart():
    obj = {
        "skala": [],
        "input": [],
        "question": [],
    }
    for line in lines[1:]:  # [1:] list without index 0
        parts = line.split(';')

        for index in range(7, 18):
            obj["skala"].append(parts[index])
            obj["input"].append("Gloves")
            obj["question"].append("Question " + str(COLUMN_DICTIONARY[index]))

        for index in range(20, 31):
            obj["skala"].append(parts[index])
            obj["input"].append("Controller")
            obj["question"].append("Question " + str(COLUMN_DICTIONARY[index]))

    drawGroupBarChart(obj)


def barChart(start, end):
    obj = {
        "skala": [],
        "question": [],
    }
    for line in lines[1:]:  # [1:] list without index 0
        parts = line.split(';')
        for index in range(start, end):
            obj["skala"].append(parts[index])
            obj["question"].append("Question " + str(COLUMN_DICTIONARY[index]))
    drawStandardBarChart(obj, range=[0, 5])


def fullLengthBarChart():
    obj = {
        "skala": [],
        "question": [],
        "input": [],
    }
    for line in lines[1:]:  # [1:] list without index 0
        parts = line.split(';')
        for index in range(33, 40):
            # x : C : G
            # 1 : 6 : 1
            # 2 : 5 : 2
            # 3 : 4 : 3
            # 4 : 3 : 4
            # 5 : 2 : 5
            # 6 : 1 : 6

            # x : C : G
            # 1 : 5 : 0
            # 2 : 4 : 1
            # 3 : 3 : 2
            # 4 : 2 : 3
            # 5 : 1 : 4
            # 6 : 0 : 5

            obj["skala"].append(6 - float(parts[index]))
            obj["question"].append(COLUMN_DICTIONARY[index])
            obj["input"].append("Controller")

            obj["skala"].append(float(parts[index]) - 1)
            obj["question"].append(COLUMN_DICTIONARY[index])
            obj["input"].append("Gloves")

    print(obj)

    newObj = {
        "skala": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        "question": [
            "Question " + str(COLUMN_DICTIONARY[33]),
            "Question " + str(COLUMN_DICTIONARY[34]),
            "Question " + str(COLUMN_DICTIONARY[35]),
            "Question " + str(COLUMN_DICTIONARY[36]),
            "Question " + str(COLUMN_DICTIONARY[37]),
            "Question " + str(COLUMN_DICTIONARY[38]),
            "Question " + str(COLUMN_DICTIONARY[39]),
            "Question " + str(COLUMN_DICTIONARY[33]),
            "Question " + str(COLUMN_DICTIONARY[34]),
            "Question " + str(COLUMN_DICTIONARY[35]),
            "Question " + str(COLUMN_DICTIONARY[36]),
            "Question " + str(COLUMN_DICTIONARY[37]),
            "Question " + str(COLUMN_DICTIONARY[38]),
            "Question " + str(COLUMN_DICTIONARY[39]),
        ],
        "input": ["Controller", "Controller", "Controller", "Controller", "Controller", "Controller", "Controller",
                  "Gloves", "Gloves", "Gloves", "Gloves", "Gloves", "Gloves", "Gloves"],
    }

    for index, o in enumerate(obj["skala"]):
        if obj["input"][index] == "Controller":
            newObj["skala"][int(obj["question"][index]) - 1] = newObj["skala"][int(obj["question"][index]) - 1] + float(
                o)
        if obj["input"][index] == "Gloves":
            newObj["skala"][int(obj["question"][index]) - 1 + 7] = newObj["skala"][
                                                                       int(obj["question"][index]) - 1 + 7] + float(o)

    newObj["skala"].reverse()
    newObj["question"].reverse()
    newObj["input"].reverse()

    print(newObj)
    drawFullLengthBar(newObj)


def execute():
    readFile()

    groupBarChart()
    barChart(3, 5)
    fullLengthBarChart()


if __name__ == '__main__':
    execute()