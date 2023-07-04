from logic.dirs_worker import tree_dir
from logic.file_worker import change_log
from logic.comparer import comparer, caluclater
from logic.const import MONTH_LIST


def main():
    print()
    print("Welcome!")
    action_list = [
        "",
        "----------------Меню---------------------------",
        "Выберите действие, которое хотите совершить: ",
        "0. Выход из программы",
        "1. Сверить статические данные Реестра потребителей",
        "2. Сформировать сводную ведомость",
        "3. Сформировать расчетную ведомость",
        "4. Сформировать отчет гп",
        "________________________________________________"
        ""
    ]
    
    while True:
        print(*action_list, sep='\n')
        action_number = int(input("Выберите порядковый номер действия: "))

        if action_number == 0:
            print("Вы вышли из программы. Всего хорошего!")
            break

        if action_number == 1:
            change_log()

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

