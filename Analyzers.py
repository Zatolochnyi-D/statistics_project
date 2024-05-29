import math
import tabulate as tb
import matplotlib.pyplot as plt
from IntervalsTable import IntervalsTable
from Functions import *
from scipy.stats import norm, chi2, t as student

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
            self.modes.append(round(intersection[0], 10))
            axis[0, 1].vlines(x=self.modes[i], ymin = 0, ymax = intersection[1], color="red", linestyle="dashed")
        
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

    def get_concrete_analyzer(self, analyzer_id: int):
        possible_analyzers = [NormalDistAnalyzer]
        # possible_analyzers_string_ids = ["normal"]

        # if type(analyzer_id) == str:
        #     if analyzer_id not in possible_analyzers_string_ids:
        #         return None
        #     index = possible_analyzers_string_ids.index(analyzer_id.lower())
        #     analyzer = possible_analyzers[index]()
        # elif type(analyzer_id) == int:

        return possible_analyzers[analyzer_id](self)
    
class NormalDistAnalyzer:
    def __init__(self, analyzer: GeneralAnalyzer) -> None:
        self.general_analyzer = analyzer

        self.estimate_average: float
        self.estimate_std: float

        self.possible_dependence_parameteres: tuple[float]

        self.average_confidence_interval: tuple[float]
        self.dispersion_confidence_interval: tuple[float]

        self.hipothesis0_parameter_rejected: bool
        self.hipothesis0_d_rejected: bool
        self.average_critical_range: tuple
        self.average_criteria_power: float
        self.dispersion_critical_range: tuple
        self.required_n: int

        self.is_normal_dist: bool

    def find_parameters_estimation(self) -> None:
        (a, s) = norm.fit(self.general_analyzer.data, method="MLE")
        self.estimate_average = round(a, 10)
        self.estimate_std = round(s, 10)

    def find_possible_dependence(self) -> None:
        centers = self.general_analyzer.intervals_table.extract_column(2)
        frequencies = self.general_analyzer.intervals_table.extract_column(4)
        n = self.general_analyzer.n
        x2y = sum([math.pow(x, 2) * y for x, y in zip(centers, frequencies)])
        x2 = sum([math.pow(x, 2) for x in centers])
        y = sum(frequencies)
        x4 = sum([math.pow(x, 4) for x in centers])
        xy = sum([x * y for x, y in zip(centers, frequencies)])

        a = (n * x2y - x2 * y) / (n * x4 - math.pow(x2, 2))
        b = xy / x2
        c = (x4 * y - x2 * x2y) / (n * x4 - math.pow(x2, 2))

        self.possible_dependence_parameteres = (round(a, 10), round(b, 10), round(c, 10))

    def find_confidence_intervals(self, gamma) -> None:
        deviation = math.sqrt(self.general_analyzer.dispersion / self.general_analyzer.n)
        t = inverse_laplace_function(gamma)
        delta = t * deviation
        self.average_confidence_interval = (self.general_analyzer.average - delta, self.general_analyzer.average + delta)

        k = self.general_analyzer.n - 1
        ns2 = self.general_analyzer.n * self.general_analyzer.dispersion
        if k < 30:
            xi1 = chi2.isf((1 + gamma) / 2, k)
            xi2 = chi2.isf((1 - gamma) / 2, k)
            self.dispersion_confidence_interval = (round(ns2 / xi2, 10), round(ns2 / xi1, 10))
        else:
            xi1 = 0.5 * math.pow(math.sqrt(2 * k - 1) - t, 2)
            xi2 = 0.5 * math.pow(math.sqrt(2 * k - 1) + t, 2)
            self.dispersion_confidence_interval = (round(ns2 / xi2, 10), round(ns2 / xi1, 10))

    def test_parameter_hypothesis(self, alpha, possible_average) -> None:
        average_criteria = (self.general_analyzer.average - possible_average) / self.general_analyzer.std * math.sqrt(self.general_analyzer.n - 1)
        average_critical = student.ppf(1 - alpha, self.general_analyzer.n - 1)
        self.hipothesis0_parameter_rejected = abs(average_criteria) > average_critical

        coeffitient = self.general_analyzer.std / math.sqrt(self.general_analyzer.n - 1) * average_critical
        if self.general_analyzer.average > possible_average:
            average_critical_point = round(possible_average + coeffitient, 10)
            self.average_critical_range = (average_critical_point, "inf")
            self.average_criteria_power = round(norm.cdf(average_critical - (self.general_analyzer.average - possible_average) / self.general_analyzer.std * math.sqrt(self.general_analyzer.n - 1)), 10)
        else:
            average_critical_point = round(possible_average - coeffitient, 10)
            self.average_critical_range = ("-inf", average_critical_point)
            self.average_criteria_power = round(norm.cdf(average_critical - (possible_average - self.general_analyzer.average) / self.general_analyzer.std * math.sqrt(self.general_analyzer.n - 1)), 10)

    def find_n_from_alpha_and_beta(self, possible_average, alpha, beta) -> None:
        coeffitient = self.general_analyzer.dispersion / math.pow(self.general_analyzer.average - possible_average, 2)
        func_to_search = lambda x: math.pow(student.ppf(1 - alpha, x - 1) + student.ppf(1 - beta, x - 1), 2) * coeffitient - x
        self.required_n = int(math.ceil(division_method_equation_solve(func_to_search, (2, 10000))))

    def test_for_normal_distribution(self, possible_average, possible_dispersion, alpha) -> None:
        possible_std = math.sqrt(possible_dispersion)

        counts = self.general_analyzer.intervals_table.extract_column(3)
        intervals = self.general_analyzer.intervals_table.extract_column(1)
        while True:
            if counts[0] < 5:
                counts[1] += counts[0]
                counts = counts[1:]
                intervals[1] += intervals[0]
                intervals = intervals[1:]
                continue
            break
        while True:
            if counts[-1] < 5:
                counts[-2] += counts[-1]
                counts = counts[:-2]
                intervals[-2] += intervals[-1]
                intervals = intervals[:-2]
                continue
            break
        
        t_possibilities = [norm.cdf((i[1] - possible_average) /possible_std) - norm.cdf((i[0] - possible_average) / possible_std) for i in intervals]
        t_counts = [p * self.general_analyzer.n for p in t_possibilities]
        chi = sum([math.pow(c - t_c, 2) / t_c for c, t_c in zip(counts, t_counts)])
        k = len(counts) - 3
        chi_crit = chi2.isf(alpha, k)

        self.is_normal_dist = chi < chi_crit