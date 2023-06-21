from PyQt6.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QTabWidget, QWidget, QHBoxLayout, QApplication
import sys

from rightside.ui import svod_balance_ui, consumers_ui, biku_ui, analitic_ui, network_structure_ui, disagreements_ui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ДагЭнерДжи')
        self.Width = 1200
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # add all widgets
        self.btn_1 = QPushButton('Сводный баланс', self)
        self.btn_2 = QPushButton('Потребители', self)
        self.btn_3 = QPushButton('Бику', self)
        self.btn_4 = QPushButton('Аналитика', self)
        self.btn_5 = QPushButton('Структура сети', self)
        self.btn_6 = QPushButton('Разногласия', self)

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)
        self.btn_5.clicked.connect(self.button5)
        self.btn_6.clicked.connect(self.button6)

        # add tabs
        self.svosvod_balance_tab = svod_balance_ui()
        self.consumers_tab = consumers_ui()
        self.biku_tab = biku_ui()
        self.analitic_tab = analitic_ui()
        self.network_structure_tab = network_structure_ui()
        self.disagreements_tab = disagreements_ui()

        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addWidget(self.btn_5)
        left_layout.addWidget(self.btn_6)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.setStyleSheet(
            "QTabWidget {border:1px solid #000000; border-radius: 10px;}"
        )
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.svosvod_balance_tab, '')
        self.right_widget.addTab(self.consumers_tab, '')
        self.right_widget.addTab(self.biku_tab, '')
        self.right_widget.addTab(self.analitic_tab, '')
        self.right_widget.addTab(self.network_structure_tab, '')
        self.right_widget.addTab(self.disagreements_tab, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def button1(self):
        self.right_widget.setCurrentIndex(0)

    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)

    def button4(self):
        self.right_widget.setCurrentIndex(3)

    def button5(self):
        self.right_widget.setCurrentIndex(4)

    def button6(self):
        self.right_widget.setCurrentIndex(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
