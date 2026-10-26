def czy_pierwsza(n):
    """
    Badanie pierwszości liczby naturalnej metodą dzielników postaci 6i - 1 oraz 6i + 1.
    Podręcznik: 'Informatyka na czasie 2', s. 78, Ćwiczenie 2.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
        
    return True

# Test algorytmu
print("--- Sprawdzanie czy podana liczba jest pierwsza ---")
liczby = [1, 2, 3, 4, 17, 25, 29, 49, 97, 100]
for num in liczby:
    status = "PIERWSZA" if czy_pierwsza(num) else "ZŁOŻONA / INNA"
    print(f"Liczba {num} -> {status}")
