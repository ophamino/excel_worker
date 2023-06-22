from openpyxl import load_workbook
import os
from datetime import datetime


class Calculation:

    def __init__(self, main_dir) -> None:
        self.main_dir = main_dir

    def calculate(self, file_status: str, month: str) -> None:
        static_file = load_workbook(f'{self.main_dir}\Потребители\Реестр статических данных.xslx').worksheets[0]
        svod = load_workbook(f'{self.main_dir}\Сводный баланс\{str(datetime.now().year)}\УПП\Сводная ведомость {file_status} потребления.xlsx')[month]
        result = load_workbook('template\\rv.xlsx')
        result_sheet = result.worksheets[0]

        for row_svod in range(6, svod.max_row + 1):
            for row_static in range(9, static_file.max_row + 1):
                if svod.cell(row=row_svod, column=3).value == static_file.cell(row=row_static, column=3).value:
                    result_sheet.append(
                        [
                            1,  # A
                            static_file.cell(row=row_static, column=2).value,  # B
                            static_file.cell(row=row_static, column=3).value,  # C
                            static_file.cell(row=row_static, column=4).value,  # D
                            static_file.cell(row=row_static, column=5).value,  # E
                            static_file.cell(row=row_static, column=6).value,  # F
                            static_file.cell(row=row_static, column=7).value,  # G
                            static_file.cell(row=row_static, column=8).value,  # H
                            static_file.cell(row=row_static, column=11).value,  # I
                            static_file.cell(row=row_static, column=12).value,  # J
                            static_file.cell(row=row_static, column=13).value,  # K
                            static_file.cell(row=row_static, column=19).value,  # L
                            static_file.cell(row=row_static, column=20).value,  # M
                            static_file.cell(row=row_static, column=21).value,  # N
                            static_file.cell(row=row_static, column=22).value,  # O
                            static_file.cell(row=row_static, column=23).value,  # P
                            static_file.cell(row=row_static, column=26).value,  # Q
                            static_file.cell(row=row_static, column=27).value,  # R
                            static_file.cell(row=row_static, column=28).value,  # S
                            static_file.cell(row=row_static, column=29).value,  # T
                            svod.cell(row=row_svod, column=22).value,  # u
                            svod.cell(row=row_svod, column=22).value,  # v
                            svod.cell(row=row_svod, column=23).value,  # w
                            svod.cell(row=row_svod, column=24).value,  # x
                            svod.cell(row=row_svod, column=25).value,  # y
                            svod.cell(row=row_svod, column=26).value,  # z
                            svod.cell(row=row_svod, column=27).value,  # aa
                            svod.cell(row=row_svod, column=28).value,  # ab
                            svod.cell(row=row_svod, column=29).value,  # ac
                            svod.cell(row=row_svod, column=30).value,  # ad
                            '',  # ae
                            svod.cell(row=row_svod, column=32).value,  # af
                            svod.cell(row=row_svod, column=33).value,  # ag
                            svod.cell(row=row_svod, column=34).value,  # ah
                            svod.cell(row=row_svod, column=35).value,  # ai
                            svod.cell(row=row_svod, column=36).value,  # aj
                            svod.cell(row=row_svod, column=37).value,  # ak
                            "",  # al
                            '',  # am
                            svod.cell(row=row_svod, column=38).value,  # an
                            svod.cell(row=row_svod, column=39).value,  # ao
                        ]
                    )
                    break

        for num in range(1, 6):
            data = []
            for row in range(6, result_sheet.max_row + 1):
                if result_sheet.cell(row=row, column=2).value == num or result_sheet.cell(row=row, column=2).value == f"'0{num}" or result_sheet.cell(row=row, column=2).value == f"'{num}" or result_sheet.cell(row=row, column=2).value == f"0{num}":
                    data.append([result_sheet.cell(row=row, column=i).value for i in range(1, result_sheet.max_column + 1)])

            workbook = load_workbook('.\template\rv.xlsx')
            workshhet = workbook.worksheets[0]
            for i in data:
                workshhet.append(i)

            workbook.save(f'..\doc\DS\{datetime.now().year}\{datetime.now().month + 1}\DS0{num}01\DS0{num}01-{datetime.now().year}-{datetime.now().month}-{file_status}.xlsx')
