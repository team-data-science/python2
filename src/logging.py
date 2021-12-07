import logging
import pandas as pd
# load a csv file
e_commerce_data_path_csv = "./data/data.csv"

e_commerce_csv_df = pd.read_csv(
    e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1000)
# create logger

# config the default level to debug
logging.basicConfig(
    filename="./data/reading_csvs.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",  # time level message
)
# > None


def is_positive(number):
    logging.debug(f"Checking if {number} is positive.")
    if number > 0:
        logging.info(f"{number} is positive?")
    else:
        logging.error(f"Error! Number {number} is negative!")


quantities = e_commerce_csv_df["Quantity"].to_list()

# write a error log
# write information to log file
for quantity in quantities:
    is_positive(quantity)
# example from the created reading_csvs.log file
# 2021-12-07 14:04:02,032 - INFO - 10 is positive?
# 2021-12-07 14: 04: 02, 032 - DEBUG - Checking if -1 is positive.
# 2021-12-07 14: 04: 02, 032 - ERROR - Error! Number - 1 is negative!
# 2021-12-07 14: 04: 02, 032 - DEBUG - Checking if 12 is positive.
