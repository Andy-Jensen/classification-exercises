from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

#function for doing train test split on any dataset
def tts(df):
    '''
    assigning the column of the dataframe that you want to stratify by
    '''
    x=input('stratify=')
    '''
    removing your test data from the data
    '''
    train_validate, test=train_test_split(df, 
                                 train_size=.8, 
                                 random_state=8675309, 
                                 stratify=df[x])
    '''
    splitting the remaining data into the train and validate groups
    '''            
    train, validate =train_test_split(train_validate, 
                                      test_size=.3, 
                                      random_state=8675309, 
                                      stratify=train_validate[x])
    return train, validate, test