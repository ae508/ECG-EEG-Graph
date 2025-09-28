import pandas as pd
import plotly.graph_objects as go

#Loading and Cleaning is CSV

filename = "EEG and ECG data_02_raw.csv"

#Ignoring the #s
df = pd.read_csv(filename, comment='#')

#Check to see if it prints

print(df.columns.tolist())
print(df.head())

#Select relevant columns

time_col = "Time"

eeg = ["Fz" , "P3", "C3", "F3", "F4", "C4", "P4", "Cz", "A1", "Fp1", "Fp2", "T3", "T5", "O1", "O2", "F7", "F8", "A2", "T6", "T4", "Pz"]
ecg = ["X2:REOG", "X1:LEOG"]
cm = "CM"

#Finding relevant columns

available_eeg = [ch for ch in eeg if ch in df.columns]
available_ecg = [ch for ch in ecg if ch in df.columns]
cm_present = cm if cm in df.columns else None

#Printing columns

print("EGG Channels:", available_eeg)
print("ECG Channels:", available_ecg)
print("CM channel available:", cm_present)

#Interactive plot
fig = go.Figure()

#EEG
for ch in available_eeg:
    fig.add_trace(go.Scatter(
        x = df[time_col],
        y = df[ch],
        mode= 'lines',
        name= f"EGG: {ch}",
        yaxis="y1"
    ))

#ECG
for ch in available_ecg:
    fig.add_trace(go.Scatter(
        x = df[time_col],
        y = df[ch],
        mode= 'lines',
        name= f"ECG: {ch}",
        yaxis="y2"
    ))

#CM
if cm_present:
    fig.add_trace(go.Scatter(
        x = df[time_col],
        y = df[ch],
        mode= 'lines',
        name="CM",
        yaxis="y2",
        line=dict(dash='dot')
    ))

#Layout with dual y-axes
    fig.update_layout(
        title="EEG + EGC Scrollable Plot",
        xaxis =dict(
            title="Seconds",
            rangeslider=dict(visible=True),
            type="linear"
        ),
    yaxis=dict(
        title ="EEG (uV)",
        side = "left",
        showgrid=True
    ),
    yaxis2=dict(
        title="ECG / CM (mV)",
        overlaying="y",
        side="right",
        showgrid=False
    ),
    legend=dict(
        orientation="h",
        y=-0.3,
        x=0.5,
        xanchor="center",
        yanchor="top"
    ),
    hovermode="x unified",
    height=800
)

#To show on browser


fig.show()
