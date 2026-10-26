# 🌐 Historia Algorytmów & Zadania z Podręcznika

Interaktywna strona edukacyjna prezentująca przełomowe algorytmy w historii informatyki i matematyki oraz **zestawienie 10 praktycznych zadań algorytmicznych** z podręcznika dla liceum i technikum *„Informatyka na czasie 2. Zakres rozszerzony”* (wyd. Nowa Era).

Projekt łączy teorię z praktyką — umożliwia nie tylko poznanie kontekstu historycznego i zasady działania algorytmów, ale także **bezpośrednie testowanie, modyfikowanie i uruchamianie ich kodu w języku Python wprost w przeglądarce**.

**Autor:** Polina Bohomol (uczeń ZSK, klasa 3b)

---

## 🚀 Główne Funkcje Projektu

### 1. Interaktywna Oś Czasu (`index.html`)
* **Chronologiczny przegląd:** Prezentacja kluczowych kamieni milowych w historii algorytmiki (od metody Newtona z 1671 r. po algorytm PageRank z 1998 r.).
* **Wizualizacja i opisy:** Zrozumiałe omówienie zastosowań algorytmów we współczesnym świecie (kompresja danych, sztuczna inteligencja, nawigacja GPS, grafika).
* **Ciekawostki:** Informacje o pochodzeniu słów *algorytm* i *algebra* oraz anegdoty (np. błąd botów cenowych na Amazonie).

### 2. Baza 10 Zadań z Podręcznika (`zadania.html`)
* **Oficjalne źródło:** Zadania zaczerpnięte z podręcznika *„Informatyka na czasie 2. Zakres rozszerzony”* (Nowa Era).
* **Kompletne dane:** Dokładna treść zadania, numer strony oraz numer ćwiczenia w podręczniku.
* **Dwujęzyczny kod źródłowy:** Każde zadanie posiada zakładki z kodem w **C++** (zgodnym z programem nauczania) oraz w **Pythonie**.
* **Tłumaczenie krok po kroku:** Proste, przystępne wyjaśnienie idei działania algorytmu bez zbędnego żargonu.
* **Złożoność obliczeniowa:** Precyzyjne określenie złożoności czasowej i pamięciowej dla każdego rozwiązania w czytelnych blokach.

### 3. Wbudowane Środowisko Python (IDE w przeglądarce)
* Każdy algorytm wyposażony jest w przycisk **„Wypróbuj w edytorze”**.
* Otwiera modalne okno z edytorem kodu oraz wbudowaną konsolą.
* Umożliwia edycję parametrów wejściowych i natychmiastowe uruchomienie skryptu przyciskiem **`Run ❯`** dzięki silnikowi **Skulpt**.

---

## 📚 10 Zadań z Podręcznika (*Informatyka na czasie 2*)

| Lp. | Algorytm / Problem | Położenie w podręczniku | Języki | Złożoność czasowa | Złożoność pamięciowa |
|:---:|:---|:---|:---:|:---:|:---:|
| **1** | **Zamiana liczby dziesiętnej na dwójkową** | Strona 50, Ćwiczenie 1 | C++ / Python | $O(\log_2 n)$ | $O(\log_2 n)$ |
| **2** | **Szybkie podnoszenie do potęgi** | Strona 58, Ćwiczenie 7 | C++ / Python | $O(\log_2 n)$ | $O(1)$ |
| **3** | **Sprawdzanie, czy wyraz jest palindromem** | Strona 63, Ćwiczenie 1 | C++ / Python | $O(n)$ | $O(1)$ |
| **4** | **Test pierwszości liczby (metoda $6i \pm 1$)** | Strona 78, Ćwiczenie 2 | C++ / Python | $O(\sqrt{n})$ | $O(1)$ |
| **5** | **Rozkład liczby na czynniki pierwsze** | Strona 81, Ćwiczenie 4 | C++ / Python | $O(\sqrt{n})$ | $O(1)$ |
| **6** | **Algorytm Euklidesa (NWD z resztą modulo)** | Strona 108, Ćwiczenie 1 | C++ / Python | $O(\log(\min(a, b)))$ | $O(1)$ |
| **7** | **Szyfrowanie szyfrem Cezara** | Strona 120, Ćwiczenie 2 | C++ / Python | $O(n)$ | $O(n)$ |
| **8** | **Wyszukiwanie binarne w tablicy** | Strona 157, Ćwiczenie 3 | C++ / Python | $O(\log_2 n)$ | $O(1)$ |
| **9** | **Jednoczesne szukanie min i max (MiniMaks)** | Strona 161, Ćwiczenie 4 | C++ / Python | $\approx \frac{3n}{2}$ porównań | $O(1)$ |
| **10** | **Sortowanie bąbelkowe (Bubble Sort)** | Strona 173, Ćwiczenie 1 | C++ / Python | $O(n^2)$ | $O(1)$ |

---

## ⏳ Algorytmy na Osi Czasu

1. **1671** — Metoda Newtona-Raphsona *(szukanie miejsc zerowych funkcji)*
2. **1942** — Szybka Transformacja Fouriera / FFT *(analiza sygnałów i częstotliwości)*
3. **1945** — Sortowanie przez Scalanie / Merge Sort *(wzorzec dziel i zwyciężaj)*
4. **1947** — Algorytm Simplex *(optymalizacja i programowanie liniowe)*
5. **1952** — Kodowanie Huffmana *(bezstratna kompresja danych)*
6. **1959** — Algorytm Dijkstry *(najkrótsza ścieżka w grafie)*
7. **1962** — Szybkie Sortowanie / Quick Sort *(sortowanie wokół elementu osiowego - pivota)*
8. **1968** — Algorytm A* *(heurystyczne przeszukiwanie grafów, pathfinding w grach)*
9. **1972** — Drzewa B i Czerwono-Czarne *(zbalansowane drzewiaste struktury danych)*
10. **1973** — Szyfrowanie asymetryczne RSA *(kryptografia z kluczem publicznym)*
11. **1977** — Algorytm Boyera-Moorea *(efektywne wyszukiwanie wzorca w tekście)*
12. **1983** — Algorytm CART *(drzewa klasyfikacyjne i regresyjne w uczeniu maszynowym)*
13. **1998** — Algorytm PageRank *(ranking stron WWW stanowiący fundament Google)*

---

## 🛠️ Użyte Technologie

* **HTML5 & CSS3:** Semantyczny kod, responsywny layout (Flexbox/Grid), szklany motyw (Glassmorphism), animacje w CSS.
* **JavaScript (ES6+):** Dynamiczne ładowanie plików kodu (`fetch`), przełączanie zakładek językowych, obsługa okien modalnych.
* **[Skulpt](https://skulpt.org/):** Silnik interpretujący język Python bezpośrednio w JavaScript po stronie przeglądarki.
* **HTML5 Canvas:** Tło z animacją spadających cyfr (`#confetti`).
* **Google Fonts:** Krój pisma *Montserrat*.

---

## 📂 Struktura Projektu

```text
historia-algorytmow/
├── index.html                    # Strona główna z osią czasu historii algorytmów
├── zadania.html                  # Podstrona z 10 zadaniami z podręcznika
├── style.css                     # Wspólne style CSS dla obu podstron
├── script.js                     # Logika przełączania zakładek, animacji i edytora Skulpt
├── README.md                     # Dokumentacja projektu
└── algorithms/                   # Skrypty Python ładowane do edytora na żywo
    ├── newton.py
    ├── fft.py
    ├── merge_sort.py
    ├── simplex.py
    ├── huffman.py
    ├── dijkstra.py
    ├── quick_sort.py
    ├── a_star.py
    ├── trees.py
    ├── rsa.py
    ├── boyer_moore.py
    ├── cart.py
    ├── pagerank.py
    ├── zadanie1_dec_to_bin.py
    ├── zadanie2_szybkie_potegowanie.py
    ├── zadanie3_palindrom.py
    ├── zadanie4_liczba_pierwsza.py
    ├── zadanie5_czynniki_pierwsze.py
    ├── zadanie6_euklides_nwd.py
    ├── zadanie7_szyfr_cezara.py
    ├── zadanie8_wyszukiwanie_binarne.py
    ├── zadanie9_min_maks.py
    └── zadanie10_sortowanie_babelkowe.py
```

---

## 💻 Jak uruchomić projekt lokalnie?

Ze względu na to, że wbudowany edytor wczytuje pliki z katalogu `algorithms/` za pomocą funkcji `fetch()`, przeglądarka wymaga uruchomienia strony przez lokalny serwer HTTP (aby uniknąć blokady polityki CORS dla protokołu `file:///`):

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoj-login/historia-algorytmow.git
   cd historia-algorytmow
   ```
2. Uruchom prosty serwer lokalny:
   * **W Visual Studio Code:** Zainstaluj rozszerzenie *Live Server*, kliknij prawym przyciskiem myszy na `index.html` i wybierz **„Open with Live Server”**.
   * **LUB za pomocą Pythona:**
     ```bash
     python -m http.server 8000
     ```
     a następnie otwórz w przeglądarce adres: `http://localhost:8000`.

---

## 📖 Źródła

* Podręcznik: *„Informatyka na czasie 2. Zakres rozszerzony”* — Janusz Mazur, Paweł Perekietka, Zbigniew Talaga, Janusz S. Wierzbicki (Wydawnictwo Nowa Era).
* [GeeksforGeeks – DSA Tutorial](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
* [Runestone Academy – PythonDS](https://runestone.academy/ns/books/published/pythonds/index.html)
* [Red Blob Games – A* Pathfinding](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
* [3Blue1Brown – Fourier Transforms](https://www.3blue1brown.com/)
