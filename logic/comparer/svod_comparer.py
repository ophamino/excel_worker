from openpyxl import load_workbook
from datetime import datetime
import os


class Comparer:

    def __init__(self, main_dir: str) -> None:
        self.main_dir = main_dir
        self.svod_FL = f'SVOD{str(datetime.now().year)}FL.xlsx'
        self.svod_UL = f'SVOD{str(datetime.now().year)}UL.xlsx'

    def comparer(self):
        for folder in os.listdir(self.main_dir):
            static_path = f'{self.main_dir}/{folder}/{str(datetime.now().year)}/'
            svod_FL = load_workbook(f'{self.main_dir}/{folder}/{str(datetime.now().year)}/{self.svod_FL}')
            svod_UL = load_workbook(f'{self.main_dir}/{folder}/{str(datetime.now().year)}/{self.svod_UL}')

            if not str(datetime.now().month) in svod_FL:
                svod_FL.create_sheet(str(datetime.now().month))
            if not str(datetime.now().month) in svod_UL:
                svod_UL.create_sheet(str(datetime.now().month))

            svod_FL_sheet = svod_FL[str(datetime.now().month)]
            svod_UL_sheet = svod_UL[str(datetime.now().month)]

            for month in range(1, 12 + 1):
                month_path = static_path + str(month)
                for departement in os.listdir(month_path):
                    workbook_FL = load_workbook(f'{month_path}/{departement}/RV{str(datetime.now().year)}FL.xlsx').worksheets[0]
                    workbook_UL = load_workbook(f'{month_path}/{departement}/RV{str(datetime.now().year)}UL.xlsx').worksheets[0]

                    for row in workbook_FL.iter_rows(min_row=6, values_only=True):
                        svod_FL_sheet.append(row)
                    for row in workbook_UL.iter_rows(min_row=6, values_only=True):
                        svod_UL_sheet.append(row)

            svod_FL.save(f'{self.main_dir}/{folder}/{str(datetime.now().year)}/{self.svod_FL}')
            svod_UL.save(f'{self.main_dir}/{folder}/{str(datetime.now().year)}/{self.svod_UL}')


comparer = Comparer('../doc')
comparer.comparer()
