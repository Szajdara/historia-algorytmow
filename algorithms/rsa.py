import math

def mod_inverse(e, phi):
    """Oblicza d takie, że (d * e) % phi == 1"""
    d_nowy, d = 1, 0
    r_nowy, r = e, phi
    
    while r_nowy != 0:
        kraj = r // r_nowy
        d, d_nowy = d_nowy, d - kraj * d_nowy
        r, r_nowy = r_nowy, r - kraj * r_nowy
        
    if r > 1:
        raise ValueError("Liczby nie są względnie pierwsze!")
    if d < 0:
        d += phi
    return d

# 1. Wybór liczb pierwszych
p, q = 3, 11
n = p * q
phi = (p - 1) * (q - 1)

# 2. Wybór e
e = 3
assert math.gcd(e, phi) == 1, "e i phi muszą być względnie pierwsze!"

# 3. Obliczenie d (działa bez problemu w Skulpt)
d = mod_inverse(e, phi)

# 4. Szyfrowanie i Odszyfrowanie
wiadomosc = 5
szyfrogram = pow(wiadomosc, e, n)
odszyfrowana = pow(szyfrogram, d, n)

print(f"Klucz publiczny: (e={e}, n={n})")
print(f"Klucz prywatny:  (d={d}, n={n})")
print(f"Wiadomość: {wiadomosc} -> Zaszyfrowana: {szyfrogram} -> Odszyfrowana: {odszyfrowana}")

#To miniaturowa demonstracja kryptografii asymetrycznej RSA,
#  która działa jak kłódka z dwoma różnymi kluczami:
#  bierze dwie małe liczby pierwsze ($p=3, q=11$)
#  i mnoży je w moduł $n=33$, tworząc z liczby $e=3$
#  ogólnodostępny klucz publiczny $(e, n)$, 
# którym każdy może zablokować wiadomość przez potęgowanie
#  modularne ($5^3 \bmod 33 = 26$), a klucz do otwarcia tej 
# kłódki — klucz prywatny $(d, n)$ — oblicza za pomocą
#  rozszerzonego algorytmu Euklidesa (mod_inverse),
#  znajdującego taką liczbę $d=7$, która w matematyce 
# zegarowej idealnie odwraca działanie potęgi $e$,
#  dzięki czemu tylko właściciel sekretu $d$ jest w 
# stanie z powrotem odczytać ukrytą treść ($26^7 \bmod 33 = 5$),
#  podczas gdy postronny obserwator musiałby najpierw mozolnie
#  rozbić duży iloczyn $n$ z powrotem na liczby pierwsze
#  $p$ i $q$, co w świecie prawdziwych, 600-cyfrowych liczb
#  jest dla komputerów praktycznie niewykonalne.