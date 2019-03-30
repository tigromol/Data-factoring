from pandas import DataFrame, read_csv, read_excel

def parse(file, rows_count=500):
    fileformat = file.filename.split('.')[-1] 
    if fileformat == 'csv' or fileformat == 'txt':
        data = read_csv(file, nrows=rows_count, skipinitialspace=True, sep=',\s+', delimiter=',').rename(columns=lambda x: x.strip())
        return data.to_dict(orient='list')

    if fileformat == 'xls' or fileformat == 'xlsx':
        data = read_excel(file, nrows=rows_count, skipinitialspace=True, sep=',\s+', delimiter=',').rename(columns=lambda x: x.strip())
        return data.to_dict(orient='list')

