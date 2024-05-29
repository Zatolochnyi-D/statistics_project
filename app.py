import os
from FileReader import CsvFileReader
from DataPicker import DataPicker
from Analyzers import *

# Console application. Handles input/output.
class App:

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
        self.run_test_scenario()

    def start2(self) -> None:
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

        print('Читаємо файл "data.csv".')
        file_path = "data.csv"
        reader = CsvFileReader()
        reader.read_file(file_path)
        print("Перші 5 рядків файла:")
        print(reader.peek_first_rows(5))
        print()

        print("Обрані дані - час роботи алгоритму.")
        print("Обрані 100 значень рівномірно.")
        picker = DataPicker(reader.extract_number_column(1, False))
        general_analyzer = GeneralAnalyzer(picker.pick_even(100))
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
        print()

        print("Аналіз продовжено як для нормального розподілу.")
        normal_analyzer = general_analyzer.get_concrete_analyzer(0)
        print("Методом максимальної правдоподібності знайдені наступні параметри розподілу:")
        normal_analyzer.find_parameters_estimation()
        print(f"Оцінка середнього: {normal_analyzer.estimate_average}")
        print(f"Оцінка середнього квадратичного відхилення: {normal_analyzer.estimate_std}")
        print()

        print("Для пошуку теоретичної залежності між значеннями та частістю використана парабола (оскільки розподіл нормальний).")
        print("Знайдена парабола:")
        normal_analyzer.find_possible_dependence()
        print("y = {}x^2 + {}x + {}".format(*normal_analyzer.possible_dependence_parameteres))

        print("Довірчі інтервали з довірчою ймовірністю 𝜸 = 0.95:")
        normal_analyzer.find_confidence_intervals(0.95)
        print("Для генерального середнього: [{}, {}]".format(*normal_analyzer.average_confidence_interval))
        print("Для генеральної дисперсії: [{}, {}]".format(*normal_analyzer.dispersion_confidence_interval))
        print()

        print("Гіпотеза про значення середнього.")
        print("H0: a = 75.")
        print(f"H1: a = {general_analyzer.average} (тобто отримане середнє).")
        print("Перевірка відбувається на рівні значущості 𝛼 = 0.05.")
        normal_analyzer.test_parameter_hypothesis(0.05, 75)
        print()

        print(f"Гіпотеза H0{"" if normal_analyzer.hipothesis0_parameter_rejected else " не"} відкинута на рівні значущості 𝛼 = 0.05.")
        print("Критична область: ({}, {})".format(*normal_analyzer.average_critical_range))
        print(f"Потужність критерію: {normal_analyzer.average_criteria_power}")
        print()

        print("Знайдемо обсяг вибірки, потрібної для перевірки із заданими 𝛼 = 0.05 𝛽 = 0.025:")
        normal_analyzer.find_n_from_alpha_and_beta(75, 0.05, 0.025)
        print(f"Необхідний обсяг вибірки: {normal_analyzer.required_n}")

        print("Перевіримо гіпотезу про закон розподілу генеральної сукупності.")
        print("H0: N(a, 𝜎²) ---> N(75, 49)")
        print("H1: N(a, 𝜎²) -/-> N(75, 49)")
        print("Перевірка відбувається на рівні значущості 𝛼 = 0.05.")
        normal_analyzer.test_for_normal_distribution(75, 49, 0.05)
        print()

        print(f"Гіпотеза H0{" не" if normal_analyzer.is_normal_dist else ""} відкинута на рівні значущості 𝛼 = 0.05.")
        print()
        self.pause()
        print()

        print("Другі обрані дані - довжина аудіозапису.")
        print("Обрані 100 значень рівномірно.")
        picker2 = DataPicker(reader.extract_number_column(2, False))
        general_analyzer2 = GeneralAnalyzer(picker2.pick_even(100))
        print("Ранжована вибірка:")
        print(general_analyzer2.get_data_representation_string(10))
        print()

        print("Знайдені інтервальні параметри.")   
        general_analyzer2.find_interval_parameters()
        print(f"Розмах: {general_analyzer2.range}")
        print(f"Кількість інтервалів: {general_analyzer2.intervals_count}")
        print(f"Розмір одного інтервалу: {general_analyzer2.interval_size}")
        print()

        print(f"Таблиця інтервального статистичного розподілу:")
        general_analyzer2.build_intervals_table()
        print(general_analyzer2.intervals_table.get_table_representation())
        print()

        print("Графіки виведені окремо.")
        general_analyzer2.plot_graphics()
        general_analyzer2.plots.show()
        print("Характеристики:")
        general_analyzer2.find_characteristics()
        print(f"Середнє: a = {general_analyzer2.average}")
        print(f"Дисперсія: s² = {general_analyzer2.dispersion}")
        print(f"Середнє квадратичне відхилення: s = {general_analyzer2.std}")
        print(f"Моди: {str.join(" ", [f"Mo{i + 1} = {mode}" for i, mode in enumerate(general_analyzer2.modes)])}")
        print(f"Медіана: Me = {general_analyzer2.median}")
        print(f"Коефіцієнт варіації: v = {round(general_analyzer2.variation * 100, 2)}%")
        print()

        print("Висновок:")
        if general_analyzer2.variation < .1:
            print("Мінливість вибірки є незначною.")
        elif general_analyzer2.variation < .25:
            print("Мінливість вибірки є середньою.")
        else:
            print("Мінливість вибірки є значною. Можливі неточності.")
        print()
        self.pause()
        print()

        print("Складемо двовимірну таблицю:")
        correlation_analyzer = CorrelationAnalyzer(general_analyzer, general_analyzer2)
        correlation_analyzer.build_2d_table()
        print(correlation_analyzer.get_table_representation())

    def run_manual_scenario(self) -> None:
        self.clear()