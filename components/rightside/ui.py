from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from .buttons import RightButton


def svod_balance_ui():
    main_layout = QVBoxLayout()
    label = QLabel("Сводный баланс")
    main_layout.addWidget(label)
    main_layout.addWidget(RightButton("Отчет", "Сформировать отчет гп"))
    main_layout.addWidget(RightButton("Number 2", "ghbd"))
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


def consumers_ui():
    main_layout = QVBoxLayout()
    main_layout.addWidget(QLabel("Потребители"))
    main_layout.addStretch(5)
    main = QWidget()
    main.setLayout(main_layout)
    return main

def biku_ui():
    main_layout = QVBoxLayout()
    main_layout.addWidget(QLabel("БИКУ"))
    main_layout.addStretch(5)
    main = QWidget()
    main.setLayout(main_layout)
    return main


def analitic_ui():
    main_layout = QVBoxLayout()
    label = QLabel("Аналитика")
    main_layout.addWidget(label)
    main_layout.addWidget(RightButton("Реестр СУ", "Тут должно быть описание"))
    main_layout.addWidget(RightButton("Сводный баланс", "Тут должно быть описание"))
    main_layout.addWidget(RightButton("Сводная ведомость", "Тут должно быть описание"))
    main_layout.addWidget(RightButton("Расчет компенсация потерь", "Тут должно быть описание"))
    main_layout.addWidget(RightButton("Акт оказания услуг", "Тут должно быть описание"))
    main_layout.addStretch(5)
    label.setStyleSheet(
        "font-size: 18px;"
        "font-weight: bold;"
        "margin-bottom: 1em;"
        "margin-top: 0.3em;"
    )
    main = QWidget()
    main.setLayout(main_layout)
    return main


def network_structure_ui():
    main_layout = QVBoxLayout()
    main_layout.addWidget(QLabel("Структура сети"))
    main_layout.addStretch(5)
    main = QWidget()
    main.setLayout(main_layout)
    return main


def disagreements_ui():
    main_layout = QVBoxLayout()
    main_layout.addWidget(QLabel("Разногласия"))
    main_layout.addStretch(5)
    main = QWidget()
    main.setLayout(main_layout)
    return main
