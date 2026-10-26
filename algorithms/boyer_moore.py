def boyer_moore(tekst, wzorzec):
    n, m = len(tekst), len(wzorzec)
    # Tablica przesunięć: zapamiętuje ostatni indeks każdego znaku we wzorcu
    bad_char = {char: i for i, char in enumerate(wzorzec)}

    s = 0  # Przesunięcie wzorca względem tekstu
    while s <= n - m:
        j = m - 1
        # Porównanie od prawej do lewej
        while j >= 0 and wzorzec[j] == tekst[s + j]:
            j -= 1

        if j < 0:
            return s  # Znaleziono wzorzec

        # Przeskok: wyrównaj niedopasowany znak lub przesuń o min. 1 pozycję
        s += max(1, j - bad_char.get(tekst[s + j], -1))

    return -1

tekst = "PROGRAMOWANIE ALGORYTMOW"
wzorzec = "RYM"
print("Indeks:", boyer_moore(tekst, wzorzec))

#Algorytm Boyera-Moore’a (tutaj w uproszczonej
#  wersji z regułą złego znaku – Bad Character Rule)
#  działa jak czytanie przez lupę od tyłu: przykłada
#  wzorzec do tekstu i zamiast sprawdzać literka po 
# literce od początku, porównuje znaki od prawej do 
# lewej strony wzorca. Gdy trafi na literę, która się
#  nie zgadza (tzw. zły znak w tekście), sprawdza
#  w przygotowanym wcześniej słowniku (bad_char),
#  gdzie ta litera w ogóle występuje w poszukiwanym 
# słowie. Jeśli litera w nim jest, algorytm przesuwa
#  cały wzorzec w prawo tak, aby dopasować do siebie
#  te same litery; jeśli litery nie ma w całym wzorcu,
#  przeskakuje go bez wahania za ten znak
#  (czyli o kilka pozycji naraz zamiast mozolnego sprawdzania
#  o 1). W podanym przykładzie szuka "RYM" w "PROGRAMOWANIE
#  ALGORYTMOW": omija całe bloki tekstu dużymi krokami,
#  aż natrafi na dopasowanie na indeksie 19, co daje o 
# wiele większą szybkość niż zwykłe sprawdzanie litera 
# po literze.