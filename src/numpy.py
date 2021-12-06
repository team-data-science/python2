# read in dataframe
import pandas as pd
import numpy as np
# load a csv file
e_commerce_data_path_csv = "./data/data.csv"
e_commerce_csv_df = pd.read_csv(
    e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1000)
# create new average cloumn of all attributes
quantity_array = e_commerce_csv_df["Quantity"].to_numpy()
np.mean(quantity_array)
# find minimum in dataframe
np.min(quantity_array)
# find maximum in dataframe
np.max(quantity_array)
