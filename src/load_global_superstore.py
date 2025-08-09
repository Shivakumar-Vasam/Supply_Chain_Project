import pandas as pd

# Function to load order and return data from train.csv
def load_orders():
    
    # Load the data
    orders = pd.read_excel('./data/Global_Superstore.xls', sheet_name='Orders')
    returns = pd.read_excel('./data/Global_Superstore.xls', sheet_name='Returns')
    people = pd.read_excel('./data/Global_Superstore.xls', sheet_name='People')


    return orders, returns,people




