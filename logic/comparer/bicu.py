from openpyxl import load_workbook
import os
from datetime import datetime

from logic.const import MAIN_DIR, MONTH_LIST


def comparer(month: str) -> None:
        
        static_path = f'{MAIN_DIR}\Сводный баланс\{datetime.now().year}\Бику'

        if not static_path in os.listdir(static_path):
            svod = load_workbook('template/bicu.xlsx')
            svod.save(f"{static_path}\Сводная ведомость БИКУ.xlsx")
        svod = load_workbook(f"{static_path}\Сводная ведомость БИКУ.xlsx")
        svod_sheet = svod[str(month)]

        month_path = f"{static_path}\{MONTH_LIST[month - 1]}"

        for departement in os.listdir(month_path):
            try:
                file_name = list(filter(lambda x: "БИКУ" in x, os.listdir(f"{month_path}\{departement}")))[0]
                workbook = load_workbook(f'{month_path}\{departement}\{file_name}', read_only=True).worksheets[0]
                for row in workbook.iter_rows(min_row=8, values_only=True):
                    svod_sheet.append(row)
            except Exception as e:
                print(f"[INFO] Сформировать документ невозможно, Файл отсутсвует или не соответсвует синтаксису."
                      f"[INFO] Папка: {month_path}\{departement}")
                print(e)
        
        svod.save(f"{static_path}\Сводная ведомость БИКУ.xlsx")