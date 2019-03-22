import pandas as pn
from pandas import DataFrame
def parse(file):
        fileformat = file.filename.split('.')[-1] 
        if fileformat == 'csv' or fileformat == 'txt':
                data = pn.read_csv(file)
                return data.to_dict(orient='list')
        if fileformat == 'xls' or fileformat == 'xlsx':
                data = pn.read_excel(file)
                return data.to_dict(orient='list')
        
