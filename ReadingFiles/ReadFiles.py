import csv
import pandas as pd

archive = open("Products.txt", 'rt')

for line in archive.readlines():
     print(line)
     
print("\nend txt file read\n")

archive = open("Products.txt", 'rt')

print(archive.readline())
print(archive.readline())
print(archive.readline())
print(archive.readline())

print("\nend txt file read line by line\n")


leitorCSV = csv.reader('mycsv.csv')

# with open('mycsv.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile)
#     for row in spamreader:
#         print(', '.join(row))

with open('mycsv.csv', newline='', encoding='utf-8-sig') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        print('-'.join(row))


print("\nend csv file read\n")


# lê todas as planilhas (retorna dict de DataFrames)
dfs = pd.read_excel("mycsv.xlsx", sheet_name=None)

# ou lê apenas a 1ª planilha como DataFrame
df = pd.read_excel("mycsv.xlsx", sheet_name=0)

print(df.head())

print("\n")

archive = open("mycsv.csv", 'rt', encoding='utf-8-sig')
reader = csv.reader(archive, delimiter=',')

for lines in reader:
    print(lines)

print("\n")


with open("mycsv.csv", "r", newline='', encoding="utf-8") as archiveCSV:
    reader = csv.reader(archiveCSV, delimiter=';')
    for row in reader:
        print("Element: " + row[0] + " = " + row[1])