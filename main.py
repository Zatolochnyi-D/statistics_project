from data_analyzer import DataAnalyzer
from data_picker import DataPicker
from file_parser import CsvFileParser

if __name__ == '__main__':
    # algorithm of assignment 1
    # read file with data
    parser = CsvFileParser()
    parser.read_file("udemy_courses_paid.csv")

    # select column
    # convert to floats
    data = [float(el) for el in parser.extract_column(5, True)]

    # pick 100 elements randomly
    picker = DataPicker(data)
    data = picker.pick_random(100)

    # put into analyzer and analyze
    # print results    
    analyzer = DataAnalyzer()
    print("Результат аналізу вибірки з реальних даних:")
    analyzer.set_data(data)
    print(analyzer.get_data_representation(10, 0))

    analyzer.analyze_data()
    print(analyzer.get_range())