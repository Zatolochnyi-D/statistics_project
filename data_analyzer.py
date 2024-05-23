import math
import tabulate as tb
import matplotlib.pyplot as plt
from scipy.stats import norm
from functions import line_intersection

# class GeneralDataAnalyzer:
#     def __init__(self, data: list[float]) -> None:
#         self.data = sorted(data)
#         self.length = len(self.data)

#         self.range: float
#         self.intervals_count: int
#         self.interval_size: float

#         # self.intervals_table = IntervalsTable()
#         # self.intervals_table.set_headers(["Номер", "Інтервал", "Центр інтервалу", "Частота", "Частість", "Накопичена частота", "Накопичена частість"])

#         # self.average: float
#         # self.dispersion: float
#         # self.average_quadratic_deviation: float
#         # self.variation_coeffitient: float
#         # self.asymmetry_coeffitient: float
#         # self.excess_coeefitient: float
#         # self.mode: float
#         # self.median: float
#         # self.plots: plt.Figure
#         # self.t_average: float
#         # self.t_dispersion: float
#         # self.parabolic_parameters: tuple[float]

#     def find_intervals_parameters(self) -> None:
#         self.range = self.data[-1] - self.data[0]
#         self.intervals_count = math.ceil(1 + 3.3221 * math.log10(len(self.data)))
#         self.interval_size = self.range / self.intervals_count

#     def fill_intervals_table(self) -> None:
#         half_size = self.interval_size / 2 # half of original interval size, used for shifting
#         corrected_size = self.interval_size * (1 + 1 / self.intervals_count) # corrected interval size, used because of intervals shifting

#         cumulative_count = 0 
#         cumulative_frequency = 0
#         for i in range(self.intervals_count):
#             lower_bound = self.data[0] - half_size + corrected_size * i
#             upper_bound = lower_bound + corrected_size
#             interval = f'{round(lower_bound} - {upper_bound}'
#             interval_center = (lower_bound + upper_bound) / 2
#             count = len([i for i in self.data if lower_bound <= i < upper_bound])
#             frequency = count / self.length
#             cumulative_count += count
#             cumulative_frequency += frequency

#             line = [i, interval, interval_center, count, frequency, cumulative_count, cumulative_frequency]
#             self.intervals_table.append_to_body(line)

#         whole_interval = f'{self.data[0] - half_size} - {upper_bound}'
#         footers = ["-", whole_interval,  "-", cumulative_count, cumulative_frequency, cumulative_count, cumulative_frequency]
#         self.intervals_table.set_footers(footers)    

    


# class GeneralDataAnalyzerReader:
#     def __init__(self, analyzer: GeneralDataAnalyzer) -> None:
#         self.analyzer = analyzer
#         self.data_grid: list[list]

#     def get_data_representation_string(self, elements_per_row: int) -> str:
#         if self.data_grid == None:
#             self.data_grid = []
#             for i in range(math.ceil(self.analyzer.length / elements_per_row)):
#                 self.data_grid.append([])

#             x, y = 0
#             for el in self.analyzer.data:
#                 self.data_grid[y].append(el)
#                 x += 1
#                 if x > elements_per_row - 1:
#                     x = 0
#                     y += 1

#         return tb.tabulate(self.data_grid)


# # class 


# class NormalDistributedDataAnalyzer:
#     pass



class DataAnalyzer:

    def __init__(self, data: list[float]) -> None:
        self.data = sorted(data)

        self.range: float
        self.intervals_count: int
        self.interval_size: float

        self.intervals_table = IntervalsTable()
        self.intervals_table.set_headers(["Номер", "Інтервал", "Центр інтервалу", "Частота", "Частість", "Накопичена частота", "Накопичена частість"])

        self.average: float
        self.dispersion: float
        self.average_quadratic_deviation: float
        self.variation_coeffitient: float
        self.asymmetry_coeffitient: float
        self.excess_coeefitient: float
        self.mode: float
        self.median: float
        self.plots: plt.Figure
        self.t_average: float
        self.t_dispersion: float
        self.parabolic_parameters: tuple[float]
    
    # main functionality

    # run all analyzind methods
    def analyze_data(self) -> None:
        self.find_size()
        self.find_intervals_data()
        self.find_characteristics()
        self.plot()
        self.find_theoretical_parameters()
        self.find_dependence()

    # analysis methods

    # find range, number of intervals and width of each interval
    def find_size(self) -> None:
        self.range = self.data[-1] - self.data[0]
        self.intervals_count = math.ceil(1 + 3.3221 * math.log10(len(self.data)))
        self.interval_size = self.range / self.intervals_count

    # form interval table
    def find_intervals_data(self) -> None:
        half_size = self.interval_size / 2 # half of original interval size, used for shifting
        corrected_size = self.interval_size * (1 + 1 / self.intervals_count) # corrected interval size, used because of intervals shifting

        cumulative_count = 0 
        cumulative_frequency = 0
        for i in range(self.intervals_count):
            lower_bound = self.data[0] - half_size + corrected_size * i
            upper_bound = lower_bound + corrected_size
            interval = f'{lower_bound} - {upper_bound}'
            interval_center = (lower_bound + upper_bound) / 2
            count = len([i for i in self.data if lower_bound <= i < upper_bound])
            frequency = count / len(self.data)
            cumulative_count += count
            cumulative_frequency += frequency

            line = [i, interval, interval_center, count, frequency, cumulative_count, cumulative_frequency]
            self.intervals_table.append_to_body(line)

        whole_interval = f'{self.data[0] - half_size} - {upper_bound}'
        footers = ["-", whole_interval,  "-", len(self.data), 1.0, cumulative_count, cumulative_frequency]
        self.intervals_table.set_footers(footers)

    # find average, dispersion and deviation, variation, asymmetry and excess
    def find_characteristics(self) -> None:
        averages = self.intervals_table.extract_column(2)
        self.average = sum(averages) / len(averages)
        counts = self.intervals_table.extract_column(3)
        self.dispersion = sum([math.pow(averages[i] - self.average, 2) * counts[i] for i in range(len(averages))]) / len(self.data)
        self.average_quadratic_deviation = math.sqrt(self.dispersion)
        self.variation_coeffitient = self.average_quadratic_deviation / self.average
        self.asymmetry_coeffitient = sum([math.pow(averages[i] - self.average, 3) * counts[i] for i in range(len(averages))]) / (len(self.data) * math.pow(self.average_quadratic_deviation, 3))
        self.excess_coeefitient = sum([math.pow(averages[i] - self.average, 4) * counts[i] for i in range(len(averages))]) / (len(self.data) * math.pow(self.average_quadratic_deviation, 4)) - 3

    # plot required plots, find median and mode
    def plot(self) -> None:
        self.plots, axis = plt.subplots(2, 2)
        centers = self.intervals_table.extract_column(2)
        counts = self.intervals_table.extract_column(3)
        cumulative_frequency = self.intervals_table.extract_column(6)

        axis[0, 0].plot(centers, counts)
        axis[0, 0].set_title("Полігон частот")

        index_of_max_count = counts.index(max(counts))
        bar_width = self.interval_size * 0.95
        axis[0, 1].bar(centers, counts, width = bar_width)
        x1, y1 = centers[index_of_max_count] - bar_width / 2, counts[index_of_max_count]
        x2, y2 = centers[index_of_max_count + 1] - bar_width / 2, counts[index_of_max_count + 1]
        x3, y3 = centers[index_of_max_count] + bar_width / 2, counts[index_of_max_count]
        x4, y4 = centers[index_of_max_count - 1] + bar_width / 2, counts[index_of_max_count - 1]
        axis[0, 1].plot([x1, x2], [y1, y2], color="red")
        axis[0, 1].plot([x3, x4], [y3, y4], color="red")
        intersection = line_intersection(((x1, y1), (x2, y2)), ((x3, y3), (x4, y4)))
        self.mode = intersection[0]
        axis[0, 1].vlines(x=self.mode, ymin = 0, ymax = intersection[1], color="red", linestyle="dashed")
        axis[0, 1].set_title("Гістограма")

        axis[1, 0].plot(centers, cumulative_frequency)
        lower_index = 0
        while True:
            if (cumulative_frequency[lower_index + 1] > 0.5):
                break
            lower_index += 1
        cumulate_line = ((centers[lower_index], cumulative_frequency[lower_index]), (centers[lower_index + 1], cumulative_frequency[lower_index + 1]))
        median_line = ((0, 0.5), (centers[-1], 0.5))
        self.median = line_intersection(cumulate_line, median_line)[0]
        axis[1, 0].vlines(x=self.median, ymax=0.5, ymin=0, color="red", linestyle="dashed")
        axis[1, 0].hlines(y=0.5, xmin=centers[0], xmax=self.median, color="red", linestyle="dashed")
        axis[1, 0].set_title("Кумулята")

    def find_theoretical_parameters(self) -> None:
        self.t_average, self.t_dispersion = norm.fit(self.data)

    def find_dependence(self) -> None:
        n = len(self.data)
        centers = self.intervals_table.extract_column(2)
        frequencies = self.intervals_table.extract_column(4)
        # TODO replace ** with math.pow
        x_power_2_y = sum([math.pow(x, 2) * y for x, y in zip(centers, frequencies)])
        x_power_2 = sum([math.pow(x, 2) for x in centers])
        y = sum([y for y in frequencies])
        x_power_4 = sum([math.pow(x, 4) for x in centers])
        xy = sum([x * y for x, y in zip(centers, frequencies)])

        a = (n * x_power_2_y - x_power_2 * y) / (n * x_power_4 - math.pow(x_power_2, 2))
        b = xy / x_power_2
        c = (x_power_4 * y - x_power_2 * x_power_2_y) / (n * x_power_4 - math.pow(x_power_2, 2))

        self.parabolic_parameters = (a, b, c)
   
    # get methods

    def get_data_representation_string(self, elements_per_line: int, digits_after_point_number: int) -> str:
        result = ""
        i = 0
        for element in self.data:
            if element >= 0:
                result += " "
            result += f"{element:.{digits_after_point_number}f}\t"
            i += 1
            if i == elements_per_line:
                i = 0
                result += '\n'

        return result

    def show_plot(self) -> None:
        plt.show()
    

class IntervalsTable:
    def __init__(self) -> None:
        self.headers: list = []
        self.types: list[type] = []
        self.body: list[list] = []
        self.footers: list = []

    def set_headers(self, headers: list) -> None:
        self.headers = headers

    def set_column_types(self, types: list[type]) -> None:
        self.types = types

    def append_to_body(self, line: list) -> None:
        self.body.append(line)

    def set_footers(self, footers: list) -> None:
        self.footers = footers

    def extract_column(self, index: int) -> list:
        return [line[index] for line in self.body]
    
    def get_table_representation(self) -> str:
        return tb.tabulate([*self.body, self.footers], self.headers)