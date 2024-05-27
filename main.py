# from data_analyzer import DataAnalyzer
# from DataPicker import DataPicker
# from FileReader import CsvFileParser
from App import App

console_app = App()

if __name__ == '__main__':
    console_app.start()
    # # console_app.start()
    # # algorithm of assignment 1
    # # read file with data
    # file_path = "data.csv"
    # parser = CsvFileParser()
    # parser.read_file(file_path)

    # # select column and convert to floats
    # data = [float(el) for el in parser.extract_column(1, True)]

    # # pick 100 elements randomly
    # picker = DataPicker(data)
    # data = picker.pick_random(100)

    # # put into analyzer and analyze
    # # print results
    # analyzer = DataAnalyzer(data)
    # print("Результат аналізу вибірки з реальних даних:")
    # print(analyzer.get_data_representation_string(10))

    # analyzer.analyze_data()
    # print(analyzer.range)
    # print(analyzer.intervals_count)
    # print(analyzer.interval_size)

    # print(analyzer.intervals_table.get_table_representation())

    # print(f"Середнє: {analyzer.average}")
    # print(f"Дисперсія: {analyzer.dispersion}")
    # print(f"Середнє квадратичне відхилення: {analyzer.average_quadratic_deviation}")
    # print(f"Коефіцієнт варіації: {analyzer.variation_coeffitient}")
    # print(f"Коефіцієнт асиметрії: {analyzer.asymmetry_coeffitient}")
    # print(f"Ексцес: {analyzer.excess_coeefitient}")
    # print(f"Мода: {analyzer.mode}")
    # print(f"Медіана: {analyzer.median}")
    # print(f"Оцінка теоретичного середнього: {analyzer.t_average}")
    # print(f"Оцінка теоретичної дисперсії: {analyzer.t_dispersion}")
    # print(f"Парабола залежності: {analyzer.parabolic_parameters[0]}x^2 + {analyzer.parabolic_parameters[1]}x + {analyzer.parabolic_parameters[2]}")
    # print(f"Довірчий інтервал для середнього з надійністю 0.95: {analyzer.average_confidence_interval}")
    # print(f"Довірчий інтервал для дисперсії з надійністю 0.95: {analyzer.dispersion_confidence_interval}")
    # print("H0: a = 75, D = 49, H1: a = вибіркове середнє, D = =вибіркова дисперсія")
    # print("alpha = 0.05")
    # print(f"Гіпотеза про a = 75 є вірна: {not analyzer.hipothesis0_a_rejected}")
    # print(f"Гіпотеза про D = 49 є вірна: {not analyzer.hipothesis0_D_rejected}")
    # print(f"Критична область для середнього: {analyzer.average_crit}")
    # print(f"Потужність критерію для середнього: {analyzer.a_criteria_power}")
    # print(f"Критична область для дисперсії: {analyzer.d_crit}")
    # print(f"Потрібна n для alpha = 0.01, beta = 0.025: {analyzer.required_length}")
    # print(f"З alpha = 0.05 є N(75, 49): {analyzer.is_normal_dist}")
    # analyzer.show_plot()
    # print()
    # print()
    # print()

    # data2 = [float(el) for el in parser.extract_column(2, True)]

    #  # pick 100 elements randomly
    # picker2 = DataPicker(data2)
    # data2 = picker2.pick_random(100)

    # # put into analyzer and analyze
    # # print results
    # analyzer2 = DataAnalyzer(data2)
    # print("Результат аналізу вибірки з реальних даних:")
    # print(analyzer2.get_data_representation_string(10))

    # analyzer2.analyze_data()
    # print(analyzer2.range)
    # print(analyzer2.intervals_count)
    # print(analyzer2.interval_size)

    # print(analyzer2.intervals_table.get_table_representation())

    # print(f"Середнє: {analyzer2.average}")
    # print(f"Дисперсія: {analyzer2.dispersion}")
    # print(f"Середнє квадратичне відхилення: {analyzer2.average_quadratic_deviation}")
    # print(f"Коефіцієнт варіації: {analyzer2.variation_coeffitient}")
    # print(f"Коефіцієнт асиметрії: {analyzer2.asymmetry_coeffitient}")
    # print(f"Ексцес: {analyzer2.excess_coeefitient}")
    # print(f"Мода: {analyzer2.mode}")
    # print(f"Медіана: {analyzer2.median}")
    # print(f"Оцінка теоретичного середнього: {analyzer2.t_average}")
    # print(f"Оцінка теоретичної дисперсії: {analyzer2.t_dispersion}")
    # print(f"Парабола залежності: {analyzer2.parabolic_parameters[0]}x^2 + {analyzer.parabolic_parameters[1]}x + {analyzer.parabolic_parameters[2]}")
    # print(f"Довірчий інтервал для середнього з надійністю 0.95: {analyzer2.average_confidence_interval}")
    # print(f"Довірчий інтервал для дисперсії з надійністю 0.95: {analyzer2.dispersion_confidence_interval}")
    # print("H0: a = 75, D = 49, H1: a = вибіркове середнє, D = =вибіркова дисперсія")
    # print("alpha = 0.05")
    # print(f"Гіпотеза про a = 75 є вірна: {not analyzer2.hipothesis0_a_rejected}")
    # print(f"Гіпотеза про D = 49 є вірна: {not analyzer2.hipothesis0_D_rejected}")
    # print(f"Критична область для середнього: {analyzer2.average_crit}")
    # print(f"Потужність критерію для середнього: {analyzer2.a_criteria_power}")
    # print(f"Критична область для дисперсії: {analyzer2.d_crit}")
    # print(f"Потрібна n для alpha = 0.01, beta = 0.025: {analyzer2.required_length}")
    # print(f"З alpha = 0.05 є N(75, 49): {analyzer2.is_normal_dist}")
    # analyzer2.show_plot()
