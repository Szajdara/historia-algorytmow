def czy_palindrom(wyraz):
    """
    Sprawdzanie, czy wyraz jest palindromem (niezależnie od wielkości liter).
    Podręcznik: 'Informatyka na czasie 2', s. 63, Ćwiczenie 1.
    """
    s = wyraz.lower()
    i = 0
    j = len(s) - 1
    palindrom = True
    
    while palindrom and i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            palindrom = False
            
    return palindrom

# Test algorytmu
print("--- Sprawdzanie, czy wyraz jest palindromem ---")
slowa = ["Kajak", "radar", "Informatyka", "potop", "Programowanie", "Anna"]
for w in slowa:
    wynik = "TAK" if czy_palindrom(w) else "NIE"
    print(f"Czy słowo '{w}' to palindrom? -> {wynik}")
