import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("System Monitor")
        self.setGeometry(300, 300, 400, 300)

        # Создание меток для отображения данных
        self.cpu_label = QLabel("CPU Usage: 0%", self)
        self.memory_label = QLabel("Memory Usage: 0%", self)
        self.disk_label = QLabel("Disk Usage: 0%", self)  # Метка для отображения использования диска

        # Устанавливаем шрифт и стиль для меток
        self.cpu_label.setStyleSheet("font-size: 18px; color: black;")
        self.memory_label.setStyleSheet("font-size: 18px; color: black;")
        self.disk_label.setStyleSheet("font-size: 18px; color: black;")  # Стиль для метки диска

        # Вертикальный layout
        layout = QVBoxLayout()
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.memory_label)
        layout.addWidget(self.disk_label)  # Добавляем метку для диска

        self.setLayout(layout)

        # Обновление данных каждую секунду
        self.timer = self.startTimer(1000)

    def timerEvent(self, event):
        # Получение информации о ЦП
        cpu_usage = psutil.cpu_percent(interval=1)
        self.cpu_label.setText(f"CPU Usage: {cpu_usage:.1f}%")

        # Получение информации о памяти
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        self.memory_label.setText(f"Memory Usage: {memory_usage:.1f}%")

        # Получение информации о диске (основной памяти)
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        self.disk_label.setText(f"Disk Usage: {disk_usage:.1f}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemMonitor()
    window.show()
    sys.exit(app.exec_())
