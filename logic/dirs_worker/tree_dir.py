import os
from datetime import datetime

from logic.const import MAIN_DIR, MONTH_LIST, DEPARTAMENT_NAMES


class TreeDir:
    """Класс для создания дерева каталогов"""

    def __init__(self) -> None:
        self.main_dir = MAIN_DIR

    def validate_dir(self, path: str) -> None:
        """Функция для проверки сущесьвует ли папка"""
        if not os.path.exists(path):
            os.makedirs(path)

    def crete_main_folders(self) -> None:
        """Функция для создания главных папок"""
        folder_name = [
            "Потребители",
            "Структура сети",
            "Сводный баланс",
            "Аналитика",
            "Разногласия",
            "Бику"
        ]

        self.validate_dir(self.main_dir)

        for folder in folder_name:
            path = f"{self.main_dir}\{folder}"
            self.validate_dir(path)

    def create_analitic_dirs(self) -> None:
        folder_name = [
            "Отчеты",
            "Dashboard",
            "Анализ по Разногласиям"
        ]

        main_path = f"{self.main_dir}\Аналитика"
        self.validate_dir(main_path)

        for folder in folder_name:
            path = f"{main_path}\{folder}"
            self.validate_dir(path)

    def create_disagreements_dirs(self) -> None:
        main_path = f"{self.main_dir}\Разногласия"
        year = f"{main_path}\{datetime.now().year}"
        self.validate_dir(year)
        for month_number in MONTH_LIST:
            self.validate_dir(f'{year}\{month_number}')

    def create_svod_balance(self):
        year = f"{self.main_dir}\Сводный баланс\{datetime.now().year}"
        self.validate_dir(year)
        folders_name = [
            "Бику",
            "УПП"
        ]

        for folder in folders_name:
            path = f"{year}\{folder}"
            self.validate_dir(path)
            for month_number in MONTH_LIST:
                month = f"{path}\{month_number}"
                self.validate_dir(month)
                for departament in DEPARTAMENT_NAMES:
                    departament = f"{month}\{departament}"
                    self.validate_dir(departament)
        
    def create_tree_dir(self) -> None:
        self.crete_main_folders()
        self.create_analitic_dirs()
        self.create_disagreements_dirs()
        self.create_svod_balance()

test = TreeDir()
test.create_tree_dir()