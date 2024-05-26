from data_analyzer import DataAnalyzer
from data_picker import DataPicker
from file_parser import CsvFileParser
from app import App

console_app = App()

if __name__ == '__main__':
    # console_app.start()
    # algorithm of assignment 1
    # read file with data
    file_path = "data.csv"
    parser = CsvFileParser()
    parser.read_file(file_path)

    # select column and convert to floats
    data = [float(el) for el in parser.extract_column(1, True)]

    # pick 100 elements randomly
    picker = DataPicker(data)
    data = picker.pick_random(100)

    # put into analyzer and analyze
    # print results
    analyzer = DataAnalyzer(data)
    print("Результат аналізу вибірки з реальних даних:")
    print(analyzer.get_data_representation_string(10))

    analyzer.analyze_data()
    print(analyzer.range)
    print(analyzer.intervals_count)
    print(analyzer.interval_size)

    print(analyzer.intervals_table.get_table_representation())

    print(f"Середнє: {analyzer.average}")
    print(f"Дисперсія: {analyzer.dispersion}")
    print(f"Середнє квадратичне відхилення: {analyzer.average_quadratic_deviation}")
    print(f"Коефіцієнт варіації: {analyzer.variation_coeffitient}")
    print(f"Коефіцієнт асиметрії: {analyzer.asymmetry_coeffitient}")
    print(f"Ексцес: {analyzer.excess_coeefitient}")
    print(f"Мода: {analyzer.mode}")
    print(f"Медіана: {analyzer.median}")
    print(f"Оцінка теоретичного середнього: {analyzer.t_average}")
    print(f"Оцінка теоретичної дисперсії: {analyzer.t_dispersion}")
    print(f"Парабола залежності: {analyzer.parabolic_parameters[0]}x^2 + {analyzer.parabolic_parameters[1]}x + {analyzer.parabolic_parameters[2]}")
    print(f"Довірчий інтервал для середнього з надійністю 0.95: {analyzer.average_confidence_interval}")
    print(f"Довірчий інтервал для дисперсії з надійністю 0.95: {analyzer.dispersion_confidence_interval}")
    print("H0: a = 75, D = 49, H1: a = вибіркове середнє, D = =вибіркова дисперсія")
    print("alpha = 0.05")
    print(f"Гіпотеза про a = 75 є вірна: {not analyzer.hipothesis0_a_rejected}")
    print(f"Гіпотеза про D = 49 є вірна: {not analyzer.hipothesis0_D_rejected}")
    print(f"Критична область для середнього: {analyzer.average_crit}")
    print(f"Потужність критерію для середнього: {analyzer.a_criteria_power}")
    print(f"Критична область для дисперсії: {analyzer.d_crit}")
    analyzer.show_plot()