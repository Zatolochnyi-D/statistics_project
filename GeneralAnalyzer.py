import math
import tabulate as tb

class GeneralAnalyzer:
    def __init__(self, data: list[float]) -> None:
        self.data = sorted(data)
        self.n = len(self.data)

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