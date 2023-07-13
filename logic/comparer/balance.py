from typing import Any
from os import listdir
from datetime import datetime

from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.worksheet import Worksheet

from logic.const import MAIN_DIR, MONTH_LIST


class Balance:
    """
    Класс для формирования сводного баланса
    """    
    
    
    def open_excel(self, path: str) -> None:
        """
        Открывает файл, если его не существует - создаёт и открывает

        Args:
            path (str): путь к файлу, где должен находиться файл
        """
        if not listdir(path):
            workbook = Workbook()
            workbook.save(path)
        return load_workbook(path)
    
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
            if month not in MONTH_LIST:
                raise ValueError(f"Указано неправильное название месяца: {month}")

        if isinstance(month, int):
            if 1 <= month <= len(MONTH_LIST):
                month = MONTH_LIST[month - 1]
                create(workbook, month, sheetnames)

            if not 0 < month < len(MONTH_LIST):
                raise ValueError(f"Указан неправильный номер месяца: {month}")

        if month is None:
            month = datetime.now().month
            month = MONTH_LIST[month - 1]
            create(workbook, month, sheetnames)
            
    def open_sheet(self, workbook: Workbook, sheet_month: str | int) -> Worksheet:
        """
        Открывает лист по номеру или названию месяца

        Args:
            workbook (Workbook): Excel файл, лист которого нужно открыть
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
            month (str | int): Номер месяца, за который нужно сфофрмировать хэш-таблицу

        Returns:
            dict[str, dict[str, str]]: Хэш-таблица структуры сети
        """        
        network_structure_path = f"{MAIN_DIR}\Структура сети\Свод ОЭСХ.xlsx"
        network_structure = self.open_excel(network_structure_path)
        network = self.open_sheet(network_structure, month)
        
    
    def get_consumers_hash(self) -> dict[str, dict[str, str]]:
        """
        Функция для формирования хэш-таблицы потребителей из файлы "Сводная ведомость.xlsx"

        Returns:
            dict[str, dict[str, str]]: Хэш-таблица потребителей
        """        
        pass
    
    def get_balance_hash(self) -> dict[str, dict[str, str]]:
        """
        Функция для формирования данных сводного баланса из файлов "Структура сети.xlsx" и "Сводная ведомость.xlsx"

        Returns:
            dict[str, dict[str, str]]: Хэш таблица сводного баланса
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