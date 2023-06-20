import csv

def calcular_gastos_parlamentares(arquivo_csv):
    gastos_parlamentares = {}

    with open(arquivo_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            ano = int(row['Ano'])
            parlamentar = row['Parlamentar']
            gasto = float(row['Gasto'])

            if ano >= 2019 and ano <= 2022:
                if parlamentar in gastos_parlamentares:
                    gastos_parlamentares[parlamentar] += gasto
                else:
                    gastos_parlamentares[parlamentar] = gasto

    return gastos_parlamentares

arquivo_csv = 'dados_gastos.csv'  # Substitua pelo nome do seu arquivo CSV

gastos = calcular_gastos_parlamentares(arquivo_csv)

for parlamentar, total_gastos in gastos.items():
    print(f"{parlamentar}: R$ {total_gastos:.2f}")

