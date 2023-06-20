from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QFrame


class RightButton(QFrame):
    def __init__(self, button_text: str, button_description: str):
        super().__init__()
        self.resize(500, 150)
        self.title = QLabel(button_text)
        self.title.setStyleSheet(
            "font-size: 18px;"
            "font-weight: bold;"
            "border: none;"
        )
        self.description= QLabel(button_description)
        self.description.setStyleSheet(
            "font-size: 12px;"
            "border: none;"
        )
        self.button = QPushButton("Сформировать")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.title)
        self.vbox.addWidget(self.description)
        self.vbox.addWidget(self.button)

        self.setStyleSheet("QFrame {border:1px solid #000000; border-radius: 10px;}")
        self.setLayout(self.vbox)