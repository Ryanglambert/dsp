import csv
# import pandas as pd  <<<< trying without

def read_file(file_path):
    data = []
    dictionary = {}
    with open(file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    header  = data[0]
    body = data[1:]
    
    for i in range(len(header)):
        column = []
        for row in body:
            column.append(row[i])
        dictionary[header[i]] = column
    return dictionary

faculty = read_file('faculty.csv')
emails = faculty[' email']
for i in emails: 
    print i
