import random as r
import tabulate as tb

class DataPicker:

    def __init__(self, data: list) -> None:
        self.data = data

    def get_data_preview_string(self, rows: int) -> str:
        return tb.tabulate([self.data[i] for i in range(rows)])

    def pick_random(self, amount: int) -> list:
        return r.choices(self.data, k = amount)