import random as r

class DataPicker:

    def __init__(self, data: list) -> None:
        self.data = data

    def pick_random(self, amount: int) -> list:
        return r.choices(self.data, k = amount)