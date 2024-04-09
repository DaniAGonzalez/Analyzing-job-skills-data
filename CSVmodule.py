"""
Matthew Gregorio
Daniela Alejandra Gonzalez
Ikonkar Kaur Khalsa
"""
import csv

class CSVLoader:
    def __init__(self, filename):
        """
        function: Initialize the CSVLoader.
        param: filename (str): The name of the CSV file.
        """
        self.filename = filename
        self.data = []

    def load_data(self):
        """
        function: Load data from the CSV file into self.data list. This method will read the specified
                  CSV file and adds its contents to the 'self.data' list.
        raises: If the file is not found, an error will be raised.
        """
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader: # Iteration over each line of the CSV file
                    self.data.append(row)
            print("CSV file loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error while loading the file: {e}")

    def display_data(self, n=5):
        """
        function: Display the first n rows of loaded data.This method prints the
                  first n rows of the loaded data stored in the 'self.data'. If no
                  value for 'n' is provided, it defaults to 5.
        param: n (int): The number of rows to display. Default is 5.
        raises: If the data is not loaded, it will print a message indicating
                that no file is loaded.
        """
        if self.data: # Checking if the data is loaded; if so then:
            print(f"First {n} rows:")
            for row in self.data[:n]:
                print(row)
        else:
            print("No file loaded.")

    def tail_data(self, n=5):
        """
        function: Display the last n rows of loaded data. It will print the last
                  n rows of the loaded data stored in the 'self.data' attribute.
                  If there are no values for 'n', it will print the default, which is 5.
        param: n (int): The number of rows to display. Default is 5.
        raises: If the data is not loaded, it will print a message indicating that no
                file is loaded.
        """
        if self.data: # Checking if the data is loaded; if so then:
            print(f"Last {n} rows:")
            for row in self.data[-n:]:
                print(row)
        else:
            print("No file loaded.")

    def info(self):
        """
        function: Display information about the loaded data. This method prints the
                  information about the loaded data, specifically the number of rows.
        return: If the data is loaded, it prints the number of rows stored in the 'self.data'
                attribute. Otherwise, it prints a message indicating that no file is loaded.
        """
        if self.data: # Checking if the data is loaded; if so then:
            print(f"Number of rows: {len(self.data)}")
        else:
            print("No file loaded.")

# Example usage
#csv_loader = CSVLoader("job_skills.csv")
#csv_loader.load_data()
#csv_loader.display_data()
#csv_loader.tail_data()
#csv_loader.info()