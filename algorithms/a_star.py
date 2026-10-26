# Algorytm A*
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

start = (0, 0)
cel = (3, 3)
pozycja_aktualna = (1, 2)

g_score = 3
h_score = manhattan(pozycja_aktualna, cel)
f_score = g_score + h_score

print(f"Pozycja: {pozycja_aktualna}, Cel: {cel}")
print(f"g(n) [koszt dotychczasowy] = {g_score}")
print(f"h(n) [heurystyka do celu] = {h_score}")
print(f"f(n) = g(n) + h(n) = {f_score}")    

#Algorytm A* działa jak sprytny pieszo-GPS
#  na siatce ulic: ocenia każde pole, dodając
#  kroki już zrobione od startu (g, czyli przeszłość)
#  do szacowanej liczby kratek, jaka została w linii
#  prostej do celu (h, czyli odległość Manhattan 
# liczona jako suma różnic współrzędnych bez chodzenia 
# na ukos), co daje łączną prognozę długości całej
#  trasy (f = g + h) — w Twoim kodzie zrobiłeś 3 kroki
#  ($g=3$), do celu brakuje jeszcze 3 kratek ($h=3$),
#  więc łączny koszt tej ścieżki to 6, a algorytm zawsze
#  wybiera krok z najniższym wynikiem $f$, żeby nie błądzić
#  na oślep i dotrzeć do mety najkrótszą drogą.