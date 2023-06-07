import os
from datetime import datetime

from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.worksheet import Worksheet


class LogChanges:
    """Класс журнала изменений"""

    def __init__(self, dir_name: str) -> None:
        self.dir_name = dir_name
        self.static_file_name = 'static.xlsx'
        self.static_file_without_changes_name = 'static_without_changes.xlsx'
        self.log_file_name = 'log.xlsx'

    def __compare_cells(self, static_sheet: Worksheet, changes_sheet: Worksheet) -> list[str]:
        """Функция для сранения значений"""
        data = []

        static_identifiers = set([static_sheet.cell(row=i, column=3).value for i in range(9, static_sheet.max_row + 1)])
        changes_identifiers = set([changes_sheet.cell(row=i, column=3).value for i in range(9, changes_sheet.max_row + 1)])

        added_identifiers = list(static_identifiers.difference(changes_identifiers))
        deleted_identifiers = list(changes_identifiers.difference(static_identifiers))

        for row_static in range(9, static_sheet.max_row + 1):
            for row_changes in range(9, changes_sheet.max_row + 1):
                if static_sheet.cell(row=row_static, column=3).value == changes_sheet.cell(row=row_changes, column=3).value:
                    for column in range(2, static_sheet.max_column + 1):
                        if static_sheet.cell(row=row_static, column=column).value != changes_sheet.cell(row=row_changes, column=column).value:
                            data.append(
                                [
                                    1,
                                    static_sheet.cell(row=row_changes, column=3).value,
                                    static_sheet.cell(row=4, column=column).value,
                                    changes_sheet.cell(row=row_changes, column=column).coordinate,
                                    changes_sheet.cell(row=row_changes, column=column).value,
                                    static_sheet.cell(row=row_static, column=column).value,
                                    'Изменено',
                                    datetime.now().date(),
                                    datetime.now().time().replace(microsecond=0, minute=0)
                                ]
                            )
                    break

        for item in deleted_identifiers:
            data.append(
                [1,
                 item,
                 '',
                 '',
                 '',
                 '',
                 "Удалено",
                 datetime.now().date(),
                 datetime.now().time().replace(microsecond=0, minute=0)
                 ]
            )
        for item in added_identifiers:
            data.append(
                [1,
                 item,
                 '',
                 '',
                 '',
                 '',
                 "",
                 datetime.now().date(),
                 datetime.now().time().replace(microsecond=0, minute=0)
                 ]
            )
        return data

    def __rewrite_log_in_folder(self, folder: str, data: list[str]) -> None:
        """Перезапись жарнула в директории"""

        if self.log_file_name not in os.listdir(f'{self.dir_name}/{folder}'):
            log_file = load_workbook("template/log.xlsx")
            log_file.save(f'{self.dir_name}/{folder}/{self.log_file_name}')
        log_file = load_workbook(f'{self.dir_name}/{folder}/{self.log_file_name}')

        if not str(datetime.now().year) in log_file.sheetnames:
            log_file.create_sheet(str(datetime.now().year))
        log_sheet = log_file[str(datetime.now().year)]

        for log_data in data:
            log_sheet.append(log_data)
        log_file.save(f'{self.dir_name}/{folder}/{self.log_file_name}')

    def add_changes_in_log(self) -> None:
        """Функция для записи изменений в журнал"""
        for folder in os.listdir(self.dir_name):

            static_file = load_workbook(f'{self.dir_name}/{folder}/{self.static_file_name}')
            static_file_without_changes = load_workbook(f'{self.dir_name}/{folder}/{self.static_file_without_changes_name}')
            static_sheet = static_file[str(datetime.now().year)]
            changes_sheet = static_file_without_changes[str(datetime.now().year)]

            self.__rewrite_log_in_folder(folder=folder,
                                         data=self.__compare_cells(static_sheet=static_sheet,
                                                                   changes_sheet=changes_sheet))

        static_file.save(f'{self.dir_name}/{folder}/{self.static_file_without_changes_name}')
