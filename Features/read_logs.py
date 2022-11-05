import pandas

def read_logs(file_path, column ):
    df = pandas.read_csv(file_path)
    print(list(df[column])[-1])
    return list(df[column])[-1]
