import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QCalendarWidget, QMainWindow
from PyQt6 import QtCore


class MainWindow(QWidget):
    """Main window for DagEnargy application"""
    def __init__(self, parent: QWidget | None = None) -> None:
        QWidget.__init__(self, parent)
        self.label = QLabel("Дагэнерджи")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.btn_quit = QPushButton("&Close")
        self.vbox = QVBoxLayout()
        # self.calendar = QCalendarWidget()
        self.vbox.addWidget(self.label)
        # self.vbox.addWidget(self.calendar)
        self.vbox.addWidget(self.btn_quit)
        self.setLayout(self.vbox)
        self.btn_quit.clicked.connect(QApplication.instance().quit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("DagEnergy")
    window.resize(800, 800)
    window.show()

    sys.exit(app.exec())