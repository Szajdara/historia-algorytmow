def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partycjonowanie (Lomuto)
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        # Umieszczenie pivota na właściwym miejscu
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1

        # Rekurencja musi być WEWNĄTRZ bloku 'if low < high'
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

    return arr

dane = [29, 10, 14, 37, 13, 9, 21]
print("Przed:", dane)
quick_sort_inplace(dane)
print("Po:", dane)

#QuickSort w tej wersji (schemat Lomuto) działa jak 
# ustawianie ludzi w kolejce według wzrostu względem
#  wybranej osoby odniesienia: bierze ostatnią liczbę 
# z listy jako punkt odniesienia (pivot, w Twoim przypadku 21),
#  po czym przegląda całą resztę od lewej do prawej i za
#  każdym razem, gdy trafi na liczbę mniejszą lub równą
#  pivotowi, zamienia ją miejscami tak, by upchnąć ją
#  na lewą stronę, a na koniec wstawia samego pivota
#  idealnie pomiędzy te mniejsze a większe elementy
#  (pi = i + 1); w tym momencie liczba 21 stoi już
#  na swoim ostatecznym, perfekcyjnym miejscu w
#  posortowanym szyku, a cała funkcja powtarza dokładnie
#  ten sam manewr rekurencyjnie dla powstałej lewej
#  (mniejsze liczby) i prawej (większe liczby) części
#  listy bez tworzenia nowych tablic w pamięci (in-place),
#  aż cała lista będzie uporządkowana rosnąco.