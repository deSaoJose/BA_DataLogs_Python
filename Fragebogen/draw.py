import pandas as pd
import plotly.express as px

def drawGroupBarChart(data):
    fig = px.histogram(
            pd.DataFrame(data=data),
            x="question",
            y="skala",
            color='input',
            barmode='group',
            height=700,
            range_y=[0, 5],
            histfunc='avg',
            labels={
                     "question": "Questions",
                     "skala": "Answers",
                     "input": "Input (Controller/Gloves)"
                },
            text_auto=True,
            )
    fig.show()

def drawStandardBarChart(data, range):
    fig = px.histogram(
            pd.DataFrame(data=data),
            x="question",
            y="skala",
            range_y=range,
            height=700,
            histfunc='avg',
            labels={
                     "question": "Questions",
                     "skala": "Answers"
                },
            text_auto=True)
    fig.show()

def drawFullLengthBar(data):
    fig = px.bar(
            pd.DataFrame(data=data),
            x="skala",
            y="question",
            range_x=[0, 50],
            orientation='h',
            height=700,
            labels={
                     "question": "Question",
                     "skala": "Input<br>Gloves / Controller"
                },
        )
    fig.update_traces(marker_line_color='rgb(0, 0, 0)',
                  marker_line_width=5)
    fig.show()