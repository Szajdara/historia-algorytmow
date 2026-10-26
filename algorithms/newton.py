def newton_sqrt(n, tol=1e-10):
    if n < 0:
        raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej.")
    if n == 0:
        return 0.0

    x = float(n)
    while True:
        next_x = 0.5 * (x + n / x)
        if abs(next_x - x) < tol:
            return next_x
        x = next_x

liczba = 25
print(f"Pierwiastek z {liczba}: {newton_sqrt(liczba)}")

#Ten algorytm (metoda Newtona-Raphsona) działa jak stopniowe
#  „zgadywanie i poprawianie” pierwiastka: zaczynasz od strzału,
#  że pierwiastkiem z liczby $n$ jest ona sama ($x = n$),
#  a następnie w pętli wyliczasz średnią arytmetyczną
#  z Twojego obecnego strzału $x$ oraz wartości $n / x$ 
# (wzór 0.5 * (x + n / x)) — jeśli $x$ był za duży, 
# to $n / x$ jest za małe, więc ich średnia ląduje
#  niesamowicie blisko prawdziwego wyniku; 
# komputer powtarza to uśrednianie tak długo,
#  aż kolejna poprawka różni się od poprzedniej o
#  mniej niż mikroskopijny margines błędu (tol = 1e-10),
#  błyskawicznie (zazwyczaj w kilka kroków)
#  podając idealnie dokładny pierwiastek, np. $5.0$
#  dla liczby $25$.