from openpyxl import load_workbook
from datetime import datetime
import os


class Comparer:

    def __init__(self, main_dir: str) -> None:
        self.main_dir = main_dir

    def comparer(self, file_status: str, month: str) -> None:
        for folder in os.listdir(self.main_dir):
            static_path = f'{self.main_dir}/{folder}/{str(datetime.now().year)}/'
            svod = load_workbook('template/svod.xlsx')
            if month not in svod.sheetnames:
                svod.create_sheet(month)

            svod_sheet = svod[month]
            month_path = static_path + month
            for departement in os.listdir(month_path):
                workbook = load_workbook(f'{month_path}/{departement}/RV{str(datetime.now().year)}{file_status}.xlsx').worksheets[0]
                for row in workbook.iter_rows(min_row=11, values_only=True):
                    svod_sheet.append(row)

            svod.save(f'{self.main_dir}/{folder}/{str(datetime.now().year)}/SVOD{str(datetime.now().year)}{file_status}.xlsx')
