import pandas as pd

#this is a code for reading csv files.

def read_csv1(filepath1, header1, datatype1, column_name):
    table = pd.read_csv(filepath1, header=header1, dtype=float, usecols=column_name)
    return table
