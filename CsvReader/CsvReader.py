import csv
from os import path

class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        if not path.exists(filepath):
            raise FileNotFoundError("file not found")
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass