def dec_to_bin(d):
    """
    Zamiana liczby dziesiętnej na postać dwójkową.
    Podręcznik: 'Informatyka na czasie 2', s. 50, Ćwiczenie 1.
    """
    if d == 0:
        return "0"
    b = ""
    liczba = d
    while liczba > 0:
        if liczba % 2 == 0:
            b = "0" + b
        else:
            b = "1" + b
        liczba = liczba // 2
    return b

# Test algorytmu
liczby = [26, 13, 45, 128]
print("--- Algorytm zamiany liczby dziesiętnej na dwójkową ---")
for liczba in liczby:
    print(f"Liczba {liczba} (dec) = {dec_to_bin(liczba)} (bin)")
