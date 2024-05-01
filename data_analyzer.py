class DataAnalyzer:

    def __init__(self,) -> None:
        self.data = None
        self.range = None
    
    def set_data(self, data: list[float]) -> None:
        self.validate_input_data(data)
        self.data = sorted(data)

    def validate_input_data(self, data) -> None:
        if type(data) != list:
            raise TypeError("Data Analyzer expects list of floats or integers")
        for el in data:
            if type(el) != float:
                raise TypeError("Data Analyzer expects list of floats or integers")

    def find_range(self) -> None:
        self.range = self.data[-1] - self.data[0]

    def analyze_data(self) -> None:
        self.find_range()

    def get_data_representation(self, elements_per_line: int, digits_after_point_number: int) -> str:
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

    def get_range(self) -> int | float:
        return self.range