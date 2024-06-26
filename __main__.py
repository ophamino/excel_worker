from logic.consumers import start_consumer
from logic.start_bicu import start_bicu
from logic.analytics.balance import BalanceAnalytics


balance = BalanceAnalytics()
balance.create_analytics(6)


def main():
    print()
    print("Welcome!")
    main_action = [
        "",
        "----------------Меню---------------------------",
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
            start_consumer()
        if action == 2:
            start_bicu()
        if action == 3:
            pass


if __name__ == "__main__":
    main()
    