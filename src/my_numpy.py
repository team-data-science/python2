# read in dataframe
import pandas as pd
import numpy as np
# load a csv file
e_commerce_data_path_csv = "./data/data.csv"
e_commerce_csv_df = pd.read_csv(
    e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1000)

print(e_commerce_csv_df)
    
# create new average cloumn of all attributes
quantity_array = e_commerce_csv_df["Quantity"].to_numpy()
print(np.mean(quantity_array))
# > 12.785
# find minimum in dataframe
print(np.min(quantity_array))
# > -24
# find maximum in dataframe
print(np.max(quantity_array))
# > 600

#add a random int
# randint needs to be the same as the users 100k
e_commerce_csv_df['user_id'] = np.random.randint(1,10, e_commerce_csv_df.shape[0])
print(e_commerce_csv_df.dtypes)
print(e_commerce_csv_df)