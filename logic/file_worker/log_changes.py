import os
from datetime import datetime

from openpyxl import load_workbook

from logic.const import MAIN_DIR


class Log:

    def __init__(self) -> None:
        self.static_file_name = 'Реестр статических данных.xlsx'
        self.changes_file_name = 'Реестр статических данных для сравнения.xlsx'
        self.log_file_name = 'Журнал изменений.xlsx'

        self.static_file = load_workbook(f'{MAIN_DIR}\Потребители\{self.static_file_name}')
        self.changes_file = load_workbook(f"./template/{self.changes_file_name}")

        self.static_file_sheet = self.static_file.worksheets[0]
        self.changes_file_sheet = self.changes_file.worksheets[0]

        self.date = datetime.now().date()
        self.time = datetime.now().time().replace(microsecond=0, minute=0)

    def get_status_data(self, identifiers: list, status: str) -> None:
        status_data = []
        if identifiers:
            for item in identifiers:
                status_data.append([1, item, '', '', '', '', status, self.date, self.time])
        return status_data

    def get_changes_data(self, static_row: int, changes_row: int):
        changes = []
        for column in range(2, self.static_file_sheet.max_column + 1):
            if self.static_file_sheet.cell(row=static_row, column=column).value != self.changes_file_sheet.cell(row=changes_row, column=column).value:
                changes.append(
                    [
                        1,
                        self.static_file_sheet.cell(row=changes_row, column=3).value,
                        self.static_file_sheet.cell(row=4, column=column).value,
                        self.changes_file_sheet.cell(row=changes_row, column=column).coordinate,
                        self.changes_file_sheet.cell(row=changes_row, column=column).value,
                        self.static_file_sheet.cell(row=static_row, column=column).value,
                        'Изменено',
                        self.date,
                        self.time
                    ]
                )

        return changes

    def search_changes(self) -> list:
        changes_data = []
        for row_static in range(9, self.static_file_sheet.max_row + 1):
            for row_changes in range(9, self.changes_file_sheet.max_row + 1):
                if self.static_file_sheet.cell(row=row_static, column=4).value == self.changes_file_sheet.cell(row=row_changes, column=4).value:
                    change = self.get_changes_data(row_static, row_changes)
                    changes_data = changes_data + change
                    break
        return changes_data

    def append_data_in_log(self, data: list[str]) -> None:
        if self.log_file_name not in os.listdir(f'{MAIN_DIR}\Потребители'):
            log_file = load_workbook("./template/log.xlsx").save(f'{MAIN_DIR}\Потребители\{self.log_file_name}')
        log_file = load_workbook(f'{MAIN_DIR}\Потребители\{self.log_file_name}')

        if not str(self.date) in log_file.sheetnames:
            log_file.create_sheet(str(self.date.year))
        log_sheet = log_file[str(self.date.year)]

        for log_data in data:
            log_sheet.append(log_data)
        log_file.save(f'{MAIN_DIR}\Потребители\{self.log_file_name}')

    def change_log(self):
        changes_ID = set([self.static_file_sheet.cell(row=i, column=3).value for i in range(9, self.static_file_sheet.max_row + 1)])
        static_ID = set([self.changes_file_sheet.cell(row=i, column=3).value for i in range(9, self.changes_file_sheet.max_row + 1)])

        added_ids = list(static_ID.difference(changes_ID))
        deleted_ids = list(changes_ID.difference(static_ID))

        changes_data = self.search_changes()
        added_data = self.get_status_data(added_ids, status="Добавлено")
        deleted_data = self.get_status_data(deleted_ids, status="Удалено")

        all_data = changes_data + added_data + deleted_data
        self.append_data_in_log(all_data)

        self.static_file.save(f"./template/{self.changes_file_name}")
