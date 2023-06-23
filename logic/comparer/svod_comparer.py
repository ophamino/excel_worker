from openpyxl import load_workbook
from datetime import datetime
import os

from logic.const import MAIN_DIR, MONTH_LIST

class Comparer:

    def __init__(self) -> None:
        self.main_dir = MAIN_DIR
        self.year = datetime.now().year
        self.month = datetime.now().month

    def comparer(self, file_status: str, month: str) -> None:
        static_path = f'{self.main_dir}\Сводный баланс\{self.year}\УПП'

        if not static_path in os.listdir(static_path):
            svod = load_workbook('template/svod.xlsx')
            svod.save(f"{static_path}\Сводная ведомость {file_status} потребления.xlsx")
        svod = load_workbook(f"{static_path}\Сводная ведомость {file_status} потребления.xlsx", data_only=True)
        svod_sheet = svod[str(month)]

        month_path = f"{static_path}\{MONTH_LIST[month - 1]}"
        print(month_path)

        for departement in os.listdir(month_path):
            try:
                workbook = load_workbook(f'{month_path}\{departement}\РВ {file_status} потребления.xlsx').worksheets[0]
                for row in workbook.iter_rows(min_row=11, values_only=True):
                    svod_sheet.append(row)
            except Exception:
                print(f"[INFO] Сформировать документ невозможно, Файл отсутсвует или не соответсвует синтаксису."
                      f"[INFO] Папка: {month_path}\{departement}")

        svod.save(f"{static_path}\Сводная ведомость {file_status} потребления.xlsx")
