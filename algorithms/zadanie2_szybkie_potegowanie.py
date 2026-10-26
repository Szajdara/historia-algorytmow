def szybkie_potegowanie(x, n):
    """
    Algorytm szybkiego podnoszenia do potęgi.
    Podręcznik: 'Informatyka na czasie 2', s. 58, Ćwiczenie 7.
    """
    y = 1
    tmp = x
    wykladnik = n
    while wykladnik > 0:
        if wykladnik % 2 == 1:
            y = y * tmp
        wykladnik = wykladnik // 2
        if wykladnik > 0:
            tmp = tmp * tmp
    return y

# Test algorytmu
print("--- Algorytm szybkiego podnoszenia do potęgi ---")
przykłady = [(3, 13), (2, 10), (5, 4), (7, 5)]
for podstawa, wykladnik in przykłady:
    wynik = szybkie_potegowanie(podstawa, wykladnik)
    print(f"{podstawa}^{wykladnik} = {wynik}")
