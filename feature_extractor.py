"""
-------------------------------------------------------
CARDIAXCARE
feature_extractor.py

Signal preprocessing and ECG feature extraction.

Author : THILAKESH TM 
Project: CARDIAXCARE
-------------------------------------------------------
"""

import numpy as np
from scipy.signal import butter, filtfilt


class ECGFeatureExtractor:

    def __init__(self, sampling_rate=200):
        self.fs = sampling_rate

    # --------------------------------------------------
    # Butterworth Low-Pass Filter
    # --------------------------------------------------

    def lowpass_filter(self, signal, cutoff=40, order=4):
        """
        Removes high-frequency noise.

        Parameters
        ----------
        signal : list or numpy array
        cutoff : cutoff frequency (Hz)

        Returns
        -------
        Filtered ECG signal
        """

        nyquist = 0.5 * self.fs
        normal_cutoff = cutoff / nyquist

        b, a = butter(order, normal_cutoff, btype='low')

        filtered = filtfilt(b, a, signal)

        return filtered

    # --------------------------------------------------
    # Normalize ECG
    # --------------------------------------------------

    def normalize(self, signal):
        """
        Normalize ECG between 0 and 1.
        """

        signal = np.asarray(signal)

        minimum = np.min(signal)
        maximum = np.max(signal)

        if maximum == minimum:
            return signal

        normalized = (signal - minimum) / (maximum - minimum)

        return normalized

    # --------------------------------------------------
    # Feature Extraction
    # --------------------------------------------------

    def extract_features(self, signal):
        """
        Extract statistical ECG features.

        Returns
        -------
        Feature vector
        """

        signal = np.asarray(signal)

        features = [

            np.mean(signal),

            np.std(signal),

            np.var(signal),

            np.min(signal),

            np.max(signal),

            np.median(signal),

            np.ptp(signal),            # Peak-to-Peak

            np.sqrt(np.mean(signal**2)),  # RMS

            np.max(np.abs(signal)),    # Maximum Absolute Value

            np.sum(signal**2)          # Signal Energy

        ]

        return np.array(features)

    # --------------------------------------------------
    # Complete Processing Pipeline
    # --------------------------------------------------

    def process(self, signal):
        """
        Complete ECG preprocessing.

        Raw ECG
            ↓
        Low-pass Filter
            ↓
        Normalization
            ↓
        Feature Extraction
        """

        filtered = self.lowpass_filter(signal)

        normalized = self.normalize(filtered)

        features = self.extract_features(normalized)

        return filtered, normalized, features


# ------------------------------------------------------
# Example Usage
# ------------------------------------------------------

if __name__ == "__main__":

    extractor = ECGFeatureExtractor()

    # Simulated ECG signal

    ecg = np.random.randint(450, 600, 400)

    filtered, normalized, features = extractor.process(ecg)

    print("Filtered Signal Length :", len(filtered))

    print("Normalized Signal Length :", len(normalized))

    print("\nExtracted Features\n")

    feature_names = [

        "Mean",

        "Standard Deviation",

        "Variance",

        "Minimum",

        "Maximum",

        "Median",

        "Peak-to-Peak",

        "RMS",

        "Maximum Absolute",

        "Signal Energy"

    ]

    for name, value in zip(feature_names, features):
        print(f"{name:20} : {value:.4f}")



############################################################
  Raw ECG Signal
       │
       ▼
Butterworth Low-Pass Filter
       │
       ▼
Noise Reduced ECG
       │
       ▼
Normalization (0–1)
       │
       ▼
Feature Extraction
       │
       ▼
Feature Vector
       │
       ▼
Machine Learning Model

#######################################################
Filtered Signal Length : 400
Normalized Signal Length : 400

Extracted Features

Mean                 : 0.5123
Standard Deviation   : 0.1942
Variance             : 0.0377
Minimum              : 0.0000
Maximum              : 1.0000
Median               : 0.5051
Peak-to-Peak         : 1.0000
RMS                  : 0.5486
Maximum Absolute     : 1.0000
Signal Energy        : 120.4158
