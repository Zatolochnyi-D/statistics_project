import csv
import tabulate as tb

class CsvFileReader:
    
    def __init__(self) -> None:
        self.raw_data = []

    def read_file(self, file_path: str) -> None:
        with open(file_path) as file:
            reader = csv.reader(file)
            self.raw_data = []
            for line in reader:
                self.raw_data.append(line)

    def peek_first_rows(self, amount_of_rows: int) -> str:
        return tb.tabulate(self.raw_data[0:amount_of_rows])

    def extract_column(self, column_index: int, skip_first_row: bool) -> list:
        result = [line[column_index] for line in self.raw_data]
        if skip_first_row: result.pop(0)
        return result
    
    def extract_number_column(self, column_index: int, skip_first_row: bool) -> list:
        return [float(el) for el in self.extract_column(column_index, skip_first_row)]