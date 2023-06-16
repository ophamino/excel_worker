from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import QThread


class SideBarButtonThread(QThread):
    pass


class SideBarButton(QWidget):
    "Класс конпки бокового меню"
    def __init__(self, parent: QWidget | None = None) -> None:
        QWidget().__init__(self, parent)
        self.button = QPushButton("Название")
        self.button.setStyleSheet(
            "background-color: #fbeee0;"
            "border: 2px solid #422800;"
            "border-radius: 30px;"
            "box-shadow: #422800 4px 4px 0 0;"
            "color: #422800;"
            "cursor: pointer;"
            "display: inline-block;"
            "font-weight: 600;"
            "font-size: 18px;"
            "padding: 0 18px;"
            "line-height: 50px;"
            "text-align: center;"
            "text-decoration: none;"
           " user-select: none;"
            "-webkit-user-select: none;"
           " touch-action: manipulation;"
           "height: 150px;"
           "width: 250px;"
        )

    def call_function(func):
        pass