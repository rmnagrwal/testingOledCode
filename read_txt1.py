import pandas as pd

#this is a code to read space saperated value text files

def read_txt1(filepath,column_name):
    table = pd.read_table(filepath,delim_whitespace=True, header=0, names=column_name, dtype=float, skiprows=10)
    return table
