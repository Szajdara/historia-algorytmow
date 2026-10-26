def simplex_dydaktyczny():
    # Tablica Simplex dla problemu:
    # Max Z = 3x + 5y --> Z - 3x - 5y = 0
    # 1) 1x + 0y + s1 = 4
    # 2) 0x + 2y + s2 = 12
    # 3) 3x + 2y + s3 = 18
    # Macierz: [x, y, s1, s2, s3, RHS]
    tablica = [
        [1.0, 0.0, 1.0, 0.0, 0.0,  4.0],
        [0.0, 2.0, 0.0, 1.0, 0.0, 12.0],
        [3.0, 2.0, 0.0, 0.0, 1.0, 18.0],
        [-3.0, -5.0, 0.0, 0.0, 0.0,  0.0]  # Wiersz funkcji celu
    ]

    wiersze = len(tablica) - 1
    kolumny = len(tablica[0]) - 1

    while True:
        # 1. Szukamy kolumny z najbardziej ujemną wartością w ostatnim wierszu
        kolumna_pivot = min(range(kolumny), key=lambda j: tablica[-1][j])
        if tablica[-1][kolumna_pivot] >= 0:
            break  # Brak wartości ujemnych = znaleziono optymum!

        # 2. Szukamy wiersza pivotującego (najmniejszy dodatni iloraz RHS / element)
        ilorazy = []
        for i in range(wiersze):
            val = tablica[i][kolumna_pivot]
            if val > 0:
                ilorazy.append((tablica[i][-1] / val, i))
            else:
                ilorazy.append((float('inf'), i))
        
        wiersz_pivot = min(ilorazy, key=lambda x: x[0])[1]

        # 3. Normalizacja wiersza pivotującego
        element_pivot = tablica[wiersz_pivot][kolumna_pivot]
        tablica[wiersz_pivot] = [x / element_pivot for x in tablica[wiersz_pivot]]

        # 4. Eliminacja elementów w pozostałych wierszach
        for i in range(wiersze + 1):
            if i != wiersz_pivot:
                wspolczynnik = tablica[i][kolumna_pivot]
                tablica[i] = [tablica[i][j] - wspolczynnik * tablica[wiersz_pivot][j] for j in range(kolumny + 1)]

    # Odczyt wyników
    x = tablica[0][-1] if tablica[0][0] == 1 else (tablica[2][-1] if tablica[2][0] == 1 else 0)
    y = tablica[1][-1] / 2.0 if tablica[1][1] == 2.0 else tablica[1][-1]
    zysk = tablica[-1][-1]

    print(f"Znalezione optymum Simplex: x = {round(x, 2)}, y = {round(y, 2)}")
    print(f"Maksymalny zysk Z = {round(zysk, 2)}")

simplex_dydaktyczny()

#Algorytm Simplex działa jak wspinaczka po narożnikach
#  ogrodzonej działki w poszukiwaniu najwyższego punktu:
#  zamienia ograniczenia produkcyjne 
# (np. limity surowców i czasu) na równania z dodatkowymi
#  „luzami” ($s_1, s_2, s_3$) i zapisuje je w tabeli,
#  po czym w każdej rundzie sprawdza wiersz zysku,
#  by wybrać towar dający najszybszy zarobek
#  (najbardziej ujemna liczba w ostatnim wierszu wskazuje
#  kolumnę pivota, na start zmienną $y$), następnie przez
#  dzielenie zasobów (RHS) wybiera „wąskie gardło”,
#  które skończy się najszybciej (najmniejszy iloraz
#  wyznacza wiersz pivota), a potem metodą operacji 
# na wierszach (eliminacja Gaussa) przeskakuje do tego 
# nowego, lepszego wierzchołka; powtarza te przeskoki 
# tak długo, aż w dolnym wierszu nie ma już żadnych 
# ujemnych liczb — co oznacza, że żaden ruch nie przyniesie
#  już większego zysku i osiągnięto absolutne maksimum 
# (tutaj $x=2, y=6$, dające zysk $Z=36$).