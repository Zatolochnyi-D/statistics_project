from data_analyzer import DataAnalyzer
from data_picker import DataPicker
from file_parser import CsvFileParser

if __name__ == '__main__':
    # step 1
    # select file
    # read file
    # select column
    # pick values randomly

    # step 2
    # analyze


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
    print(analyzer.get_data_representation_string(10, 1))

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
    analyzer.plot_graphics()
