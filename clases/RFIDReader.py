import threading
import serial
from PySide2 import QtCore
from PySide2.QtWidgets import QMessageBox

class RFIDReader(QtCore.QObject):
    uid_detected_signal = QtCore.Signal(str)  # Señal para pasar la UID detectada

    def __init__(self, port='COM7', baudrate=9600, parent=None):
        super(RFIDReader, self).__init__(parent)
        self.port = port
        self.baudrate = baudrate
        self.arduino = None
        self.start_reading()

    def start_reading(self):
        try:
            self.arduino = serial.Serial(self.port, self.baudrate, timeout=1)
            self.arduino.flush()
            self.read_thread = threading.Thread(target=self.read_rfid)
            self.read_thread.daemon = True  # Termina el hilo cuando se cierra la ventana
            self.read_thread.start()
        except serial.SerialException as e:
            QMessageBox.critical(None, "Error", f"No se pudo abrir el puerto serial: {e}")

    def read_rfid(self):
        while True:
            if self.arduino.in_waiting > 0:
                rfid_data = self.arduino.readline().decode('utf-8').strip()
                if rfid_data.startswith("UID:"):
                    uid = rfid_data.split(":")[1].strip()
                    self.uid_detected_signal.emit(uid)  # Emitir la señal con la UID detectada

    def close(self):
        if self.arduino:
            self.arduino.close()  # Cierra el puerto serial