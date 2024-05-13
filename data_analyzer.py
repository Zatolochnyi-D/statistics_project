import math
import tabulate as tb

class DataAnalyzer:

    def __init__(self,) -> None:
        self.data = None
        self.range = None
        self.interval_count = None
        self.interval_size = None
        self.interval_names = ["id", "working_time", "count", "frequency", "cumultive_count", "cumultive_frequency", "intervals_center"]
        self.intervals = []
    
    # main functionality

    def set_data(self, data: list[float]) -> None:
        if type(data) != list:
            raise TypeError("Data Analyzer expects list of floats")
        for el in data:
            if type(el) != float:
                raise TypeError("Data Analyzer expects list of floats")
        self.data = sorted(data)

    # run all analyzind methods
    def analyze_data(self) -> None:
        self.find_size()
        self.find_intervals_data()

    # analysis methods

    # find range, number of intervals and width of each interval
    def find_size(self) -> None:
        self.range = self.data[-1] - self.data[0]
        self.interval_count = math.ceil(1 + 3.3221 * math.log10(len(self.data)))
        self.interval_size = self.range / self.interval_count

    # form interval table
    def find_intervals_data(self) -> None:
        half_size = self.interval_size / 2 # half of original interval size, used for shifting
        corrected_size = self.interval_size * (1 + 1 / self.interval_count) # corrected interval size, used because of intervals shifting

        cumulative_count = 0 
        cumulative_frequency = 0
        for i in range(self.interval_count):
            lower_bound = self.data[0] - half_size + corrected_size * i
            upper_bound = lower_bound + corrected_size
            working_time = f'{lower_bound} - {upper_bound}'
            count = len([i for i in self.data if lower_bound <= i < upper_bound])
            frequency = count / len(self.data)
            cumulative_count = sum([i[2] for i in self.intervals]) + count
            cumulative_frequency = sum([i[3] for i in self.intervals]) + frequency
            interval_center = round((lower_bound + upper_bound) / 2, 3)

            self.intervals.append([i, working_time, count, frequency, cumulative_count, cumulative_frequency, interval_center])
        whole_interval = f'{round(self.data[0] - half_size, 3)} - {round(self.data[-1] + half_size, 3)}'
        self.intervals.append(["-", whole_interval, len(self.data), 1.0, cumulative_count, cumulative_frequency, "-"])

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
    
    def get_interval_table_representation(self) -> str:
        return tb.tabulate(self.intervals, self.interval_names)