import streamlit as st
import plotly.graph_objects as go
import numpy as np

def patient_age_input():
    """Patient age input sidebar."""
    st.sidebar.markdown("### Patient Info")
    age = st.sidebar.number_input("Patient Age", min_value=0, max_value=120, value=45)
    return age

def ecg_waveform_plot(signal, height=400):
    """2D ECG waveform plot - device-like scrolling green/red on black."""
    time = np.arange(len(signal))
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=time, y=signal,
        mode='lines',
        line=dict(color='lime', width=2),
        hovertemplate='Time: %{x:.0f}s<br>Amplitude: %{y:.2f}<extra></extra>'
    ))
    fig.update_layout(
        title="Live ECG Waveform",
        xaxis_title="Time (samples)",
        yaxis_title="Amplitude (mV)",
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='lime'),
        height=height,
        showlegend=False,
        margin=dict(l=0, r=0, t=40, b=0),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )
    st.plotly_chart(fig, use_container_width=True)

def prediction_panel(disease):
    """AI Prediction digital display."""
    colors = {
        'Normal': 'green',
        'AFib': 'orange',
        'PVC': 'yellow',
        'Tachycardia': 'red',
        'Bradycardia': 'blue'
    }
    color = colors.get(disease, 'white')
    st.markdown(f'''
        <div style="background: linear-gradient(145deg, #1a1a1a, #0a0a0a); border: 3px solid {color}; border-radius: 15px; padding: 20px; text-align: center; box-shadow: 0 0 20px {color}80;">
            <h2 style="color: {color}; font-family: monospace; font-size: 2.5em; margin: 0;">AI DIAGNOSIS</h2>
            <h1 style="color: {color}; font-family: monospace; font-size: 3.5em; margin: 10px 0;">{disease}</h1>
        </div>
    ''', unsafe_allow_html=True)

def treatment_panel(disease):
    """Treatment recommendation panel."""
    treatment_map = {
        "Normal": "No action needed. Healthy ECG.",
        "AFib": "Consult cardiologist. Anticoagulants/rate control may be needed.",
        "PVC": "Monitor. Consult if frequent (>10/hr). Beta-blockers possible.",
        "Tachycardia": "Emergency if >150bpm. Cardioversion/meds.",
        "Bradycardia": "Pacemaker if symptomatic. Monitor."
    }
    treatment = treatment_map.get(disease, "Consult physician immediately.")
    st.markdown(f'''
        <div style="background: #001100; border: 2px solid lime; border-radius: 10px; padding: 15px;">
            <h3 style="color: lime; margin: 0 0 10px 0;">TREATMENT</h3>
            <p style="color: white; font-family: monospace; line-height: 1.4;">{treatment}</p>
        </div>
    ''', unsafe_allow_html=True)

def ecg_3d_plot(signal, height=400):
    """3D ECG view."""
    time = np.arange(len(signal))
    fig = go.Figure(data=[go.Scatter3d(
        x=time, y=np.zeros_like(time), z=signal,
        mode='lines',
        line=dict(color='red', width=4)
    )])
    fig.update_layout(
        scene=dict(
            xaxis_title='Time',
            yaxis_title='Lead',
            zaxis_title='mV',
            bgcolor='black'
        ),
        plot_bgcolor='black',
        paper_bgcolor='black',
        height=height
    )
    st.plotly_chart(fig, use_container_width=True)

