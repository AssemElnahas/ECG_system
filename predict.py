import torch
import torch.nn as nn
import numpy as np

class ECGClassifier(nn.Module):
    def __init__(self):
        super(ECGClassifier, self).__init__()
        self.conv1 = nn.Conv1d(1, 32, kernel_size=7)
        self.pool = nn.MaxPool1d(2)
        self.fc1 = nn.Linear(32 * 2500, 128)  # Assuming resized input ~5000 samples
        self.fc2 = nn.Linear(128, 5)  # 5 classes

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = ECGClassifier()
model.eval()  # Dummy pre-trained mode

DISEASES = ["Normal", "AFib", "PVC", "Tachycardia", "Bradycardia"]

def predict_ecg(ecg_signal, sample_length=5000):
    """
    Predict ECG disease using dummy model.
    
    Args:
        ecg_signal: Filtered ECG numpy array
    
    Returns:
        Predicted disease string
    """
    # Simple heuristic fallback + dummy model inference
    mean_rate = np.mean(np.abs(np.diff(ecg_signal)))
    std_dev = np.std(ecg_signal)
    
    if mean_rate < 0.5:
        pred_class = 4  # Bradycardia
    elif mean_rate > 2.0:
        pred_class = 3  # Tachycardia
    elif std_dev > 0.3:
        pred_class = 1  # AFib
    elif np.sum(np.abs(np.diff(ecg_signal)) > 0.5) > len(ecg_signal) * 0.1:
        pred_class = 2  # PVC
    else:
        pred_class = 0  # Normal
    
    # Dummy torch inference (random for demo)
    if len(ecg_signal) >= sample_length:
        sig_tensor = torch.tensor(ecg_signal[:sample_length].reshape(1, 1, -1), dtype=torch.float32)
        with torch.no_grad():
            logits = model(sig_tensor)
            pred_class = torch.argmax(logits, dim=1).item()
    
    return DISEASES[pred_class]

