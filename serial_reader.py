"""
-------------------------------------------------------
CARDIAXCARE
serial_reader.py

Reads ECG data from Arduino Uno using Serial Communication.

Author : THILAKESH TM
Project: CARDIAXCARE
-------------------------------------------------------
"""

import serial
import time


class SerialReader:
    """
    Reads ECG values from Arduino through USB Serial Port.
    """

    def __init__(self, port="COM3", baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial_port = None

    def connect(self):
        """
        Establish serial connection.
        """
        try:
            self.serial_port = serial.Serial(
                self.port,
                self.baudrate,
                timeout=1
            )

            # Wait for Arduino to reset
            time.sleep(2)

            print("--------------------------------")
            print(" CARDIAXCARE Serial Connected")
            print("--------------------------------")
            print(f"Port      : {self.port}")
            print(f"Baud Rate : {self.baudrate}")
            print("--------------------------------")

        except Exception as e:
            print("Connection Error")
            print(e)

    def read_ecg(self):
        """
        Reads one ECG sample from Arduino.

        Returns:
            int ECG value
            None if invalid
        """

        if self.serial_port is None:
            return None

        try:
            line = self.serial_port.readline().decode("utf-8").strip()

            if line == "":
                return None

            ecg = int(line)

            return ecg

        except:
            return None

    def close(self):
        """
        Close serial connection.
        """

        if self.serial_port:
            self.serial_port.close()
            print("Serial Port Closed")


# ---------------------------------------------------
# Standalone Testing
# ---------------------------------------------------

if __name__ == "__main__":

    reader = SerialReader(
        port="COM3",      # Change if needed
        baudrate=9600
    )

    reader.connect()

    try:

        while True:

            value = reader.read_ecg()

            if value is not None:
                print(value)

    except KeyboardInterrupt:

        print("\nStopping...")

    finally:

        reader.close()
