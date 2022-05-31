import pandas as pd


class DataCleaner:
    def __init__(self):
        pass
    
    # implementing a function to create dummies
    def to_dummies(self, raw_categories):
        stripped_categories = raw_categories.str.strip()
        categories = pd.Categorical(stripped_categories.astype('category'))
        dummies = categories.codes
        
        return dummies
    
    # cleaning data function
    def clean_data(self, raw_ceo_data):
        clean_ceo_data = pd.DataFrame(raw_ceo_data)
        
        # create dummies
        #clean_ceo_data['gender']= self.to_dummies(clean_ceo_data['gender'])
        
        return clean_ceo_data