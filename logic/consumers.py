from .file_worker import change_log
from .const import MAIN_DIR, MONTH_LIST
from .comparer import comparer, caluclater


def start_consumer():
    menu = [
         "",
        "----------------Потребители-------------------",
        "Выберите действие, которое хотите совершить: ",
        "1. Сверить статические данные",
        "2. Сформировать сводную ведомость",
        "3. Сформировать расчетную ведомость",
        "0. Главное меню",
        "________________________________________________",
        ""
    ]
    print(*menu, sep='\n')
    action = int(input("Выберите порядковый номер действия: " ))
    while True:
        if action == 0:
            print("Вы вышли из программы. Всего хорошего!")
            break
        if action == 1:
            change_log()
        if action == 2:
            for number, month in enumerate(MONTH_LIST, 1):
                print(f'{number}. {month}')
            month = int(input('Введите номер месяца: '))
            print("1. Бытовое потребление",
                  '2. Комерческое потребление',
                  "3. Общая",
                  sep='\n')
            status = input("Выберите статус сводной ведомости: ")
            if status == "1":
                try:
                    comparer.comparer("Бытового", month)
                except Exception:
                    print('Введены неверные данные, повторите попытку.')
            if status == "2":
                comparer.comparer("Коммерческого", month)
            if status == "3":
                comparer.total_comparer(month)
        if action == 3:
            for number, month in enumerate(MONTH_LIST, 1):
                print(f'{number}. {month}')
            month = int(input('Введите номер месяца:  ')) - 1
            print("1. Бытовое потребление",
                  '2. Комерческое потребление',
                  sep='\n')
            status = input("Выберите статус сводной ведомости: ")
            if status == "1":
                try:
                    caluclater.calculate("Бытового", month)
                except Exception:
                    print('Введены неверные данные, повторите попытку.')
            if status == "2":
                caluclater.calculate("Коммерческого", month)
        break
