from logic.dirs_worker import tree_dir
from logic.file_worker import change_log
from logic.comparer import comparer, caluclater
from logic.const import MONTH_LIST, MAIN_DIR
from logic.comparer import bicu


def main():
    print()
    print("Welcome!")
    main_action = [
        "",
        f"----------------Меню---------------------------",
        "Выберите действие, которое хотите совершить: ",
        "1. Потребители",
        "2. БИКУ",
        "3. Отчеты"
        "________________________________________________"
        ""
    ]
    while True:
        print(*main_action, sep='\n')
        action = int(input("Выберите порядковый номер действия: "))
        
        if action == 1:
            pass
        if action == 2:
            pass
        if action == 3:
            pass
    
    while True:
        print(*subaction, sep='\n')
        action_number = int(input("Выберите порядковый номер действия: "))

        if action_number == 0:
            print("Вы вышли из программы. Всего хорошего!")
            break

        if action_number == 1:
            action = int(input())
            change_log(
                static=f'{MAIN_DIR}\Потребители\Реестр потребителей.xlsx', 
                change=f"./template/Реестр потребителей для сравнения.xlsx",
                upload_to=f'{MAIN_DIR}\Потребители\Журнал изменений.xlsx')

        if action_number == 2:
            for number, month in enumerate(MONTH_LIST, 1):
                print(f'{number}. {month}')
            month = int(input('Введите номер месяца: '))
            print("1. Бытовое потребление",
                  '2. Комерческое потребление', sep='\n')
            status = input("Выберите статус сводной ведомости: ")
            if status == "1":
                try:
                    comparer.comparer("Бытового", month)
                except Exception:
                    print('Введены неверные данные, повторите попытку.')
            if status == "2":
                comparer.comparer("Коммерческого", month)

        if action_number == 3:
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


if __name__ == "__main__":
    main()
    