import random as r
import tabulate as tb

class DataPicker:

    def __init__(self, data: list) -> None:
        self.data = data

    def get_data_preview_string(self, rows: int) -> str:
        return tb.tabulate([self.data[i] for i in range(rows)])

    def pick_random(self, amount: int) -> list:
        return r.choices(self.data, k = amount)
    
    def pick_even(self, amount: int) -> list:
        step = len(self.data) // amount
        selected = []
        for i in range(amount):
            selected.append(self.data[i * step])
        return selected
    
    # def pick_from_querry(self, querry_string: str) -> None:
    #     # possible option: select 1 element
    #     # example: 42
    #     # possible errors: out of range
    #     # possible option: select range
    #     # example: [10 15]
    #     # possible errors: [ 10 15] additional space, out of range, more numbers in brackets [1 2 3 4]
    #     # possible option: select range with steps
    #     # example: [10 15 2]
    #     # possible errors: [ 10 15 2 ] additional space, out of range, more numbers in brackets [1 2 3 4]
    #     # possible option: select random
    #     # example: {15}
    #     # possible errors: { 15} additional space, more numbers in brackets {1 2}
    #     querry = querry_string.split()
    #     for i, el in enumerate(querry):
    #         if el[0] == '[':
    #             if len(el) == 1:
    #                 return None
                
    #             # [
    #             # [14]
    #             # [14 24]
    #             # 
    #             pass
    #         elif el[0] == '{':
    #             pass

    #         try:
    #             parsed_el = int(el)
    #         except ValueError:
    #             return None
            
    # def extract_number(self, string: str) -> int:
    #     pass