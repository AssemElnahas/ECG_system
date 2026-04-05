import streamlit as st
import numpy as np
import plotly.graph_objects as go
from model.predict import predict_ecg
from processing.filter_signal import bandpass_filter

st.set_page_config(page_title="ECG AI System", layout="wide")

st.title("ECG AI System")
st.write("Upload ECG data, visualize the signal, and predict disease.")

# Upload ECG file (CSV with 1 column of samples)
uploaded_file = st.file_uploader("Upload ECG CSV", type=["csv"])

if uploaded_file is not None:
    # Load signal
    signal = np.loadtxt(uploaded_file, delimiter=",")
    
    # Preprocess
    filtered_signal = bandpass_filter(signal)
    
    # Display 2D ECG signal
    st.subheader("ECG Signal (2D)")
    st.line_chart(filtered_signal)
    
    # Display 3D ECG signal
    st.subheader("ECG Signal (3D)")
    time = np.arange(len(filtered_signal))
    fig = go.Figure(data=[go.Scatter3d(
        x=time, y=np.zeros_like(time), z=filtered_signal, mode='lines', line=dict(color='yellow')
    )])
    fig.update_layout(scene=dict(
        xaxis_title='Time',
        yaxis_title='Lead',
        zaxis_title='Amplitude'
    ))
    st.plotly_chart(fig, use_container_width=True)
    
    # Prediction
    st.subheader("Predected desease")
    disease = predict_ecg(filtered_signal)
    st.success(f"Predicted: {disease}")
    
    # Simple treatment suggestion
    st.subheader("Treatment Recommendation")
    treatment_map = {
        "Normal": "No action needed.",
        "AFib": "Consult a cardiologist. Medication may be needed.",
        "PVC": "Monitor condition, consult doctor if frequent.",
        "Tachycardia": "Seek medical advice for heart rate control.",
        "Bradycardia": "Consult doctor for possible pacemaker."
    }
    st.info(treatment_map.get(disease, "Consult your doctor."))