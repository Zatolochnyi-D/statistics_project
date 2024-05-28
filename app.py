import os
from FileReader import CsvFileReader
from DataPicker import DataPicker
from GeneralAnalyzer import GeneralAnalyzer

# Console application. Handles input/output.
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
    
    def pause(self) -> None:
        input('Натисніть "Enter" щоб продовжити...')

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
        print("Обирані 100 значень випадковим чином.")
        picker = DataPicker(reader.extract_number_column(1, False))
        general_analyzer = GeneralAnalyzer(picker.pick_random(100))
        print("Ранжована вибірка:")
        print(general_analyzer.get_data_representation_string(10))
        print()

        print("Знайдені інтервальні параметри.")   
        general_analyzer.find_interval_parameters()
        print(f"Розмах: {general_analyzer.range}")
        print(f"Кількість інтервалів: {general_analyzer.intervals_count}")
        print(f"Розмір одного інтервалу: {general_analyzer.interval_size}")
        print()

        print(f"Таблиця інтервального статистичного розподілу:")
        general_analyzer.build_intervals_table()
        print(general_analyzer.intervals_table.get_table_representation())
        print()

        print("Графіки виведені окремо.")
        general_analyzer.plot_graphics()
        general_analyzer.plots.show()
        print("Характеристики:")
        general_analyzer.find_characteristics()
        print(f"Середнє: a = {general_analyzer.average}")
        print(f"Дисперсія: s² = {general_analyzer.dispersion}")
        print(f"Середнє квадратичне відхилення: s = {general_analyzer.std}")
        # print(f"Моди: Mo1 = {general_analyzer.mode}")
        print(f"Моди: {str.join(" ", [f"Mo{i + 1} = {mode}" for i, mode in enumerate(general_analyzer.modes)])}")
        print(f"Медіана: Me = {general_analyzer.median}")
        print(f"Коефіцієнт варіації: v = {round(general_analyzer.variation * 100, 2)}%")
        print()

        print("Висновок:")
        if general_analyzer.variation < .1:
            print("Мінливість вибірки є незначною.")
        elif general_analyzer.variation < .25:
            print("Мінливість вибірки є середньою.")
        else:
            print("Мінливість вибірки є значною. Можливі неточності.")
        print()
        self.pause()


    def run_manual_scenario(self) -> None:
        self.clear()