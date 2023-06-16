import sys
import typing
from PyQt6.QtCore import QObject

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QCalendarWidget, QMainWindow
from PyQt6 import QtCore
from sidebar import SideBarButton


class MainThread(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(str)
    
    def __init__(self, parent: QObject | None = None) -> None:
        QtCore.QThread.__init__(self, parent)


class MainWindow(QWidget):
    """Main window for DagEnargy application"""
    def __init__(self, parent: QWidget | None = None) -> None:
        QWidget.__init__(self, parent)
        self.label = QLabel("Дагэнерджи")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.btn_quit = QPushButton("&Close")
        self.vbox = QVBoxLayout()
        self.buton = SideBarButton()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btn_quit)
        self.setLayout(self.vbox)
        self.btn_quit.clicked.connect(QApplication.instance().quit)
        thread = MainThread()

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("DagEnergy")
    window.resize(800, 800)
    window.show()

    sys.exit(app.exec())
