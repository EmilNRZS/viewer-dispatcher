#!/usr/bin/env python3

import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("System Monitor")
        self.setGeometry(300, 300, 400, 400)

        # Метки для отображения данных
        self.cpu_label = QLabel("CPU Usage: 0%", self)
        self.memory_label = QLabel("Memory Usage: 0%", self)
        self.memory_detail_label = QLabel("Memory: 0 MB / 0 GB", self)  # Детали памяти
        self.disk_label = QLabel("Disk Usage: 0%", self)
        self.disk_detail_label = QLabel("Disk: 0 GB / 0 GB", self)  # Детали диска
        self.temp_label = QLabel("CPU Temperature: N/A", self)

        # Шрифты и стиль
        for label in [self.cpu_label, self.memory_label, self.memory_detail_label,
                      self.disk_label, self.disk_detail_label, self.temp_label]:
            label.setStyleSheet("font-size: 18px; color: black;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.memory_label)
        layout.addWidget(self.memory_detail_label)
        layout.addWidget(self.disk_label)
        layout.addWidget(self.disk_detail_label)
        layout.addWidget(self.temp_label)

        self.setLayout(layout)

        # Таймер обновления
        self.timer = self.startTimer(1000)

    def timerEvent(self, event):
        # CPU
        cpu_usage = psutil.cpu_percent(interval=1)
        self.cpu_label.setText(f"CPU Usage: {cpu_usage:.1f}%")

        # Memory
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        self.memory_label.setText(f"Memory Usage: {memory_usage:.1f}%")
        used_memory_mb = memory.used / (1024 ** 2)
        total_memory_gb = memory.total / (1024 ** 3)
        self.memory_detail_label.setText(
            f"Memory: {used_memory_mb:.1f} MB / {total_memory_gb:.1f} GB"
        )

        # Disk
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        self.disk_label.setText(f"Disk Usage: {disk_usage:.1f}%")
        used_disk_gb = disk.used / (1024 ** 3)
        total_disk_gb = disk.total / (1024 ** 3)
        self.disk_detail_label.setText(
            f"Disk: {used_disk_gb:.1f} GB / {total_disk_gb:.1f} GB"
        )

        # CPU Temperature
        try:
            temperature = psutil.sensors_temperatures()
            if "coretemp" in temperature:
                cpu_temp = temperature["coretemp"][0].current
                self.temp_label.setText(f"CPU Temperature: {cpu_temp} °C")
            else:
                self.temp_label.setText("CPU Temperature: N/A")
        except Exception:
            self.temp_label.setText("CPU Temperature: Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemMonitor()
    window.show()
    sys.exit(app.exec_())

