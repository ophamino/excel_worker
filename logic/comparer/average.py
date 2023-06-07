import os

from openpyxl import load_workbook


class Avarage:

    def get_data(self):
        for folder in os.listdir('../group'):
            hashtable = dict()
            for file in os.listdir(f'../group/{folder}'):
                workbook = load_workbook(f"../group/{folder}/{file}", data_only=True)
                worksheet = workbook.worksheets[0]
                for row in range(9, worksheet.max_row + 1):
                    cell = worksheet.cell(row=row, column=7).value
                    if cell is None:
                        continue
                    if cell not in hashtable.keys():
                        hashtable[cell] = []
                    if worksheet.cell(row=row, column=10).value != 0 or worksheet.cell(row=row, column=10).value != '0':
                        hashtable[cell].append(worksheet.cell(row=row, column=10).value)


test = Avarage()

test.get_data()
