def sortowanie_babelkowe(A):
    """
    Sortowanie bąbelkowe tablicy niemalejąco z flagą zamiany.
    Podręcznik: 'Informatyka na czasie 2', s. 173, Ćwiczenie 1.
    """
    tab = list(A)
    n = len(tab)
    for i in range(1, n):
        zamiana = False
        for j in range(0, n - i):
            if tab[j] > tab[j + 1]:
                pom = tab[j]
                tab[j] = tab[j + 1]
                tab[j + 1] = pom
                zamiana = True
        if not zamiana:
            break
    return tab

# Test algorytmu
print("--- Sortowanie bąbelkowe (Bubble Sort) ---")
dane = [6, 4, 9, 1, 5]
print("Przed posortowaniem:", dane)
posortowane = sortowanie_babelkowe(dane)
print("Po posortowaniu:    ", posortowane)
