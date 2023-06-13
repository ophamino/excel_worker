import os
from datetime import datetime

from openpyxl import load_workbook, Workbook


class TreeDir:
    """Класс для создания дерева каталогов"""

    def __init__(self) -> None:
        self.main_dir = "../Dagenergy"

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
            path = f"{self.main_dir}/{folder}"
            self.validate_dir(path)

    def create_analitic_dirs(self) -> None:
        folder_name = [
            "Отчеты",
            "Dashboard",
            "Анализ по Разногласиям"
        ]

        main_path = f"{self.main_dir}/Аналитика"
        self.validate_dir(main_path)

        for folder in folder_name:
            path = f"{self.main_dir}/{main_path}/{folder}"
            self.validate_dir(path)

    def create_disagreements_dirs(self) -> None:
        main_path = f"{self.main_dir}/Разногласия"
        year = f"{main_path}/{datetime.now().year}"
        self.validate_dir(year)
        for month_number in range(1, 13):
            self.validate_dir(f'{year}/{month_number}')

    def create_svod_balance(self):
        year = f"{self.main_dir}/Сводный баланс/{datetime.now().year}"
        self.validate_dir(year)
        folders_name = [
            "Бику",
            "УПП"
        ]

        for folder in folders_name:
            path = f"{year}/{folder}"
            self.validate_dir(path)
            for month_number in range(1, 13):
                month = f"{path}/{month_number}"
                self.validate_dir(month)
                for departament in range(1, 6):
                    departament = f"{month}/Отделение {departament}"
                    self.validate_dir(departament)
