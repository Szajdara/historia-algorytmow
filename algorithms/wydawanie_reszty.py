# Algorytm zachłanny - Wydawanie reszty
# Dostępne nominały monet: 5, 2, 1

def wydaj_reszte(kwota, nominaly=[5, 2, 1]):
    wydane_monety = []
    pozostalo = kwota
    i = 0

    while pozostalo > 0 and i < len(nominaly):
        if pozostalo >= nominaly[i]:
            ile = pozostalo // nominaly[i]
            for _ in range(ile):
                wydane_monety.append(nominaly[i])
            pozostalo = pozostalo % nominaly[i]
        i += 1

    return wydane_monety


# Rozwiązanie dla reszty 6 oraz 13 (zgodnie z zadaniem)
for kwota in [6, 13]:
    monety = wydaj_reszte(kwota)
    opis_monet = " + ".join(str(m) for m in monety)
    print(f"=== RESZTA {kwota} ===")
    print(f"Wydane monety: {opis_monet}")
    print(f"Liczba monet:  {len(monety)}\n")
