from pandas import DataFrame, read_csv, read_excel

def parse(file, **kwargs):
    print(file)
    print(dir(file))
    fileformat = file.name.split('.')[-1] 
    if fileformat == 'csv' or fileformat == 'txt':
        data = read_csv(file, skipinitialspace=True, sep=',\s+', delimiter=',', **kwargs).rename(columns=lambda x: x.strip())
        return data.to_dict(orient='list')

    if fileformat == 'xls' or fileformat == 'xlsx':
        data = read_excel(file,  skipinitialspace=True, sep=',\s+', delimiter=',',**kwargs).rename(columns=lambda x: x.strip())
        return data.to_dict(orient='list')

