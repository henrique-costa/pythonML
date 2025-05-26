import csv


# with open("ProductsTable2.csv", mode='r', encoding='utf-8') as csvFile:
#     readerCsv = csv.reader(csvFile)
#     for linha in readerCsv:
#         print(linha)   


csvFile = open("ProductsTable2.csv", encoding='utf-8-sig')
readerCsv = csv.reader(csvFile, delimiter=';')

# for i in readerCsv:
#     linha1 = csvFile.readline()
#     print("Linha :", linha1.strip())

print("Items to buy:")

for item in readerCsv:
    code = item[0]
    name = item[1]
    stock = int(item[2])
    maxStock = int(item[3])

    if (stock == 0) or (stock < (maxStock * 5 / 100)):
        print(code + " - " + name)



