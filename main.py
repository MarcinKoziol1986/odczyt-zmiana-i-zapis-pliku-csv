"""Napisz program, który odczyta wejściowy plik CSV, następnie zmodyfikuje go i
wyświetli w terminalu jego zawartość, a na końcu zapisze w wybranej lokalizacji.

Uruchomienie programu przez terminal:
python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

 <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv
 <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv
<zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są
współrzędnymi liczonymi od 0, natomiast "wartosc" zmianą która ma trafić na
podane miejsce.

Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "iris.csv".

plik iris.csv zmodyfikowany
"""

import sys
import csv
import pprint

plik_wejsciowy = sys.argv[1]
plik_wyjsciowy = sys.argv[2]
zmiany_csv = sys.argv[3:]
tabela = []
with open(plik_wejsciowy, 'r') as f:
    odczytany_plik = csv.reader(f, delimiter=',')
    for row in odczytany_plik:
        tabela.append(row)
    pprint.pprint(tabela)
    for zmiana in zmiany_csv:
        wiersz, kolumna , nowa_zmiana = zmiana.split(",")
        wiersz = int(wiersz)
        kolumna = int(kolumna)
        tabela[wiersz][kolumna] = nowa_zmiana
    pprint.pprint(tabela)
with open(plik_wyjsciowy, 'w') as plikcsv:
    csvwriter = csv.writer(plikcsv, delimiter=',')
    csvwriter.writerows(tabela)

