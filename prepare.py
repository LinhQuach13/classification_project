import seaborn as sns
import os
from pydataset import data
from scipy import stats
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

import acquire



# ************************************ TELCO DATA***********************************
def clean_data(df):
    '''
    takes in a dataframe of the telco dataset that was acquired before and returns a cleaned dataframe
    arguments:
    - df: a pandas DataFrame with the expected feature names and columns
    '''
    #Add zero to columns to convert to float    
    df['total_charges'] = (df['total_charges'] + '0')
    #make total charges into datatype float
    df['total_charges'] = df['total_charges'].astype('float')
    return df
 

def prep_telco_data(df):
    '''
    takes in a dataframe of the titanic dataset that was acquired before and returns a new dataframe with string/object values transformed into numeric values
    arguments:
    - df: a pandas DataFrame with the expected feature names and columns
    '''
    #clean data
    df = df.drop_duplicates()
    # filters to objects only starting at index 1 to put in dummy dataframe
    col_list= list(df.select_dtypes('object').columns)[1:] 
    #creating dummy dataframe
    dummy_df = pd.get_dummies(df[col_list])
    dummy_df
    #Concatenate the dummy_df dataframe above with the original df
    df = pd.concat([df, dummy_df], axis=1) 
    return df


def corr_telco_data(df):
    '''
    takes in a dataframe of the telco dataset that was acquired before and returns a cleaned dataframe with a correlation table.
    arguments:
    - df: a pandas DataFrame with the expected feature names and columns
    '''
    #creating correlation table
    df=  prep_telco_data(df).corr().reset_index()
    #rename columns in correlation table
    df.rename(columns={"index": "col_names"},  inplace= True)
    #Filter columns to only churn_no and churn_yes and tranpose table
    df= df[(df.col_names=='churn_No') | (df.col_names=='churn_Yes')].T.reset_index()
    #Renaming more columns in correlation table
    df= df.rename(columns={38:"churn_No", 39: "churn_Yes"})
    #Drop first row to be able to sort values
    df= df.drop([0], axis=0)
    #Sort correlation values
    df.sort_values(by='churn_No')
    # drop column 81 and 82
    df.drop(columns= [81, 82], inplace= True)
    return df

def clean_churn(df):
    '''
    takes in a dataframe of the telco dataset that was acquired before and returns a numeric datatype of churn column.
    arguments:
    - df: a pandas DataFrame with the expected feature names and columns
    '''
    # Changing churn column to integer data type
    df['churn']= (df['churn'] == 'Yes').astype(int) 
    #Make new dataframe with numeric columns only
    df= df.select_dtypes(['int64', 'float64', 'uint8' ])
    return df

def telco_split(df):
    '''
    This function take in the telco data acquired by get_telco_data,
    performs a split and stratifies churn column.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test
