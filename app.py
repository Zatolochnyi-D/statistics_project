import os

class App:
    def __init__(self) -> None:
        pass

    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self) -> None:
        self.clear()

        print("###########################################")
        print("#                                         #")
        print("#    Оберіть опцію:                       #")
        print("#    1 - Використати тестовий сценарій    #")
        print("#    2 - Використати ручний сценарій      #")
        print("#    3 - Вийти                            #")
        print("#                                         #")
        print("###########################################")
        
        while True:
            option = input("Ведіть потрібну опцію: ")
            try:
                final_option = int(option)
            except ValueError:
                print("Неправильний ввід, спробуйте ще раз.")
                print()
                continue
            if final_option not in [1, 2, 3]:
                print("Оберіть опцію зі списку.")
                print()
                continue
            break

        if final_option == 1:
            self.run_test_scenario()
        elif final_option == 2:
            self.run_manual_scenario()
        elif final_option == 3:
            exit()

    def run_test_scenario(self) -> None:
        self.clear()

    def run_manual_scenario(self) -> None:
        self.clear()