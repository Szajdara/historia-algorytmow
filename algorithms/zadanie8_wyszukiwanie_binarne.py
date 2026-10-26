def szukaj_bin(tablica, x):
    """
    Przeszukiwanie binarne w posortowanej tablicy liczb.
    Podręcznik: 'Informatyka na czasie 2', s. 157, Ćwiczenie 3.
    """
    lewy = 0
    prawy = len(tablica) - 1
    
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if tablica[srodek] == x:
            return srodek  # Zwracamy indeks
        elif tablica[srodek] < x:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
            
    return -1  # Nie znaleziono

# Test algorytmu
print("--- Wyszukiwanie binarne w uporządkowanym zbiorze ---")
A = [1, 4, 5, 6, 9, 12, 17, 24, 30]
print("Tablica wejściowa:", A)
szukane = [5, 3, 17, 25]
for cel in szukane:
    pozycja = szukaj_bin(A, cel)
    if pozycja != -1:
        print(f"Liczba {cel} -> ZNALEZIONA pod indeksem {pozycja}")
    else:
        print(f"Liczba {cel} -> NIE ZNALEZIONO w tablicy")
