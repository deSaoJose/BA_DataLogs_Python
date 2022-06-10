from traceback import print_tb
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import pandas as pd


wheelGloves = {
    1 :  "01/Wheel_26_05_2022_15_28.csv",
    2 :  "02/Wheel_27_05_2022_11_56.csv",
    3 :  "03/Wheel_27_05_2022_12_35.csv",
    4 :  "04/Wheel_30_05_2022_14_15.csv",
    5 :  "05/Wheel_30_05_2022_15_03.csv",
    6 :  "06/Wheel_30_05_2022_15_20.csv",
    7 :  "07/Wheel_30_05_2022_15_52.csv",
    8 :  "08/Wheel_30_05_2022_16_12.csv",
    9 :  "09/Wheel_30_05_2022_17_11.csv",
    10 : "10/Wheel_30_05_2022_17_39.csv"
}


wheelController = {
    1 : "01/WheelController_26_05_2022_15_09.csv",
    2 : "02/WheelController_27_05_2022_11_39.csv",
    3 : "03/WheelController_27_05_2022_12_57.csv",
    4 : "04/WheelController_30_05_2022_14_32.csv",
    5 : "05/WheelController_30_05_2022_14_50.csv",
    6 : "06/WheelController_30_05_2022_15_32.csv",
    7 : "07/WheelController_30_05_2022_15_41.csv",
    8 : "08/WheelController_30_05_2022_16_29.csv",
    9 : "09/WheelController_30_05_2022_16_49.csv",
    10 : "10/WheelController_30_05_2022_17_54.csv"
}

for i in range(1, 11):
    wheel_data = pd.read_csv(wheelGloves[i], sep=';')

    # ------------------- Position Data -------------------
    x_data_pos_l = []
    y_data_pos_l = []
    z_data_pos_l = []
    time_l = []
    counter_l = 0
    x_data_pos_r = []
    y_data_pos_r = []
    z_data_pos_r = []
    time_r = []
    counter_r = 0

    for index, value in enumerate(wheel_data['Position Real']):
        cleaned_values = value.replace('(', '').replace(')', '').split(', ')
        if wheel_data['L/R'][index] == "L":
            x_data_pos_l.append(float(cleaned_values[0]))
            y_data_pos_l.append(float(cleaned_values[1]))
            z_data_pos_l.append(float(cleaned_values[2]))
            time_l.append(counter_l)
            counter_l += 1
        else:
            x_data_pos_r.append(float(cleaned_values[0]))
            y_data_pos_r.append(float(cleaned_values[1]))
            z_data_pos_r.append(float(cleaned_values[2]))
            time_r.append(counter_r)
            counter_r += 1

    # --------------------- u v w ---------------------------------
    u_data_l = []
    v_data_l = []
    w_data_l = []

    u_data_r = []
    v_data_r = []
    w_data_r = []

    for index, value in enumerate(wheel_data['Rotation Real Normalized']):
        cleaned_values = value.replace('(', '').replace(')', '').split(', ')
        if wheel_data['L/R'][index] == "L":
            u_data_l.append(float(cleaned_values[0]))
            v_data_l.append(float(cleaned_values[1]))
            w_data_l.append(float(cleaned_values[2]))
        else:
            u_data_r.append(float(cleaned_values[0]))
            v_data_r.append(float(cleaned_values[1]))
            w_data_r.append(float(cleaned_values[2]))

    print("-----------------------")
    print(len(x_data_pos_l))
    print(len(y_data_pos_l))
    print(len(z_data_pos_l))
    print(len(u_data_l))
    print(len(v_data_l))
    print(len(w_data_l))
    print("-----------------------")

    posRot_data_l = pd.DataFrame(dict(
        PosX=x_data_pos_l,
        PosY=y_data_pos_l,
        PosZ=z_data_pos_l,
        U=u_data_l,
        V=v_data_l,
        W=w_data_l
    ))

    posRot_data_r = pd.DataFrame(dict(
        PosX=x_data_pos_r,
        PosY=y_data_pos_r,
        PosZ=z_data_pos_r,
        U=u_data_r,
        V=v_data_r,
        W=w_data_r
    ))


    fig = go.Figure(
            data = go.Cone(
            x=posRot_data_l['PosX'],
            y=posRot_data_l['PosY'],
            z=posRot_data_l['PosZ'],
            u=posRot_data_l['U'],
            v=posRot_data_l['V'],
            w=posRot_data_l['W'],
            colorscale='Teal',
            colorbar=dict(thickness=20, x=1),
            sizemode="scaled",
            sizeref=40)
        )

    fig.add_cone(x=posRot_data_r['PosX'],
            y=posRot_data_r['PosY'],
            z=posRot_data_r['PosZ'],
            u=posRot_data_r['U'],
            v=posRot_data_r['V'],
            w=posRot_data_r['W'],
            colorscale='Peach',
            colorbar=dict(thickness=20, x=1.1),
            sizemode="scaled",
            sizeref=40
        )

    fig.update_layout(scene=dict(aspectratio=dict(x=1, y=1, z=0.8),
                                 camera_eye=dict(x=1.2, y=1.2, z=0.6)))

    fig.show()

