class Node:
    def __init__(self, cecha=None, prog=None, lewy=None, prawy=None, decyzja=None):
        self.cecha = cecha      # Nazwa cechy (np. 'wiek')
        self.prog = prog        # Wartość podziału (np. 30)
        self.lewy = lewy        # Dziecko, gdy warunek spełniony (<= prog)
        self.prawy = prawy      # Dziecko, gdy warunek niespełniony (> prog)
        self.decyzja = decyzja  # Wynik (tylko w liściach)

def przewiduj(wezel, dane):
    """Rekurencyjnie przechodzi po drzewie do momentu trafienia na decyzję."""
    if wezel.decyzja is not None:
        return wezel.decyzja

    wartosc = dane[wezel.cecha]
    if wartosc <= wezel.prog:
        return przewiduj(wezel.lewy, dane)
    else:
        return przewiduj(wezel.prawy, dane)

drzewo = Node(
    cecha="wiek", prog=30,
    lewy=Node(decyzja="Grupa A: Młody użytkownik"),
    prawy=Node(
        cecha="dochod", prog=5000,
        lewy=Node(decyzja="Grupa C: Standardowe dochody"),
        prawy=Node(decyzja="Grupa B: Wysokie dochody")
    )
)

osoba1 = {"wiek": 25, "dochod": 3000}
osoba2 = {"wiek": 42, "dochod": 7500}

print("Osoba 1:", przewiduj(drzewo, osoba1))
print("Osoba 2:", przewiduj(drzewo, osoba2))

#Ten kod to klasyczne drzewo decyzyjne, 
# które działa dokładnie jak formularz 
# z pytaniami „TAK / NIE”: zaczynając od samej góry
#  (korzenia), algorytm sprawdza konkretną cechę osoby
#  (np. czy wiek wynosi co najwyżej 30 lat)
#  i jeśli warunek jest spełniony, skręca w lewą gałąź,
#  a jeśli nie – w prawą, powtarzając ten proces
#  rekurencyjnie na kolejnych pytaniach (węzłach Node)
#  tak długo, aż dotrze do ślepego zaułka bez pytań
#  (liścia z polem decyzja), gdzie odczytuje gotowy
#  wynik — dlatego Osoba 1 (wiek 25) natychmiast 
# wpada w lewą odnogę i dostaje etykietę
#  „Grupa A: Młody użytkownik”, podczas gdy
#  Osoba 2 (wiek 42) idzie najpierw w prawo
#  (bo wiek > 30), tam trafia na drugie pytanie o dochód
#  (czy dochód $\le$ 5000) i z zarobkami 7500 ponownie 
# skręca w prawo, lądując ostatecznie w „Grupa B: Wysokie
#  dochody”.