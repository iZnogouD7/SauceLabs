import csv
def load_csv_data(file_path):
    rows=[]
    with open(file_path, 'r') as datafile:
        reader = csv.reader(datafile)
        next(reader)
        for row in reader:
            rows.append(tuple(row))
    return rows