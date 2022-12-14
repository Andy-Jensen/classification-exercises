import pandas as pd
import numpy as np
import env
import os
from env import get_connection
def get_titanic():
    if os.path.isfile('titanic.csv'):
        return pd.read_csv('titanic.csv')
    else:
        url = get_connection('titanic_db')
        
        query = '''
                SELECT * FROM passengers
                '''
        
        df = pd.read_sql(query, url)
        df.to_csv('titanic.csv', index=False)
        return df

def get_telco_data():
    if os.path.isfile('telco_churn.csv'):
        return pd.read_csv('telco_churn.csv')
    else:
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
        df.to_csv('telco_churn.csv', index=False)
        return df

def get_iris_data():
    if os.path.isfile('iris_db.csv'):
        return pd.read_csv('iris_db.csv')
    else:
        url = get_connection('iris_db')
        
        query = '''
                SELECT * FROM measurements JOIN species USING(species_id)
                '''
        
        df = pd.read_sql(query, url)
        df.to_csv('iris_db.csv', index=False)
        return df

