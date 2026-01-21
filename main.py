# Dataset Management and Basic Analysis System
# University of Ilorin 

import csv

class DataSet:
    def __init__(self, numeric_file, category_file, threshold=60):
        self.numeric_file = numeric_file
        self.category_file = category_file
        self.threshold = threshold
        self.data = []
        self.categories = set()

        self.total = 0
        self.average = 0
        self.minimum = None
        self.maximum = None

    def load_data(self):
        try:
            with open(self.numeric_file, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    for value in row:
                        try:
                            self.data.append(float(value))
                        except ValueError:
                            pass

            if not self.data:
                raise ValueError("No valid numeric data found.")

        except FileNotFoundError:
            print("Numeric data file not found.")
            return False

        try:
            with open(self.category_file, "r") as file:
                for line in file:
                    if line.strip():
                        self.categories.add(line.strip())

        except FileNotFoundError:
            print("Category file not found.")
            return False

        return True

    def calculate_statistics(self):
        self.total = sum(self.data)
        self.average = self.total / len(self.data)
        self.minimum = min(self.data)
        self.maximum = max(self.data)

    def display_results(self):
        print("UNILORIN DATA ANALYSIS RESULTS")
        print("Total Score:", self.total)
        print("Average Score:", self.average)
        print("Minimum Score:", self.minimum)
        print("Maximum Score:", self.maximum)
        print("Unique Departments:", len(self.categories))

        if self.average >= self.threshold:
            print("Performance: High Performance")
        else:
            print("Performance: Needs Improvement")

    def save_report(self):
        with open("report.txt", "w") as file:
            file.write("University of Ilorin Dataset Report\n")
            file.write(f"Total Score: {self.total}\n")
            file.write(f"Average Score: {self.average}\n")
            file.write(f"Minimum Score: {self.minimum}\n")
            file.write(f"Maximum Score: {self.maximum}\n")
            file.write(f"Unique Departments: {len(self.categories)}\n")

if __name__ == "__main__":
    ds = DataSet("numeric_data.csv", "categories.txt")
    if ds.load_data():
        ds.calculate_statistics()
        ds.display_results()
        ds.save_report()
