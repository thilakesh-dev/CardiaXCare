````markdown
# Pin Connections

## Overview

The AD8232 ECG sensor is connected to the Arduino Uno to acquire the heart's electrical signals. The Arduino reads the analog ECG signal and transmits the data to the laptop through USB serial communication, where the CARDIAXCARE AI model performs prediction.

---

# Hardware Connections

| AD8232 ECG Sensor | Arduino Uno | Description |
|-------------------|-------------|-------------|
| 3.3V             | 3.3V        | Power Supply |
| GND              | GND         | Ground |
| OUTPUT           | A0          | ECG Analog Signal |
| LO+ *(Optional)* | D10         | Lead-Off Detection (+) |
| LO− *(Optional)* | D11         | Lead-Off Detection (−) |
| SDN *(Optional)* | Not Connected | Shutdown Pin (Unused) |

> **Note:** In this prototype, only the **OUTPUT**, **3.3V**, and **GND** connections are required for ECG acquisition. The Lead-Off pins are optional and can be used to detect disconnected electrodes.

---

# Electrode Placement

The AD8232 module uses three disposable ECG electrodes.

| Electrode | Placement |
|-----------|-----------|
| RA (Right Arm) | Below the right collarbone |
| LA (Left Arm) | Below the left collarbone |
| RL (Right Leg) | Lower right abdomen or right leg (Reference/Ground) |

Approximate placement:

```
          O
         /|\
      RA   LA

         |
         |

        RL
```

---

# Wiring Diagram

```
             AD8232 ECG Sensor
          -----------------------
          |                     |
          |   3.3V ------------ 3.3V (Arduino)
          |   GND  ------------ GND
          |   OUTPUT --------- A0
          |   LO+ ------------ D10 (Optional)
          |   LO- ------------ D11 (Optional)
          |   SDN ------------ NC
          -----------------------
                    │
                    │
                    ▼
             Arduino Uno
                    │
          USB Serial Communication
                    │
                    ▼
              Laptop / PC
                    │
                    ▼
        Python Application (VS Code)
                    │
                    ▼
       CARDIAXCARE AI Prediction Model
```

---

# Complete System Connection

```
      ECG Electrodes
            │
            ▼
    AD8232 ECG Sensor
            │
            ▼
      Arduino Uno
            │
      USB Cable
            │
            ▼
      Laptop / Computer
            │
            ▼
      Python Program
            │
            ▼
   CARDIAXCARE AI Model
            │
            ▼
   Cardiac Prediction Result
```

---

# Connection Notes

- Supply the AD8232 module using the **3.3V** pin of the Arduino Uno.
- Ensure all GND connections are common.
- Connect the sensor **OUTPUT** pin to **A0** to read the ECG signal.
- Use a USB cable to power the Arduino and transfer serial data to the laptop.
- If noisy signals are observed, ensure the electrodes are firmly attached and the subject remains still during acquisition.

---

# Summary

| Component | Connected To |
|-----------|--------------|
| AD8232 3.3V | Arduino 3.3V |
| AD8232 GND | Arduino GND |
| AD8232 OUTPUT | Arduino A0 |
| Arduino Uno | Laptop via USB |
| Laptop | Python Application |
| Python Application | CARDIAXCARE AI Model |

The Arduino Uno acts as the data acquisition device, while the laptop performs AI-based ECG analysis using the CARDIAXCARE model.
````
