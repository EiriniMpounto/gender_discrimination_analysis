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
    print('The number of the current CEOS in the dataset',ceo_counts)
    print('The number of the current CFOs in the dataset', cfo_counts)
    
    return ceo_counts, cfo_counts



def ceo_cfo_gender(data):
    '''
    The current function calculates the number
    of women that possess the title of the CEO
    VS the number of men that possess the same 
    title at the current moment.(PCEO and PCFO)
    '''
    # ceo and gender
    ceo_gender = data.groupby(['PCEO', 'GENDER'])['EXEC_FULLNAME']
    calculate_ceo_gender = ceo_gender.count()
    print('How many women and men have currently the title CEO',calculate_ceo_gender)
    
    # cfo and gender
    cfo_gender = data.groupby(['PCFO', 'GENDER'])['EXEC_FULLNAME']
    calculate_cfo_gender = cfo_gender.count()
    print('How many women and men have currently the CFO title', calculate_cfo_gender)
    

def average_age_bygender(data):
    '''
    This function calculates the average age of women
    in the entire database VS the average age of men.
    '''
    av_age = data.groupby('GENDER', as_index=False)['AGE'].mean()
    print('The average age of women VS men is',av_age)
    return av_age

def average_salary_by_gender(data):
    '''
    This function calculates the average salary of 
    women VS men
    '''
    av_salary = data.groupby('GENDER', as_index = False)['SALARY'].mean()
    print('The average salary of women VS men', av_salary)
    
    return av_salary

def average_sal_pct_gender(data):
     '''
     This function calculates the salry 
     percentange change for women VS Men
     '''
     av_pct_sal = data.groupby('GENDER', as_index = False)['SAL_PCT'].mean()
     print(av_pct_sal)
     
     return av_pct_sal

def av_total_compensation_gender(data):
    '''
    This function calculates the average of total 
    compensation for men VS women
    '''
    av_tdc_gender = data.groupby('GENDER', as_index= False)['TDC1'].mean()
    print('The total compensation by gender is:', av_tdc_gender)
    
    return av_tdc_gender

def reason_leaving_gender(data):
    '''
    This function calculates the most common reason 
    that women and men are leaving their company
    '''
    reason_gender = data.groupby(['REASON', 'GENDER'])['EXEC_FULLNAME']
    reason_gender = reason_gender.count()
    print(reason_gender)
    return reason_gender