import pandas as pd
import seaborn as sns

def gender_counts(data):
    '''
    The current function calculates the number
    of males VS the number of the females that 
    exist in our dataset.
    '''
    sex_counts = data['GENDER'].value_counts()
    print('How many women and men we have on our dataset',sex_counts)
    
    return sex_counts



def ceo_counts(data):
    '''
    This function calsulates the number of the CEOs
    and the number of the CFOs in the sample
    '''
    ceo_counts = data['PCEO'].value_counts()
    cfo_counts = data['PCFO'].value_counts()
    print('The number of the CEOS in the dataset',ceo_counts)
    print('The number of the CFOs in the dataset', cfo_counts)
    
    return ceo_counts, cfo_counts



def ceo_and_gender(data):
    '''
    The current function calculates the number
    of women that possess the title of the CEO
    VS the number of men that possess the same 
    title at the current moment.
    '''
    if data['PCEO']=='CEO':
        ceo_gender = data[['GENDER','PCEO']].groupby(['GENDER'])
        calculate_ceo_gender = ceo_gender.count()
        print('How many women and how many men have the title CEO, CFO',calculate_ceo_gender)
    
    return(calculate_ceo_gender)
    




