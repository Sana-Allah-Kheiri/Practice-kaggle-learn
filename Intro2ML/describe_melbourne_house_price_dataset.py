#including essential library 
import pandas as pd
# first save dataset path in a variable
dataset_path = 'C:/Users/Paratopic/Documents/kaggle_Intro2ML/melbourn_house_price/melb_data.csv'
# read the data and store data in a DataFrame
melbourne_data = pd.read_csv(dataset_path) 
# print a summary of the data in dataFrame
print(melbourne_data.describe() )
