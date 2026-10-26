def pagerank(graf_linkow, d=0.85, iteracje=3):
    N = len(graf_linkow)
    pr = [1.0 / N] * N
    
    # Obliczamy ile linków wychodzi z każdej strony
    wychodzace = [sum(row) for row in graf_linkow]

    for krok in range(1, iteracje + 1):
        pr_nowy = [0.0] * N
        for i in range(N):
            suma_wplywow = 0.0
            for j in range(N):
                # Jeśli strona j linkuje do strony i
                if graf_linkow[j][i] == 1:
                    suma_wplywow += pr[j] / wychodzace[j]
            
            pr_nowy[i] = (1 - d) / N + d * suma_wplywow
            
        pr = [round(x, 4) for x in pr_nowy]
        print(f"Iteracja {krok} - PageRank [A, B, C]: {pr}")

# Graf: row = z kogo wychodzi, col = do kogo idzie
# A -> B, C | B -> C | C -> A, B
graf = [
    [0, 1, 1], # Strona A
    [0, 0, 1], # Strona B
    [1, 1, 0]  # Strona C
]

pagerank(graf)

#Algorytm PageRank (słynny fundament wyszukiwarki Google)
#  działa jak konkurs popularności w internecie:
#  każda strona zaczyna z równą porcją „prestiżu” ($1/N$),
#  a w każdej rundzie oddaje cały swój prestiż stronom,
#  do których linkuje — dzieląc go po równo między wszystkie
#  swoje linki wychodzące (pr[j] / wychodzace[j]),
#  więc link od potężnej strony waży o wiele więcej 
# niż od mało znaczącej, a współczynnik tłumienia $d = 0.85$
#  uwzględnia to, że internauta w 85% przypadków klika linki,
#  a w 15% losowo wpisuje zupełnie nowy adres ((1 - d) / N);
#  w ten sposób po kilku iteracjach prestiż krążący w sieci
#  stabilizuje się i wskazuje najważniejszą stronę
#  (tutaj C, bo zbiera najwięcej mocnych odnośników).
