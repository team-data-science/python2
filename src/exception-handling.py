import pandas as pd
# load a csv file
e_commerce_data_path_csv = "./data/data.csv"
e_commerce_data_fake_path_csv = "./data/fake_data.csv"

# try - except example, raise a BaseException

try:
    e_commerce_csv_df = pd.read_csv(
        e_commerce_data_fake_path_csv,  encoding='unicode_escape', nrows=1000)
except:
    print(
        "Please provide a corect path to the file!"
    )
# > Please provide a corect path to the file!

# show with value exception or something else
try:
    e_commerce_csv_df = pd.read_csv(
        e_commerce_data_fake_path_csv,  encoding='unicode_escape', nrows=1000)
except FileNotFoundError as error:
    print(
        # f stings for better formating
        f"{error}, please provide a corect path to the file!"
    )
# > [Errno 2] No such file or directory: 'fake_data.csv', please provide a corect path to the file!


# create a user defined exception

class FileHasToManyRows(Exception):
    """Exception raised if file has too many rows.

    Attributes:
        salary -- input csv file
        message -- error description
    """

    def __init__(self, number_of_rows):
        self.number_of_rows = number_of_rows
        self.message = f"Csv file has too many rows, max rows is 1000 and the file has {self.number_of_rows}"

        super().__init__(self.message)


try:
    e_commerce_csv_df = pd.read_csv(
        e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1100)
    number_of_rows = len(e_commerce_csv_df)
    if number_of_rows > 1000:
        raise FileHasToManyRows(number_of_rows)
except FileNotFoundError as error:
    print(
        f"{error}, please provide a corect path to the file!"
    )
# > Traceback (most recent call last):
# >   File "<string>", line 6, in <module>
# > FileHasToManyRows: Csv file has too many rows, max rows is 1000 and the file has 1100
