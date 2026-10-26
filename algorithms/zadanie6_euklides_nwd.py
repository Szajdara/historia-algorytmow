def nwd_dzielenie(a, b):
    """
    Algorytm Euklidesa z wykorzystaniem operacji dzielenia całkowitego i reszty.
    Podręcznik: 'Informatyka na czasie 2', s. 108, Ćwiczenie 1.
    """
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a

# Test algorytmu
print("--- Algorytm Euklidesa (NWD) z dzieleniem ---")
pary = [(1989, 867), (48, 18), (1071, 462), (35, 14), (100, 25)]
for a, b in pary:
    print(f"NWD({a}, {b}) = {nwd_dzielenie(a, b)}")
