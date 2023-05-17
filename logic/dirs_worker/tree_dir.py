import os
from datetime import datetime

from openpyxl import load_workbook, Workbook


class TreeDir:
    """Класс для создания дерева каталогов"""

    def __init__(self, main_dir: str) -> None:
        if main_dir not in os.listdir('../'):
            os.mkdir(f'../{main_dir}')
        self._main_dir = f'../{main_dir}'

    def create_third_level(self, path: str) -> None:
        """Функия для создания третьего уровня каталога"""
        wb = Workbook()
        for departament_number in range(1, 6):
            departament_path = f'{path}/DS0{str(departament_number)}01'
            if not os.path.exists(departament_path):
                os.makedirs(departament_path)
            wb.save(f"{departament_path}/RV{str(datetime.now().year)}FL.xlsx")
            wb.save(f"{departament_path}/RV{str(datetime.now().year)}UL.xlsx")

    def create_second_level(self, path: str) -> None:
        """Функция для создания второго уровня каталога"""
        for month_number in range(1, 13):
            month_path = f'{path}/{str(month_number)}'
            if not os.path.exists(month_path):
                os.makedirs(month_path)
                self.create_third_level(month_path)

    def create_first_level(self, path: str) -> None:
        """Функция для создания первого уровня каталога"""
        first_level_path = f'{path}/{str(datetime.now().year)}'
        if not os.path.exists(first_level_path):
            os.makedirs(first_level_path)
            self.create_second_level(first_level_path)
            wb = Workbook()
            wb.save(f"{first_level_path}/SVOD{str(datetime.now().year)}FL.xlsx")
            wb.save(f"{first_level_path}/SVOD{str(datetime.now().year)}UL.xlsx")

    def create_new_tree_dir(self, name: str) -> None:
        """Функция для создания нового дерева каталогов"""
        three_path = f'{self._main_dir}/{name}'
        if not os.path.exists(three_path):
            os.makedirs(three_path)
            self.create_first_level(three_path)
        wb = Workbook()
        wb.save(f"{three_path}/static.xlsx")
        wb.save(f"{three_path}/static_without_changes.xlsx")
        wb.save(f"{three_path}/log.xlsx")
        wb.save(f"{three_path}/manual.xlsx")


test = TreeDir('documents')
test.create_new_tree_dir('CH')
