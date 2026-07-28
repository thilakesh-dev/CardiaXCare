"""
-------------------------------------------------------
CARDIAXCARE
app.py

Real-Time AI Integrated ECG Monitoring System

Workflow

AD8232 ECG Sensor
        ↓
Arduino Uno
        ↓
USB Serial Communication
        ↓
Python Application
        ↓
Signal Processing
        ↓
Feature Extraction
        ↓
CARDIAXCARE AI Model
        ↓
Prediction Result

-------------------------------------------------------
"""

import joblib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from serial_reader import SerialReader
from feature_extractor import ECGFeatureExtractor


# =====================================================
# Configuration
# =====================================================

SERIAL_PORT = "COM3"      # Change if required
BAUD_RATE = 9600

WINDOW_SIZE = 400         # Number of ECG samples

# =====================================================
# Load AI Model
# =====================================================

print("-----------------------------------------")
print("Loading CARDIAXCARE AI Model...")
print("-----------------------------------------")

model = joblib.load("model.pkl")

print("Model Loaded Successfully.")

# =====================================================
# Initialize Serial Reader
# =====================================================

reader = SerialReader(
    port=SERIAL_PORT,
    baudrate=BAUD_RATE
)

reader.connect()

# =====================================================
# Feature Extractor
# =====================================================

extractor = ECGFeatureExtractor()

# =====================================================
# ECG Buffer
# =====================================================

ecg_buffer = []

prediction_text = "Collecting ECG..."

# =====================================================
# Create Graph
# =====================================================

fig, ax = plt.subplots(figsize=(12,5))

line, = ax.plot([], [], lw=2)

ax.set_title("CARDIAXCARE - Live ECG")

ax.set_xlabel("Samples")

ax.set_ylabel("Amplitude")

ax.set_xlim(0, WINDOW_SIZE)

ax.set_ylim(0, 1023)

text_prediction = ax.text(
    0.02,
    0.92,
    "",
    transform=ax.transAxes,
    fontsize=12
)

# =====================================================
# Update Function
# =====================================================

def update(frame):

    global prediction_text

    value = reader.read_ecg()

    if value is None:
        return line,

    ecg_buffer.append(value)

    if len(ecg_buffer) > WINDOW_SIZE:
        ecg_buffer.pop(0)

    # Wait until buffer is full

    if len(ecg_buffer) < WINDOW_SIZE:

        line.set_data(range(len(ecg_buffer)), ecg_buffer)

        text_prediction.set_text("Collecting ECG Data...")

        return line,

    # ------------------------------------------
    # Signal Processing
    # ------------------------------------------

    filtered, normalized, features = extractor.process(ecg_buffer)

    # ------------------------------------------
    # AI Prediction
    # ------------------------------------------

    result = model.predict([features])[0]

    if result == 0:

        prediction_text = "Prediction : NORMAL ECG"

    else:

        prediction_text = "Prediction : POSSIBLE CARDIAC ANOMALY"

    # ------------------------------------------
    # Update Graph
    # ------------------------------------------

    line.set_data(range(WINDOW_SIZE), filtered)

    text_prediction.set_text(prediction_text)

    return line,

# =====================================================
# Animation
# =====================================================

ani = animation.FuncAnimation(

    fig,

    update,

    interval=10,

    cache_frame_data=False

)

plt.tight_layout()

try:

    plt.show()

except KeyboardInterrupt:

    pass

finally:

    reader.close()

    print("\nApplication Closed.")
  
