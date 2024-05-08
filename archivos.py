import csv

with open('ventas.csv', 'r') as archivo:
    datos_csv = csv.DictReader(archivo)
    for fila in datos_csv:
        print(fila)