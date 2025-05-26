import csv

archiveCSV = open("ProductsTable.csv", 'rt', encoding='utf-8-sig')
readerCSV = csv.reader(archiveCSV, delimiter=';')

noCupons = 0
acumulatedValue = 0

# for linha in readerCSV:
#     print(linha[0])

for cupom in readerCSV:
    noCupons += 1
    acumulatedValue += float(cupom[1])

AverageValue = acumulatedValue / noCupons

print("Processed " + str(noCupons) + " coupons.")
print("Total accumulated value is " + str(acumulatedValue))
print("Average value per coupon is " + str(AverageValue))
    
print("Num cupom:", noCupons)
print("Acumulated Value:", acumulatedValue)

