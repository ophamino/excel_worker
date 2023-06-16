from logic.dirs_worker import tree_dir
from logic.file_worker import log
from logic.comparer import comparer, caluclater

import os


MONTH_LIST = [
    'Январь', 'Февраль', 'Март', 'Апрель',
    'Май', 'Июнь', 'Июль', 'Август',
    'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
]


def main():
    print("Здравствуйте!")
    action_list = [
        "Выберите действие, которое хотите совершить: ",
        "0. Выход из программы",
        "1. Создать базу данных для нового района",
        "2. Сверить все статические данные",
        "3. Сформировать сводную ведомость",
        "4. Сформировать расчетную ведомость",
    ]
    
    while True:
        print(*action_list, sep='\n')
        action_number = int(input())

        if action_number == 0:
            print("Вы вышли из программы. Всего хорошего!")
            break

        if action_number == 1:
            name = input('Введите название')
            tree_dir.create_new_tree_dir(name)
            print("Новая база данных создана!")

        if action_number == 2:
            log.add_changes_in_log()

        if action_number == 3:
            for number, month in enumerate(MONTH_LIST, 1):
                print(f'{number}. {month}')
            month = input('Введите номер месяца: ')
            print("1. Физическое лицо",
                  '2. Юридическое лицо', sep='\n')
            status = input("Выберите статус сводной ведомости: ")
            if status == "1":
                try:
                    comparer.comparer("FL", month)
                except Exception:
                    print('Введены неверные данные, повторите попытку.')
            if status == "2":
                comparer.comparer("UL", month)

        if action_number == 4:
            for number, month in enumerate(MONTH_LIST, 1):
                print(f'{number}. {month}')
            month = str(int(input('Введите номер месяца: ')) - 1)
            print("1. Физическое лицо",
                  '2. Юридическое лицо',
                  sep='\n')
            status = input("Выберите статус сводной ведомости: ")
            if status == "1":
                try:
                    caluclater.calculate("FL", month)
                except Exception:
                    print('Введены неверные данные, повторите попытку.')
            if status == "2":
                caluclater.calculate("UL", month)


if __name__ == "__main__":
    main()
