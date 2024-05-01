from data_analyzer import DataAnalyzer
from data_picker import DataPicker
from file_parser import CsvFileParser
import random as r

if __name__ == '__main__':
    # algorithm of assignment 1
    # read file with data
    parser = CsvFileParser()
    parser.read_file("udemy_courses_paid.csv")

    # select column
    # convert to floats
    data = [float(el) for el in parser.extract_column(4, True)]

    # pick 100 elements randomly
    # put into analyzer and analyze
    picker = DataPicker(data)
    analyzer = DataAnalyzer()
    analyzer.set_data(picker.pick_random(100))
    analyzer.analyze_data()

    # print results    
    print("Результат аналізу вибірки з реальних даних:")
    print(analyzer.get_data_representation(10, 1))
    print(analyzer.get_range())

    # repeat with made up data
    print("Результат аналізу вибірки нормального розподілу:")
    data = sorted([round(r.normalvariate() * 9.0, 5) for i in range(100)])
    analyzer.set_data(data)
    analyzer.analyze_data()
    print(analyzer.get_data_representation(10, 5))
    print(analyzer.get_range())