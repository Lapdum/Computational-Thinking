import csv

filename = "Grade.csv"

fields = ['Name', 'Grade', 'Math Score']

rows = [['Timmy', '12', '80'],
        ['Agataha', '12', '100'],
        ['John', '11', '76'],
        ['Bobby', '10', '92'],
        ['Jack', '10', '55']]

with open(filename,'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(rows)

with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    data_list = [row for row in reader]

for data in data_list:
    print(data)