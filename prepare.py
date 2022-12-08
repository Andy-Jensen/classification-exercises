from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


def tts(df):
    x=input('stratify=')
    train_validate, test=train_test_split(df, 
                                 train_size=.8, 
                                 random_state=8675309, 
                                 stratify=df[x])
                
    train, validate =train_test_split(train_validate, 
                                      test_size=.3, 
                                      random_state=8675309, 
                                      stratify=train_validate[x])
    return train, validate, test