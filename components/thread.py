import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QObject

class MyThread(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent: QObject | None = None) -> None:
        QtCore.QThread.__init__(self, parent)
    
    def run(self):
        for num in range(1, 12):
            self.sleep(1)
            self.my_signal.emit("num = %s" % num)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Нажмите кнопку для запуска потока")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.button = QtWidgets.QPushButton('Запустить процесс')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.my_thread = MyThread()
        self.button.clicked.connect(self.on_clicked)
        self.my_thread.started.connect(self.on_started)
        self.my_thread.finished.connect(self.on_finished)
        self.my_thread.my_signal.connect(self.on_change, QtCore.Qt.ConnectionType.QueuedConnection)
        

    def on_clicked(self):
        self.button.setDisabled(True)
        self.my_thread.start()
    
    def on_started(self):
        self.label.setText('Вызов метода on_started')

    def on_finished(self):
        self.label.setText('Вызван метод on_finished')
        self.button.setDisabled(False)

    def on_change(self, s):
        self.label.setText(s) 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('aasdjaoj')
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec())