def szyfruj_cezar(tekst, klucz):
    """
    Szyfr Cezara z operacją mod 26 (obsługa wielkich i małych liter).
    Podręcznik: 'Informatyka na czasie 2', s. 120, Ćwiczenie 2.
    """
    szyfrogram = ""
    klucz = klucz % 26
    
    for c in tekst:
        if 'A' <= c <= 'Z':
            kod = (ord(c) - ord('A') + klucz) % 26 + ord('A')
            szyfrogram += chr(kod)
        elif 'a' <= c <= 'z':
            kod = (ord(c) - ord('a') + klucz) % 26 + ord('a')
            szyfrogram += chr(kod)
        else:
            szyfrogram += c
            
    return szyfrogram

# Test algorytmu
print("--- Szyfr Cezara z operacją modulo ---")
jawny = "INFORMATYKA NA CZASIE"
k = 3
zaszyfrowany = szyfruj_cezar(jawny, k)
print(f"Tekst jawny:     '{jawny}'")
print(f"Klucz:           {k}")
print(f"Tekst zaszyfr.:  '{zaszyfrowany}'")
