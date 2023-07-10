from .const import MAIN_DIR, MONTH_LIST
from .file_worker.log import change_log
from .comparer.bicu import comparer, calculate


def start_bicu():
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
        if action == 1:
            change_log()
        if action == 2:
            for number, month in enumerate(MONTH_LIST, 1):
                print(f'{number}. {month}')
            month = int(input('Введите номер месяца:  ')) - 1
            comparer(month)
        if action == 3:
            for number, month in enumerate(MONTH_LIST, 1):
                print(f'{number}. {month}')
            month = int(input('Введите номер месяца:  ')) - 1
            calculate(month)
        break