import math

class DataAnalyzer:

    def __init__(self,) -> None:
        self.data = None
        self.range = None
        self.interval_count = None
        self.interval_size = None
    
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

    # analysis methods

    # find range, number of intervals and width of each interval
    def find_size(self) -> None:
        self.range = self.data[-1] - self.data[0]
        self.interval_count = math.ceil(1 + 3.3221 * math.log10(len(self.data)))
        self.interval_size = self.range / self.interval_count

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