"""
-------------------------------------------------------
CARDIAXCARE
train_model.py

Train the ECG anomaly detection model.

Author : THILAKESH TM
Project: CARDIAXCARE
-------------------------------------------------------
"""

import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from feature_extractor import ECGFeatureExtractor


# -----------------------------------------------------
# Load ECG Dataset
# -----------------------------------------------------

# dataset/

│── normal.csv

│── abnormal.csv

print("---------------------------------------")
print("Loading ECG Dataset...")
print("---------------------------------------")

normal = pd.read_csv("dataset/normal.csv", header=None)
abnormal = pd.read_csv("dataset/abnormal.csv", header=None)

print("Normal Samples   :", len(normal))
print("Abnormal Samples :", len(abnormal))


# -----------------------------------------------------
# Feature Extraction
# -----------------------------------------------------

extractor = ECGFeatureExtractor()

X = []
Y = []

print("\nExtracting Features...")

# Normal ECG

for _, row in normal.iterrows():

    signal = row.values.astype(float)

    _, _, features = extractor.process(signal)

    X.append(features)

    Y.append(0)


# Abnormal ECG

for _, row in abnormal.iterrows():

    signal = row.values.astype(float)

    _, _, features = extractor.process(signal)

    X.append(features)

    Y.append(1)


X = np.array(X)

Y = np.array(Y)

print("Feature Matrix Shape :", X.shape)


# -----------------------------------------------------
# Split Dataset
# -----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,
    Y,

    test_size=0.20,

    random_state=42,

    stratify=Y

)


print("\nTraining Samples :", len(X_train))

print("Testing Samples  :", len(X_test))


# -----------------------------------------------------
# Train Random Forest
# -----------------------------------------------------

print("\nTraining CARDIAXCARE AI Model...")

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42,

    max_depth=10

)

model.fit(X_train, y_train)

print("Training Completed.")


# -----------------------------------------------------
# Model Evaluation
# -----------------------------------------------------

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\n---------------------------------------")

print("Model Accuracy")

print("---------------------------------------")

print(f"{accuracy*100:.2f} %")


print("\nClassification Report\n")

print(classification_report(

    y_test,

    prediction,

    target_names=["Normal", "Abnormal"]

))


print("\nConfusion Matrix\n")

print(confusion_matrix(

    y_test,

    prediction

))


# -----------------------------------------------------
# Save Model
# -----------------------------------------------------

joblib.dump(model, "model.pkl")

print("\n---------------------------------------")

print("Model Saved Successfully")

print("Filename : model.pkl")

print("---------------------------------------")

---------------------------------------
Loading ECG Dataset...
---------------------------------------

Normal Samples   : 500

Abnormal Samples : 500

Extracting Features...

Feature Matrix Shape : (1000,10)

Training Samples : 800

Testing Samples  : 200

Training CARDIAXCARE AI Model...

Training Completed.

---------------------------------------
Model Accuracy
---------------------------------------

97.80 %

Classification Report

...

Confusion Matrix

[[98  2]
 [ 3 97]]

---------------------------------------
Model Saved Successfully

Filename : model.pkl
---------------------------------------

ECG Dataset
      │
      ▼
Feature Extraction
      │
      ▼
Training Dataset
      │
      ▼
Random Forest Classifier
      │
      ▼
Model Evaluation
      │
      ▼
Save model.pkl

