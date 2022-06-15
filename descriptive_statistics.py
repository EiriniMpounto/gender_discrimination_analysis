import pandas as pd
import seaborn as sns


class DescriptiveStatistics:
    
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



    def pceo_pcfo_gender(data):
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
        
        return calculate_ceo_gender, calculate_cfo_gender
    

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
        print('The salary percentage change of women VS men',av_pct_sal)
     
        return av_pct_sal


    def av_total_compensation_gender(data):
        '''
        This function calculates the average of total 
        compensation for men VS women
        '''
        av_tdc1_gender = data.groupby('GENDER', as_index= False)['TDC1'].mean()
        av_tdc2_gender = data.groupby('GENDER', as_index = False)['TDC2'].mean()
    
        print('The total 1 year compensation by gender is:', av_tdc1_gender)
        print('The total 2 year compensation by gender is:', av_tdc2_gender)
    
        return av_tdc1_gender, av_tdc2_gender


    def reason_leaving_gender(data):
        '''
        This function calculates the most common reason 
        that women and men are leaving their company
        '''
        reason_gender = data.groupby(['REASON', 'GENDER'])['EXEC_FULLNAME']
        reason_gender = reason_gender.count()
        print('The most common reason that men and women are leaving the company', reason_gender)
        
        return reason_gender


    def mode_spindex_spcode(data):
        '''
        This function calculates the mode of the 
        spindex and the spcode variable
        '''
        spindex_mode = data['SPINDEX'].mode()
        print('The mode for the SPINDEX variable is:', spindex_mode)
    
        spcode_mode = data['SPCODE'].mode()
        print('The mode of the SPCODE variable is:', spcode_mode)
    
        return spindex_mode, spcode_mode


    def average_age_gender_ceo(data):
        '''
        This function calculates the average age between
        men and women that have currently the title CEO 
        and the title CFO
        '''
        # average age women VS men CEOs
        av_age_genderceo = data.groupby(['GENDER', 'PCEO'], as_index= False)['AGE'].mean()
        print('The average age of men and women that have currently the title CEO',av_age_genderceo)
        # average age women VS men CFOs
        av_age_gendercfo = data.groupby(['GENDER', 'PCFO'], as_index = False)['AGE'].mean()
        print('The average age of women and men that have currently the title CFO:', av_age_gendercfo)
    
        return 


    def average_salary_of_ceo_by_gender(data):
        '''
        This function calculates the average salary between 
        men and women that currently have the title CEO and CFO
        '''
        # average salary women VS men CEOs
        av_salary_ceo_gender = data.groupby(['GENDER', 'PCEO'], as_index= False)['SALARY'].mean()
        print('The average salary of women and men that have currently the title CEO',av_salary_ceo_gender)
        # average salary women VS men CFOs
        av_salary_cfo_gender = data.groupby(['GENDER','PCFO'], as_index= False)['SALARY'].mean()
        print('The average salary of women and men that have currently the title CFO',av_salary_cfo_gender)
        
        # average 1 year total compansation of women VS men CEOs and CFOs 
        av_tdc1_ceo_gender = data.groupby(['GENDER', 'PCEO'], as_index = False)['TDC1'].mean()
        print('The average 1 year total compensation of women VS men that currently have the title CEO',
              av_tdc1_ceo_gender)
        av_tdc1_cfo_gender = data.groupby(['GENDER', 'PCFO'], as_index = False)['TDC1'].mean()
        print('The average 1 year total compensation of women VS men that currently have the title CFO',
              av_tdc1_cfo_gender)
        
        # average 2 year total compensation of women VS men CEOs and CFOs
        av_tdc2_ceo_gender = data.groupby(['GENDER', 'PCEO'], as_index = False)['TDC2'].mean()
        print('The average 2 year total compensation of women VS men that have currently the title CEO',
              av_tdc2_ceo_gender)
        av_tdc2_cfo_gender = data.groupby(['GENDER', 'PCFO'], as_index = False)['TDC2'].mean()
        print('The average 2 year total compensation of women VS men that have currently the title CFO',
              av_tdc2_cfo_gender)
        
        return 
    
    
    def ceo_cfo_gender(data):
        '''
        This function calculates the number of women 
        and men that have the title of the CEO or the 
        CFO at least once during their working career, 
        and every other information that has been calculated 
        previously for the current CEOs and CFOs
        '''
        
        # number of ceos in the dataset
        ceo_counts = data['CEO_NEW'].value_counts()
        print('The number of executives that had at least once the title of the CEO:', ceo_counts)
        
        # number of the cfos in the dataset
        cfo_counts = data['CFO_NEW'].value_counts()
        print('The number of the executives that had at least once the title of the CFO:', cfo_counts)
        
        # ceo and gender
        ceo_gender = data.groupby(['CEO_NEW', 'GENDER'])['EXEC_FULLNAME']
        calculate_ceo_gender = ceo_gender.count()
        print('How many women and men have had the title CEO at least once',
              calculate_ceo_gender)
    
        # cfo and gender
        cfo_gender = data.groupby(['CFO_NEW', 'GENDER'])['EXEC_FULLNAME']
        calculate_cfo_gender = cfo_gender.count()
        print('How many women and men have had the title CFO at least once', 
              calculate_cfo_gender)
        
        # average age of ceos
        av_age_ceos_gender = data.groupby(['GENDER', 'CEO_NEW'], as_index= False)['AGE'].mean()
        print('The average age of women VS men that have had at least once the title CEO',
              av_age_ceos_gender)
        
        # average age of cfos
        av_age_cfos_gender = data.groupby(['GENDER', 'CFO_NEW'], as_index = False)['AGE'].mean()
        print('The average age of women VS men that have had at least once the title CFO', 
              av_age_cfos_gender)
        
        #average salary of ceos
        av_sal_ceos_gender = data.groupby(['GENDER', 'CEO_NEW'], as_index= False)['SALARY'].mean()
        print('The average salary of women Vs men that have had at least once the title CEO', 
              av_sal_ceos_gender)
        
        # average salary of cfos
        av_sal_cfos_gender = data.groupby(['GENDER', 'CFO_NEW'], as_index= False)['SALARY'].mean()
        print('The average salary of women Vs men that have had at least once the title CFO', 
              av_sal_cfos_gender)
        
        # average total 1 year compensation of ceos
        av_tdc1_ceos_gender = data.groupby(['GENDER', 'CEO_NEW'], as_index= False)['TDC1'].mean()
        print('The average total 1 year compensation of women VS men that have had at least once the CEO title',
              av_tdc1_ceos_gender)
        # average total 1 year compensation of cfos
        av_tdc1_cfos_gender = data.groupby(['GENDER', 'CFO_NEW'], as_index = False)['TDC1'].mean()
        print('The average total 1 year compensation of women VS men that have had at least once the title CFO',
              av_tdc1_cfos_gender)
        
        # average total 2 year compensation of ceos
        av_tdc2_ceos_gender = data.groupby(['GENDER', 'CEO_NEW'], as_index = False)['TDC2'].mean()
        print('The average total 2 year compensation of women VS men that have had at least once the title CEO',
              av_tdc2_ceos_gender)
        # average total 2 year compensation of cfos
        av_tdc2_cfos_gender = data.groupby(['GENDER','CFO_NEW'], as_index = False)['TDC2'].mean()
        print('The average total 2 year compensation of women VS men that have had at least once the titls CFO',
              av_tdc2_cfos_gender)
        
        return 
        
    
    def bonus_gender(data):
        '''
        The current function calculates the bonus 
        differences between men and women and between 
        the executives that have the title CEO and CFO
        '''
        
        # bonus differences between men and women in average
        av_bonus_gender = data.groupby('GENDER', as_index = False)['BONUS'].mean()
        print('The average bonus men VS women', av_bonus_gender)
        
        # bonus differences of women VS men current CEOs and CFOs
        av_bonus_pceo = data.groupby(['GENDER', 'PCEO'], as_index = False)['BONUS'].mean()
        print('The average bonus men VS women that are currently CEOs', av_bonus_pceo)
        av_bonus_pcfo = data.groupby(['GENDER', 'PCFO'], as_index = False)['BONUS'].mean()
        print('The average bonus men VS women that are currently CFOs', av_bonus_pcfo)
        
        # bonus differences of women VS men that have been CEO and CFO at least once
        av_bonus_ceo = data.groupby(['GENDER', 'CEO_NEW'], as_index = False)['BONUS'].mean()
        print('The average bonus differences of men VS women that were CEOs at least once',
              av_bonus_ceo)
        av_bonus_cfo = data.groupby(['GENDER', 'CFO_NEW'], as_index = False)['BONUS'].mean()
        print('The average bonus differences of men VS women that were CFOs at least once',
              av_bonus_cfo)
        
        return
        