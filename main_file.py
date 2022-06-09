'WOMEN TRAVELLERS IN A MANS WORLD'

# import initial libraries
import os
import pandas as pd

# import secondary libraries
from file_loader import DataLoader
from data_cleaner import DataCleaner
from descriptive_statistics import (ceo_cfo_gender, gender_counts, 
                                    ceo_counts, average_age_bygender, 
                                    average_salary_by_gender, average_sal_pct_gender, 
                                    av_total_compensation_gender, reason_leaving_gender)

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
#print(raw_ceo_data)

# clean the data
clean_data_funtion = DataCleaner()
ceo_data = clean_data_funtion.clean_data(raw_ceo_data)
ceo_data.to_csv(os.path.join(output_folder, './clean_ceo_data.csv'))
#print(ceo_data)

# Start calculating the descriptives

# number of man and women 
sex_counts = gender_counts(ceo_data)
# number of current CEOs per gender
ceos_counts = ceo_counts(ceo_data)
# number of current CFOs per gender
ceo_gender_counts = ceo_cfo_gender(ceo_data)
# average age per gender
average_age_per_gender = average_age_bygender(ceo_data)
# average salary by gender
av_salary_per_gender = average_salary_by_gender(ceo_data)
# average percentange salry change by gender
av_pct_sal_by_gender = average_sal_pct_gender(ceo_data)
# average of total compensation per gender
av_tdc_by_gender = av_total_compensation_gender(ceo_data)
# reason men and women leave the company
reason_per_gender = reason_leaving_gender(ceo_data)

