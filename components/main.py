from PyQt6.QtWidgets import *
import sys

from rightside.buttons import RightButton


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
    
        # self.btn_1.setStyleSheet(style)
        # self.btn_2.setStyleSheet(style)
        # self.btn_3.setStyleSheet(style)
        # self.btn_4.setStyleSheet(style)
        # self.btn_5.setStyleSheet(style)
        # self.btn_6.setStyleSheet(style)

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)
        self.btn_5.clicked.connect(self.button5)
        self.btn_6.clicked.connect(self.button6)

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()
        self.tab5 = self.ui5()
        self.tab6 = self.ui6()

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
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')
        self.right_widget.addTab(self.tab6, '')

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

    def ui1(self):
        main_layout = QVBoxLayout()
        label = QLabel("Сводный баланс")
        main_layout.addWidget(label)
        main_layout.addWidget(RightButton("Отчет", "Сформировать отчет гп"))
        main_layout.addWidget(RightButton("Number 2", "ghbd"))
        label.setStyleSheet(
            "font-size: 18px;"
            "font-weight: bold;"
            "margin-bottom: 1em;"
            "margin-top: 0.3em;"
        )

        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Потребители"))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("БИКУ"))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Аналитика"))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui5(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Структура сети"))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui6(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Разногласия"))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
