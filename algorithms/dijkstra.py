def dijkstra(graf, start, koniec):
    odleglosci = {wezel: float('inf') for wezel in graf}
    odleglosci[start] = 0
    kolejka = [(0, start)]
    
    while kolejka:
        # Znajdujemy i usuwamy element o najmniejszym koszcie
        kolejka.sort(key=lambda x: x[0])
        aktualny_koszt, aktualny = kolejka.pop(0)
        
        if aktualny == koniec:
            return aktualny_koszt
            
        if aktualny_koszt > odleglosci[aktualny]:
            continue
            
        for sasiad, waga in graf[aktualny].items():
            koszt = aktualny_koszt + waga
            if koszt < odleglosci[sasiad]:
                odleglosci[sasiad] = koszt
                kolejka.append((koszt, sasiad))
                
    return odleglosci[koniec]

# Przykład użycia:
graf = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

print("Najkrótszy koszt:", dijkstra(graf, 'A', 'E'))

#Ten program szuka najtańszej trasy z miasta A do E:
#  zaczyna z zerowym kosztem w A, a dla reszty miast
#  zakłada na start koszt nieskończony, 
# po czym w każdym kroku wybiera to miejsce, 
# do którego potrafi dotrzeć najtaniej, 
# sprawdza drogi do jego bezpośrednich sąsiadów 
# i jeśli odkryje tańszy dojazd niż dotychczas zapisany,
#  aktualizuje wynik i wrzuca sąsiada na listę
#  do odwiedzenia — dzięki temu bada trasy w kolejności 
# od najkrótszych i w momencie, gdy z listy zdejmie cel E,
#  ma stuprocentową pewność, że znalazł optymalną ścieżkę
#  (zwracając ostatecznie najniższy możliwy koszt równy 10).