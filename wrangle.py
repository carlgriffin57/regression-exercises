import numpy as np
import pandas as pd
import os

# Enables access to my env.py file in order to use sensitive info to access Codeup DB

from env import host, username, password

# sets up a secure connection to the Codeup db using my login infor
def get_db_url(db, user=username, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# assigns the telco_churn url to the variable name 'url' so it can be used in additional functions
url = get_db_url('telco_churn')

def get_connection(db, user=username, host=host, password=password):
    '''
    This function uses my env file to create a connection url to access
    the Codeup database. '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def new_telco_data():
    '''
    This function reads data from the Codeup db into a df.
    '''

    sql_query = '''SELECT customer_id, monthly_charges, tenure, total_charges
                FROM customers
                WHERE contract_type_id = 3;'''
    return pd.read_sql(sql_query, get_connection('telco_churn'))

def get_telco_data():
    '''
    This function reads in Telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco_df.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_telco_data()
     
        # Cache data
        df.to_csv('telco_df.csv')
        
    return df

def prep_telco_data(df):
    '''
    This function handles nulls, duplicates, strings and then returns the df
    '''
    # drop any duplicates
    df.drop_duplicates(inplace=True)
    
    # fill any empty spaces with np.nan
    df.replace(' ', np.nan, inplace=True)
    
    # drop rows that contain null values, they are a small percentage
    df.dropna(axis=0, inplace=True)
    
    # convert total_charges to a numeric data type
    df = df.astype({'total_charges': 'float64'})

    # No computations will be done on 'customer_id' so make that column the index.
    df.set_index('customer_id', drop=True, inplace=True)
    
    return df

   ########################## wrangle function ############################
def wrangle_telco():
    '''
    This function will utilize the routines above to acquire the telco data and prep it.
    '''
    df = get_telco_data()
    df = prep_telco_data(df)
    return df

    