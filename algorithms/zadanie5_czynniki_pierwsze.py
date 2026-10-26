def rozklad_na_czynniki_pierwsze(n):
    """
    Rozkład liczby naturalnej na czynniki pierwsze z optymalizacją.
    Podręcznik: 'Informatyka na czasie 2', s. 80-81, Ćwiczenie 4.
    """
    czynniki = []
    liczba = n
    
    # Czynnik 2 w osobnej pętli
    while liczba % 2 == 0:
        czynniki.append(2)
        liczba = liczba // 2
        
    # Czynniki nieparzyste d = 3, 5, 7, ...
    d = 3
    while d * d <= liczba:
        if liczba % d == 0:
            czynniki.append(d)
            liczba = liczba // d
        else:
            d += 2
            
    if liczba > 1:
        czynniki.append(liczba)
        
    return czynniki

# Test algorytmu
print("--- Rozkład liczby na czynniki pierwsze ---")
test_liczby = [456, 84, 100, 315, 997]
for val in test_liczby:
    cz = rozklad_na_czynniki_pierwsze(val)
    print(f"{val} = {' * '.join(map(str, cz))}")
