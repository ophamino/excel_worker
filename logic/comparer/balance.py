from typing import Any
import os
from datetime import datetime

from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.worksheet import Worksheet

from logic.const import MAIN_DIR, MONTH_LIST

import json

FILE_JSON = 'balance.json'

class Balance:
    """
    Класс для формирования сводного баланса
    """    
    
    
    def open_excel(self, path: str, data_only: bool = False, read_only: bool = False) -> None:
        """
        Открывает файл, если его не существует - создаёт и открывает\n
        Args: path (str): путь к файлу, где должен находиться файл
        """
        if not os.path.exists(path):
            workbook = Workbook()
            workbook.save(path)
        return load_workbook(path, data_only=data_only, read_only=read_only)
    
    def create_months_sheet_if_not_exists(self, workbook: Workbook, month: str | int | None = None) -> None:
        """
       Создает месячный лист, если его не существует

        Args:
            workbook (Workbook): Документ excel, который будет проверяться\n\n
            month (str | int | None): Месячный лист, который должен находится в файле:\n
            Если значение `str`, то лист создаётся по названию;\n
            Если знаение `int`, то лист создается по номеру согласно порядку;\n
            Если значение `None`, то создается лист за текущий месяц.\n
            По умолчанию `None`.
        """

        sheetnames = workbook.sheetnames

        def create(workbook: Workbook, month: str | int, sheetnames: list[str]):
            if month not in sheetnames:
                workbook.create_sheet(month)

        if isinstance(month, str):
            if month in MONTH_LIST:
                create(workbook, month, sheetnames)
            else:
                raise ValueError(f"Указано неправильное название месяца: {month}")

        if isinstance(month, int):
            if 1 <= month <= len(MONTH_LIST):
                month = MONTH_LIST[month - 1]
                create(workbook, month, sheetnames)
            else:
                raise ValueError(f"Указан неправильный номер месяца: {month}")

        if month is None:
            month = datetime.now().month
            month = MONTH_LIST[month - 1]
            create(workbook, month, sheetnames)
        
        print(month)
            
    def open_sheet(self, workbook: Workbook, sheet_month: str | int) -> Worksheet:
        """
        Открывает лист по номеру или названию месяца

        Args:
            workbook (Workbook): Excel файл, лист которого нужно открыть\n
            sheet_month (str | int): Номер или название месяца

        Returns:
            Worksheet: Лист Excel файла
        """        
        self.create_months_sheet_if_not_exists(workbook, sheet_month)
        if isinstance(sheet_month, int):
            sheet_month = MONTH_LIST[sheet_month - 1]
        return workbook[sheet_month]

    def get_network_hash(self, month: str | int) -> dict[str, dict[str, str]]:
        """
        Функция для формирования хэш-таблицы сети из файлы "Структура сети.xlsx"
        Args:
            month (str | int): Номер месяца, за который нужно сформировать хэш-таблицу

        Returns:
            dict[str, dict[str, str]]: Хэш-таблица структуры сети
        """
        hash_table = {}
        
        network_structure_path = f"{MAIN_DIR}\Структура сети\Свод ОЭСХ.xlsx"
        network_structure = self.open_excel(network_structure_path, data_only=True)
        network = self.open_sheet(network_structure, month)

        for row in range(2, network.max_row):
            hash_table[network.cell(row=row, column=1).value] = {
                "name": network.cell(row=row, column=2).value,
                "foreign_key": network.cell(row=row, column=3).value,
                "foreign_key_name": network.cell(row=row, column=4).value,
                "expenses": 0
            }
        
        return hash_table
        
    
    def get_consumers_hash(self, month: str | int) -> dict[str, dict[str, str]]:
        """
        Функция для формирования хэш-таблицы потребителей из файлы "Сводная ведомость.xlsx"
        Args:
            month (str | int): Номер месяца, за который нужно сформировать хэш-таблицу

        Returns:
            dict[str, dict[str, str]]: Хэш-таблица потребителей
        """        
        hash_table = {}
        year = datetime.now().year
        
        consumers_path = f"{MAIN_DIR}\Сводный баланс\{year}\УПП\Сводная ведомость потребителей.xlsx"
        consumers_file = self.open_excel(consumers_path, data_only=True)
        consumers = self.open_sheet(consumers_file, month)
        
        for row in range(6, consumers.max_row):
            hash_table[consumers.cell(row=row, column=3).value] = {
                "ID": consumers.cell(row=row, column=3).value,
                "foreing_key": consumers.cell(row=row, column=39).value,
                "name": consumers.cell(row=row, column=8).value,
                "expenses": consumers.cell(row=row, column=29).value
            }
        
        with open(FILE_JSON, 'w') as outfile:
            outfile.write(
                json.dumps(
                hash_table,
                sort_keys=False,
                indent=4,
                ensure_ascii=False,
                separators=(',', ': ')
                )
            )

    def get_balance_hash(self, network_hash: dict[str, dict[str, str]], consumers_hash:  dict[str, dict[str, str]]) -> dict[str, dict[str, str]]:
        """
        Функция для формирования данных сводного баланса из файлов "Структура сети.xlsx" и "Сводная ведомость.xlsx"

        Args:
            network_hash (dict[str, dict[str, str]]): Хэш-таблица сети
            consumers_hash (dict[str, dict[str, str]]): Хэш-таблица потребителей

        Returns:
            dict[str, dict[str, str]]: Хэш-таблица баланса
        """
        pass
        
    def insert_hash_in_file(self) -> None:
        """
        Функция для вставки итоговых данных в файл "Сводный баланс"
        """        
        pass
    
    def insert_formula(self) -> None:
        """
        Функция для вставки формул в файл
        """
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
