from openpyxl import load_workbook, Workbook
import os
from datetime import datetime


class Log:

    def __init__(self, dir_name: str) -> None:
        self.dir_name = dir_name
        self.static_file_name = 'static.xlsx'
        self.static_file_without_changes_name = 'static_without_changes.xlsx'
        self.log_file_name = 'log.xlsx'

    def compare_cells(self):
        for folder in os.listdir(self.dir_name):
            data = []
            static_file = load_workbook(f'{self.dir_name}/{folder}/{self.static_file_name}')
            static_file_without_changes = load_workbook(f'{self.dir_name}/{folder}/{self.static_file_without_changes_name}')

            static_sheet = static_file[str(datetime.now().year)]
            changes_sheet = static_file_without_changes[str(datetime.now().year)]

            for row in range(1, static_sheet.max_row + 1):
                for col in range(1, static_sheet.max_column + 1):
                    if static_sheet.cell(row=row, column=col).value != changes_sheet.cell(row=row, column=col).value:
                        data.append(
                            [1,
                            static_sheet.cell(row=row, column=2).value,
                            static_sheet.cell(row=4, column=col).value,
                            static_sheet.cell(row=row, column=col).coordinate,
                            static_sheet.cell(row=row, column=col).value,
                            changes_sheet.cell(row=row, column=col).value,
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                        )
            log_file = static_file_without_changes = load_workbook(f'{self.dir_name}/{folder}/{self.log_file_name}')
            if not str(datetime.now().year) in log_file.sheetnames:
                log_file.create_sheet(str(datetime.now().year))
            log_sheet = log_file[str(datetime.now().year)]
            for log_data in data:
                log_sheet.append(log_data)
            # log_file.remove_sheet[0]
            log_file
            log_file.save(f'{self.dir_name}/{folder}/{self.log_file_name}')
        static_file_without_changes.save(f'{self.dir_name}/{folder}/{self.static_file_name}')


log = Log('../doc').compare_cells()
print(os.listdir('../'))
