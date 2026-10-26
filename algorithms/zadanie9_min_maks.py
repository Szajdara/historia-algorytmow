def mini_maks(A):
    """
    Jednoczesne znajdowanie minimum i maksimum przy optymalnej liczbie porównań (~3n/2).
    Podręcznik: 'Informatyka na czasie 2', s. 161, Ćwiczenie 4.
    """
    n = len(A)
    if n == 0:
        return None, None
        
    if n % 2 == 1:
        mini = A[0]
        maks = A[0]
        i = 1
    else:
        if A[0] > A[1]:
            mini = A[1]
            maks = A[0]
        else:
            mini = A[0]
            maks = A[1]
        i = 2
        
    while i < n - 1:
        if A[i] > A[i + 1]:
            if A[i + 1] < mini:
                mini = A[i + 1]
            if A[i] > maks:
                maks = A[i]
        else:
            if A[i] < mini:
                mini = A[i]
            if A[i + 1] > maks:
                maks = A[i + 1]
        i += 2
        
    return mini, maks

# Test algorytmu
print("--- Jednoczesne wyszukiwanie minimum i maksimum (MiniMaks) ---")
tablica = [14, 3, 9, 27, 1, 42, 8, 19]
najmniejszy, najwiekszy = mini_maks(tablica)
print("Tablica:", tablica)
print(f"Najmniejszy element (MIN): {najmniejszy}")
print(f"Największy element (MAX):   {najwiekszy}")
