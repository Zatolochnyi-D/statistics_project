import math
import tabulate as tb
import matplotlib.pyplot as plt
from IntervalsTable import IntervalsTable
from Functions import *

class GeneralAnalyzer:
    def __init__(self, data: list[float]) -> None:
        self.data = sorted(data)
        self.n = len(self.data)

        # interval parameters
        self.range: float
        self.intervals_count : float
        self.interval_size: float

        # intervals table
        self.intervals_table: IntervalsTable
        self.plots: plt.Figure

        # characteristics
        self.average: float
        self.dispersion: float
        self.std: float
        self.variation: float
        self.modes: list[float] = []
        self.median: float

    def get_data_representation_string(self, elements_per_row: int) -> str:
        data_grid = []
        for i in range(math.ceil(self.n / elements_per_row)):
            data_grid.append([])
        x = y = 0
        for el in self.data:
            data_grid[y].append(el)
            x += 1
            if x > elements_per_row - 1:
                x = 0
                y += 1
        return tb.tabulate(data_grid)
    
    def find_interval_parameters(self) -> None:
        self.range = round(self.data[-1] - self.data[0], 10)
        self.intervals_count = round(math.ceil(1 + 3.3221 * math.log10(len(self.data))), 10)
        self.interval_size = round(self.range / self.intervals_count, 10)

    def build_intervals_table(self) -> None:
        self.intervals_table = IntervalsTable(["№", "Інтервал", "Центр інтервалу", "Частота", "Частість", "Накопичена частота", "Накопичена частість"])
        self.intervals_table.build_table(self.interval_size, self.intervals_count, self.data)

    def plot_graphics(self) -> None:
        self.plots, axis = plt.subplots(2, 2)
        centers = self.intervals_table.extract_column(2)
        counts = self.intervals_table.extract_column(3)
        cumulative_frequency = self.intervals_table.extract_column(6)

        axis[0, 0].plot(centers, counts)
        axis[0, 0].set_title("Полігон частот")

        bar_width = self.interval_size * 0.95
        axis[0, 1].bar(centers, counts, width = bar_width)
        axis[0, 1].set_title("Гістограма")

        indexes_of_max = []
        if counts[0] > counts[1]:
            indexes_of_max.append(0)
        if counts[-1] > counts[-2]:
            indexes_of_max.append(self.intervals_count - 1)
        for i in range(1, self.intervals_count - 1):
            if counts[i] > counts[i - 1] and counts[i] > counts[i + 1]:
                indexes_of_max.append(i)
        # index_of_max_count = counts.index(max(counts))
        for i, index in enumerate(indexes_of_max):
            x1_1, y1_1 = centers[index] - bar_width / 2, counts[index]
            if index + 1 < self.n:
                x2_1, y2_1 = centers[index + 1] - bar_width / 2, counts[index + 1]
            else:
               x2_1, y2_1 = centers[index] + self.interval_size - bar_width / 2, 0
            line1 = ((x1_1, y1_1), (x2_1, y2_1))
            x1_2, y1_2 = centers[index] + bar_width / 2, counts[index]
            if index - 1 > -1:
                x2_2, y2_2 = centers[index - 1] + bar_width / 2, counts[index - 1]
            else:
                x2_2, y2_2 = centers[index] - self.interval_size + bar_width / 2, 0
            line2 = ((x1_2, y1_2), (x2_2, y2_2))
            axis[0, 1].plot([x1_1, x2_1], [y1_1, y2_1], color="red")
            axis[0, 1].plot([x1_2, x2_2], [y1_2, y2_2], color="red")
            intersection = line_intersection(line1, line2)
            self.modes.append(intersection[0])
            axis[0, 1].vlines(x=self.modes[i], ymin = 0, ymax = intersection[1], color="red", linestyle="dashed")

        # x1_1, y1_1 = centers[index_of_max_count] - bar_width / 2, counts[index_of_max_count]
        # if index_of_max_count + 1 < len(counts):
        #     x2_1, y2_1 = centers[index_of_max_count + 1] - bar_width / 2, counts[index_of_max_count + 1]
        # else:
        #     x2_1, y2_1 = centers[index_of_max_count] + self.interval_size - bar_width / 2, 0
        # line1 = ((x1_1, y1_1), (x2_1, y2_1))
        # x1_2, y1_2 = centers[index_of_max_count] + bar_width / 2, counts[index_of_max_count]
        # if index_of_max_count - 1 > -1:
        #     x2_2, y2_2 = centers[index_of_max_count - 1] + bar_width / 2, counts[index_of_max_count - 1]
        # else:
        #     x2_2, y2_2 = centers[index_of_max_count] - self.interval_size + bar_width / 2, 0
        # line2 = ((x1_2, y1_2), (x2_2, y2_2))
        # axis[0, 1].plot([x1_1, x2_1], [y1_1, y2_1], color="red")
        # axis[0, 1].plot([x1_2, x2_2], [y1_2, y2_2], color="red")
        # intersection = line_intersection(line1, line2)
        # self.mode = intersection[0]
        # axis[0, 1].vlines(x=self.mode, ymin = 0, ymax = intersection[1], color="red", linestyle="dashed")
        
        axis[1, 0].plot(centers, cumulative_frequency)
        axis[1, 0].set_title("Кумулята")
        lower_index = 0
        while True:
            if (cumulative_frequency[lower_index] > 0.5):
                break
            lower_index += 1
        if lower_index == 0:
            start_point = (centers[lower_index] - self.interval_size, 0)
        else:
            start_point = (centers[lower_index - 1], cumulative_frequency[lower_index - 1])
        end_point = (centers[lower_index], cumulative_frequency[lower_index])
        cumulate_line = (start_point, end_point)
        median_line = ((0, 0.5), (centers[-1], 0.5))
        self.median = line_intersection(cumulate_line, median_line)[0]
        axis[1, 0].vlines(x=self.median, ymax=0.5, ymin=0, color="red", linestyle="dashed")
        axis[1, 0].hlines(y=0.5, xmin=centers[0], xmax=self.median, color="red", linestyle="dashed")

    def find_characteristics(self) -> None:
        averages = self.intervals_table.extract_column(2)
        self.average = round(sum(averages) / self.intervals_count, 10)
        counts = self.intervals_table.extract_column(3)
        self.dispersion = round(sum([math.pow(averages[i] - self.average, 2) * counts[i] for i in range(len(averages))]) / self.n, 10)
        self.std = round(math.sqrt(self.dispersion), 10)
        self.variation = round(self.std / self.average, 10)