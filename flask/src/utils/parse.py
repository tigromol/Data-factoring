from pandas import DataFrame, read_csv, read_excel

def parse(file):
        fileformat = file.filename.split('.')[-1] 
        if fileformat == 'csv' or fileformat == 'txt':
                data = read_csv(file)
                return data.to_dict(orient='list')

        if fileformat == 'xls' or fileformat == 'xlsx':
                data = read_excel(file)
                return data.to_dict(orient='list')
        
