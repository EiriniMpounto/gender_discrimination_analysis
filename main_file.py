'WOMEN TRAVELLERS IN A MANS WORLD'

# import initial libraries
import os
import pandas as pd

# import secondary libraries
from file_loader import DataLoader
from data_cleaner import DataCleaner

# print all the rows in the results
# pd.set_option('display.max_rows', None)

# load data function
data_loader = DataLoader()

# setting the output 
working_directory = data_loader.working_directory
output_folder = os.path.join(working_directory, 'Output')
os.chdir(working_directory)
os.makedirs(output_folder, exist_ok=True)

# load the data
raw_ceo_data = data_loader.ceo_official_data

# read the data
raw_ceo_data = pd.read_csv(raw_ceo_data, chunksize=10000, header=0)
raw_ceo_data = pd.concat(raw_ceo_data, ignore_index=True)
print(raw_ceo_data)

# clean the data
clean_data_funtion = DataCleaner()
ceo_data = clean_data_funtion.clean_data(raw_ceo_data)
