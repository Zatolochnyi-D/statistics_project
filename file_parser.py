import csv

class CsvFileParser:
    
    def __init__(self) -> None:
        self.raw_data = []

    def read_file(self, file_path: str) -> None:
        with open(file_path) as file:
            reader = csv.reader(file)
            self.raw_data = []
            for line in reader:
                self.raw_data.append(line)

    def peek_first_row(self) -> list:
        return self.raw_data[0]

    def extract_column(self, column_index: int, skip_first_row: bool) -> list:
        result = [line[column_index] for line in self.raw_data]
        if skip_first_row: result.pop(0)
        return result