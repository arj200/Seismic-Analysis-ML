import PySimpleGUI as sg
import numpy as np
from joblib import load

# Load Trained MLP Model and Scaler
mlp_model = load("MLP_Trained_Model.pkl")
scaler = load("scaler.pkl")

# Set GUI Theme
sg.theme('SystemDefault')

# GUI Styling
b_inp1 = {'font': ('Times New Roman', 12)}
b_inp2 = {'size': (26, 1), 'font': ('Times New Roman', 11)}
b_inp3 = {'size': (15, 1), 'font': ('Times New Roman', 11)}
b_inp4 = {'font': ('Times New Roman', 12)}

# GUI Layout
layout = [
    [sg.Text('Developed by Arjun T P', **b_inp1)],
    [sg.Frame(layout=[
        [sg.Text('Peak Ground Acceleration (g)', **b_inp2), sg.InputText(key='-f1-', **b_inp3),
         sg.Text('Spectral Acceleration at 1s (g)', **b_inp2), sg.InputText(key='-f7-', **b_inp3)],
        [sg.Text('Peak Ground Velocity (cm/s)', **b_inp2), sg.InputText(key='-f2-', **b_inp3),
         sg.Text('Spectral Acceleration at 2s (g)', **b_inp2), sg.InputText(key='-f8-', **b_inp3)],
        [sg.Text('Peak Ground Displacement (cm)', **b_inp2), sg.InputText(key='-f3-', **b_inp3),
         sg.Text('Spectral Acceleration at 3s (g)', **b_inp2), sg.InputText(key='-f9-', **b_inp3)],
        [sg.Text('Significant Duration (s)', **b_inp2), sg.InputText(key='-f4-', **b_inp3),
         sg.Text('Spectral Acceleration at 4s (g)', **b_inp2), sg.InputText(key='-f10-', **b_inp3)],
        [sg.Text('Arias Intensity (m/s)', **b_inp2), sg.InputText(key='-f5-', **b_inp3),
         sg.Text('Spectral Acceleration at 5s (g)', **b_inp2), sg.InputText(key='-f11-', **b_inp3)],
        [sg.Text('Mean Period (s)', **b_inp2), sg.InputText(key='-f6-', **b_inp3),
         sg.Text('Height of Building (m)', **b_inp2), sg.InputText(key='-f14-', **b_inp3)],
        [sg.Text('Magnitude', **b_inp2), sg.InputText(key='-f12-', **b_inp3),
         sg.Text('Span (m)', **b_inp2), sg.InputText(key='-f15-', **b_inp3)],
        [sg.Text('Radius of rupture (km)', **b_inp2), sg.InputText(key='-f13-', **b_inp3),
         sg.Text('Total BRB area in one frame (sq.cm)', **b_inp2), sg.InputText(key='-f16-', **b_inp3)]
    ], title='Input Parameters', **b_inp4)],

    [sg.Frame(layout=[
        [sg.Text('IDR (%)', **b_inp2), sg.InputText(key='-OP1-', **b_inp3, readonly=True),
         sg.Text('Maximum Ductility Demand', **b_inp2), sg.InputText(key='-OP3-', **b_inp3, readonly=True)],
        [sg.Text('RDR (%)', **b_inp2), sg.InputText(key='-OP2-', **b_inp3, readonly=True),
         sg.Text('Cumulative Ductility Demand', **b_inp2), sg.InputText(key='-OP4-', **b_inp3, readonly=True)]
    ], title='Engineering Demand Parameters (EDPs)', **b_inp4)],

    [sg.Button('Predict'), sg.Button('Cancel')]
]

# Create the Window
window = sg.Window('Estimation of EDPs of Buckling Restrained Braced Frames', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	
        break

    if event == 'Predict':
        try:
            # Get Inputs
            input_values = [
                float(values['-f1-']), float(values['-f2-']), float(values['-f3-']),
                float(values['-f4-']), float(values['-f5-']), float(values['-f6-']),
                float(values['-f7-']), float(values['-f8-']), float(values['-f9-']),
                float(values['-f10-']), float(values['-f11-']), float(values['-f12-']),
                float(values['-f13-']), float(values['-f14-']), float(values['-f15-']),
                float(values['-f16-'])
            ]
            x_test = np.array([input_values]).astype(float)

            # Apply Feature Scaling
            x_test_scaled = scaler.transform(x_test)

            # Predict using MLP Model
            prediction = mlp_model.predict(x_test_scaled)
            IDR, RDR, MaxDuc, CumDuc = prediction[0]

            # Update GUI Output
            window['-OP1-'].update(f'{IDR:.3f}')
            window['-OP2-'].update(f'{RDR:.3f}')
            window['-OP3-'].update(f'{MaxDuc:.3f}')
            window['-OP4-'].update(f'{CumDuc:.3f}')

        except Exception as e:
            sg.popup_error(f"Error: {str(e)}\nPlease enter valid numerical values.")

# Close Window
window.close()
