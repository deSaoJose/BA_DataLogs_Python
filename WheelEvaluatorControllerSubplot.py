import enum
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import pandas as pd

wheelGlove = {
    1: "01/Wheel_26_05_2022_15_28.csv",
    2: "02/Wheel_27_05_2022_11_56.csv",
    3: "03/Wheel_27_05_2022_12_35.csv",
    4: "04/Wheel_30_05_2022_14_15.csv",
    5: "05/Wheel_30_05_2022_15_03.csv",
    6: "06/Wheel_30_05_2022_15_20.csv",
    7: "07/Wheel_30_05_2022_15_52.csv",
    8: "08/Wheel_30_05_2022_16_12.csv",
    9: "09/Wheel_30_05_2022_17_11.csv",
    10: "10/Wheel_30_05_2022_17_39.csv"
}

wheelController = {
    1: "01/WheelController_26_05_2022_15_09.csv",
    2: "02/WheelController_27_05_2022_11_39.csv",
    3: "03/WheelController_27_05_2022_12_57.csv",
    4: "04/WheelController_30_05_2022_14_32.csv",
    5: "05/WheelController_30_05_2022_14_50.csv",
    6: "06/WheelController_30_05_2022_15_32.csv",
    7: "07/WheelController_30_05_2022_15_41.csv",
    8: "08/WheelController_30_05_2022_16_29.csv",
    9: "09/WheelController_30_05_2022_16_49.csv",
    10: "10/WheelController_30_05_2022_17_54.csv"
}

figMain = make_subplots(
    rows=2, cols=5,
    specs=[
        [{'type': 'scatter3d'}, {'type': 'scatter3d'}, {'type': 'scatter3d'}, {'type': 'scatter3d'},
         {'type': 'scatter3d'}],
        [{'type': 'scatter3d'}, {'type': 'scatter3d'}, {'type': 'scatter3d'}, {'type': 'scatter3d'},
         {'type': 'scatter3d'}]
    ])

row = 1
col = 1
for i in range(1, 11):
    wheel_data = pd.read_csv(wheelController[i], sep=';')  ################# CHANGE wheelController <-> wheelGlove

    # ------------------- Position Data -------------------
    x_data_pos_r = []
    y_data_pos_r = []
    z_data_pos_r = []
    x_data_pos_l = []
    y_data_pos_l = []
    z_data_pos_l = []
    hand = []
    time_l = []
    counter_l = 0
    time_r = []
    counter_r = 0
    time_v = []
    counter_v = 0

    for index, value in enumerate(wheel_data['Position Real']):
        cleaned_values = value.replace('(', '').replace(')', '').split(', ')
        if wheel_data['L/R'][index] == "L":
            x_data_pos_l.append(float(cleaned_values[0]))
            y_data_pos_l.append(float(cleaned_values[1]))
            z_data_pos_l.append(float(cleaned_values[2]))
            time_l.append(counter_l)
            counter_l += 1
        if wheel_data['L/R'][index] == "R":
            x_data_pos_r.append(float(cleaned_values[0]))
            y_data_pos_r.append(float(cleaned_values[1]))
            z_data_pos_r.append(float(cleaned_values[2]))
            time_r.append(counter_r)
            counter_r += 1
        time_v.append(counter_v)
        counter_v += 1

    x_data_pos_virtual_r = []
    y_data_pos_virtual_r = []
    z_data_pos_virtual_r = []
    x_data_pos_virtual_l = []
    y_data_pos_virtual_l = []
    z_data_pos_virtual_l = []
    hand_virtual = []
    #
    #    for index, value in enumerate(wheel_data['Position Virtual']):
    #        cleaned_values = value.replace('(', '').replace(')', '').split(', ')
    #        if wheel_data['L/R'][index] == "L":
    #            x_data_pos_virtual_l.append(float(cleaned_values[0]))
    #            y_data_pos_virtual_l.append(float(cleaned_values[1]))
    #            z_data_pos_virtual_l.append(float(cleaned_values[2]))
    #        if wheel_data['L/R'][index] == "R":
    #            x_data_pos_virtual_r.append(float(cleaned_values[0]))
    #            y_data_pos_virtual_r.append(float(cleaned_values[1]))
    #            z_data_pos_virtual_r.append(float(cleaned_values[2]))
    #        hand_virtual.append(wheel_data['L/R'][index])

    # --------------------- u v w ---------------------------------
    u_data = []
    v_data = []
    w_data = []

    for value in wheel_data['Rotation Real Normalized']:
        cleaned_values = value.replace('(', '').replace(')', '').split(', ')
        u_data.append(float(cleaned_values[0]))
        v_data.append(float(cleaned_values[1]))
        w_data.append(float(cleaned_values[2]))

    u_data_virtual = []
    v_data_virtual = []
    w_data_virtual = []

    #    for value in wheel_data['Rotation Virtual Normalized']:
    #        cleaned_values = value.replace('(', '').replace(')', '').split(', ')
    #        u_data_virtual.append(float(cleaned_values[0]))
    #        v_data_virtual.append(float(cleaned_values[1]))
    #        w_data_virtual.append(float(cleaned_values[2]))

    count = 0
    frames = []
    distance = []

    #    for value in wheel_data['Distance']:
    #        frames.append(count)
    #        distance.append(value)
    #        count += 1

    #    distance_data = pd.DataFrame(dict(
    #        Time=frames,
    #        Distance=distance
    #    ))

    fig = go.Figure(data=[go.Scatter3d(x=x_data_pos_l, y=y_data_pos_l, z=z_data_pos_l,
                                       mode='markers',
                                       marker=dict(color=time_l, colorscale='algae', colorbar=dict(thickness=20)))])

    fig.add_scatter3d(x=x_data_pos_r, y=y_data_pos_r, z=z_data_pos_r,
                      mode='markers', marker=dict(color=time_r, colorscale='Teal', colorbar=dict(thickness=20, x=1.1)))

    #    fig.add_scatter3d(x=x_data_pos_virtual_l, y=y_data_pos_virtual_l, z=z_data_pos_virtual_l,
    #                    mode='markers', marker=dict(color=time_l, colorscale='Magenta', colorbar=dict(thickness=20, x=1.2)))
    #    fig.add_scatter3d(x=x_data_pos_virtual_r, y=y_data_pos_virtual_r, z=z_data_pos_virtual_r,
    #                    mode='markers', marker=dict(color=time_r, colorscale='Peach', colorbar=dict(thickness=20, x=1.3)))

    fig.update_layout(template="plotly_dark")

    # fig.show()
    figMain.add_trace(go.Scatter3d(x=x_data_pos_l, y=y_data_pos_l, z=z_data_pos_l,
                                   mode='markers',
                                   marker=dict(color=time_l, colorscale='algae', colorbar=dict(thickness=20))), row=row,
                      col=col)
    figMain.add_trace(go.Scatter3d(x=x_data_pos_r, y=y_data_pos_r, z=z_data_pos_r,
                                   mode='markers',
                                   marker=dict(color=time_r, colorscale='Teal', colorbar=dict(thickness=20, x=1.1))),
                      row=row, col=col)
    #    figMain.add_trace(go.Scatter3d(x=x_data_pos_virtual_l, y=y_data_pos_virtual_l, z=z_data_pos_virtual_l,
    #                    mode='markers', marker=dict(color=time_l, colorscale='Magenta', colorbar=dict(thickness=20, x=1.2))), row=row, col=col)
    #    figMain.add_trace(go.Scatter3d(x=x_data_pos_virtual_r, y=y_data_pos_virtual_r, z=z_data_pos_virtual_r,
    #                    mode='markers', marker=dict(color=time_r, colorscale='Peach', colorbar=dict(thickness=20, x=1.3))), row=row, col=col)

    col += 1
    if col == 6:
        col = 1
        row += 1

figMain.show()
