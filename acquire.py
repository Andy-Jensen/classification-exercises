
#import libraries and the 'get_connection' function from env
import pandas as pd
import numpy as np
import env
import os
from env import get_connection

def get_titanic():
    '''
    looking for an already existing titanic csv on the local machine
    '''
    if os.path.isfile('titanic.csv'):
        return pd.read_csv('titanic.csv')
    else:
        '''
        if there is no existing csv, then connect to the SQL server and get the information from 
        titanic_db
        '''
        url = get_connection('titanic_db')
        
        query = '''
                SELECT * FROM passengers
                '''
        
        df = pd.read_sql(query, url)
        '''
        saving the newly queried SQL table to a csv so it
        can be used instead of connecting to the SQL server
        every time I want this info
        '''
        df.to_csv('titanic.csv', index=False)
        return df

def get_telco_data():
    '''
    looking for an already existing telco_churn csv on the local machine
    '''
    if os.path.isfile('telco_churn.csv'):
        return pd.read_csv('telco_churn.csv')
    else:
        '''
        if there is no existing csv, then connect to the SQL server and get the information from 
        telco_churn db
        '''
        url = get_connection('telco_churn')
        
        query = '''
                SELECT *
                FROM customers
                JOIN contract_types USING(contract_type_id)
                JOIN internet_service_types USING(internet_service_type_id)
                JOIN payment_types USING(payment_type_id)
                JOIN customer_signups USING(customer_id)
                LEFT JOIN customer_churn USING(customer_id)
                '''
        
        df = pd.read_sql(query, url)
        '''
        saving the newly queried SQL table to a csv so it
        can be used instead of connecting to the SQL server
        every time I want this info
        '''
        df.to_csv('telco_churn.csv', index=False)
        return df

def get_iris_data():
    '''
    looking for an already existing iris csv on the local machine
    '''
    if os.path.isfile('iris_db.csv'):
        return pd.read_csv('iris_db.csv')
    else:
        '''
        if there is no existing csv, then connect to the SQL server and get the information from 
        iris_db
        '''
        url = get_connection('iris_db')
        
        query = '''
                SELECT * FROM measurements JOIN species USING(species_id)
                '''
        
        df = pd.read_sql(query, url)
        '''
        saving the newly queried SQL table to a csv so it
        can be used instead of connecting to the SQL server
        every time I want this info
        '''
        df.to_csv('iris_db.csv', index=False)
        return df

