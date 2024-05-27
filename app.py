import os
from FileReader import CsvFileReader
from DataPicker import DataPicker
from GeneralAnalyzer import GeneralAnalyzer

class App:
    def __init__(self) -> None:
        pass

    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def request_int_input(self, tip: str, available_options: list[int]) -> int:
        while True:
            user_input = input(tip)
            try:
                selected_option = int(user_input)
            except ValueError:
                print("Неправильний ввід, спробуйте ще раз.")
                print()
                continue
            if selected_option not in available_options:
                print("Оберіть опцію зі списку.")
                print()
                continue
            break
        return selected_option

    def start(self) -> None:
        self.clear()

        print("Оберіть опцію:")
        print("1 - Використати тестовий сценарій")
        print("2 - Використати ручний сценарій")
        print("3 - Вийти")
        print()
        
        selected_option = self.request_int_input("Ведіть потрібну опцію: ", [1, 2, 3])
        if selected_option == 1:
            self.run_test_scenario()
        elif selected_option == 2:
            self.run_manual_scenario()
        elif selected_option == 3:
            exit()

    def run_test_scenario(self) -> None:
        self.clear()

        # Assume unknown data is read. Then not all columns have consistent type and there may be no float columns to analyze.
        # Possible problems:
        # - Inconsistent types in columns
        # - No columns with floats
        # - Table have less than 5 columns
        print('Читаємо файл "data.csv".')
        file_path = "data.csv"
        reader = CsvFileReader()
        reader.read_file(file_path)
        print("Перші 5 рядків файла:")
        print(reader.peek_first_rows(5))
        print()

        print("Обрані дані - час роботи алгоритму.")
        print("Обираємо 100 значень випадковим чином.")
        picker = DataPicker(reader.extract_number_column(1, False))
        general_analyzer = GeneralAnalyzer(picker.pick_random(100))
        print("Ранжована вибірка:")
        print(general_analyzer.get_data_representation_string(10))
        print()
                



    def run_manual_scenario(self) -> None:
        self.clear()
        exit()