import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    
    """ Load the datasets and megre them """ 
    
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, how='outer', on=['id'])
    return df
    #pass


def clean_data(df):
    
    """ clean the df """
    
    categories = df['categories'].str.split(';', expand=True)
    row = categories.head(1)
    category_colnames = row.applymap(lambda x: x[:-2]).iloc[0,:]
    categories.columns = category_colnames
    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1]
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
        # replace related_2 to related_1 in related column
        categories['related'] = categories['related'].replace(to_replace=2, value=1)
    
    #drop the original categories from df  
    df = df.drop(['categories'], axis=1)
    #concat df with new categories data
    df = pd.concat([df,categories], axis=1)
    #drop duplicates
    df = df.drop_duplicates()
    return df
    


def save_data(df, database_filepath):
    engine = create_engine(f'sqlite:///{database_filepath}')
    df.to_sql('disastermesseages', engine, index=False)
    #pass  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()