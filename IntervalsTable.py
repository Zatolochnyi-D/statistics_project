import tabulate as tb

class IntervalsTable:
    def __init__(self, headers: list) -> None:
        self.headers = headers
        self.body: list[list] = []
        self.footers: list = []

    def set_headers(self, headers: list) -> None:
        self.headers = headers

    def build_table(self, interval_size, intervals_count, data) -> None:
        half_size = interval_size / 2 
        corrected_size = interval_size * (1 + 1 / intervals_count)
        n = len(data)

        cumulative_count = 0 
        cumulative_frequency = 0
        for i in range(intervals_count):
            lower_bound = round(data[0] - half_size + corrected_size * i, 10)
            upper_bound = round(lower_bound + corrected_size, 10)
            interval = [lower_bound, upper_bound]
            interval_center = round((lower_bound + upper_bound) / 2, 10)
            count = len([i for i in data if lower_bound <= i < upper_bound])
            frequency = count / n
            cumulative_count += count
            cumulative_frequency += frequency

            line = [i, interval, interval_center, count, frequency, cumulative_count, cumulative_frequency]
            self.append_to_body(line)

        whole_interval = [round(data[0] - half_size, 10), upper_bound]
        footers = ["-", whole_interval,  "-", n, 1.0, cumulative_count, cumulative_frequency]
        self.set_footers(footers)

    def append_to_body(self, line: list) -> None:
        self.body.append(line)

    def set_footers(self, footers: list) -> None:
        self.footers = footers

    def extract_column(self, index: int) -> list:
        return [line[index] for line in self.body]
    
    def get_table_representation(self) -> str:
        return tb.tabulate([*self.body, self.footers], self.headers, tablefmt="rounded_grid")