import csv

shopping_centers = [
    {"id": 1, "name": "Itis", "addr": "Itäkatu 1-7, 00930 Helsinki, Finland"},
    {"id": 2, "name": "Forum", "addr": "Mannerheimintie 20, 00100 Helsinki, Finland"},
    {"id": 3, "name": "Iso Omena", "addr": "Piispansilta 11, 02230 Espoo, Finland"},
    {"id": 4, "name": "Sello", "addr": "Leppävaarankatu 3-9, 02600 Espoo, Finland"},
    {"id": 5, "name": "Jumbo", "addr": "Vantaanportinkatu 3, 01510 Vantaa, Finland"},
    {"id": 6, "name": "REDI", "addr": "Hermannin rantatie 5, 00580 Helsinki, Finland"},
    {"id": 7, "name": "Tripla", "addr": "Fredikanterassi 1, 00520 Helsinki, Finland"}
]

file_name = "shopping_centers.txt"

fieldnames = ["id", "name", "addr"]

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for shopping_center in shopping_centers:
        writer.writerow(shopping_center)