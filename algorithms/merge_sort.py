#Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

dane = [38, 27, 43, 3, 9, 82, 10]
print(f"Przed sortowaniem: {dane}")
posortowane = merge_sort(dane)
print(f"Po sortowaniu: {posortowane}")

#Kodowanie Huffmana działa jak sprytne pakowanie walizki:
#  najpierw zlicza, jak często każda litera pojawia się
#  w tekście, a następnie w pętli łączy ze sobą dwie
#  najrzadziej występujące litery w pary, przypisując
#  jednej z nich bit 0, a drugiej 1 i sumując ich wagi
#  w nowy wspólny węzeł, powtarzając to łączenie od dołu
#  do samej góry, aż powstanie jedno wielkie drzewo
#  — dzięki temu litery powtarzające się najczęściej dostają
#  najkrótsze możliwe kody zero-jedynkowe (np. 1–2 bity),
#  a litery rzadkie kody dłuższe, co pozwala bezstratnie
#  skompresować cały tekst tak, by zajmował jak najmniej 
# miejsca w pamięci.