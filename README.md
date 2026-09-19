#  Historia Algorytmów

Interaktywna oś czasu prezentująca przełomowe algorytmy w historii informatyki i matematyki — od metody Newtona-Raphsona aż po PageRank. Projekt umożliwia nie tylko poznanie kontekstu historycznego i zastosowań poszczególnych algorytmów, ale także bezpośrednie **testowanie i modyfikowanie ich kodu w języku Python w przeglądarce**.

**Autor:** Polina Bohomol (ZSK, klasa 3b)

---

##  Główne Funkcje

* **Interaktywna Oś Czasu (Timeline):** Czytelna prezentacja historyczna kluczowych algorytmów wraz z ich ramami czasowymi oraz opisem zastosowań (od grafiki po uczenie maszynowe i kryptografię).
* **Wbudowany Środowisko Python (IDE in-browser):** Każdy algorytm posiada przycisk **„Wypróbuj”**, który otwiera edytor kodu pozwalający uruchamiać i modyfikować skrypty w Pythonie bez konieczności instalowania czegokolwiek na komputerze.
* **Ciekawostki i Geneza:** Informacje na temat pochodzenia słowa *algorytm* oraz przykłady fascynujących zdarzeń z nimi związanych (np. błąd wyceny na Amazonie).
* **Animowane Efekty Wizualne:** Tło z dynamicznym efektami cząsteczkowymi (canvas) dopracowujące estetykę aplikacji.

---

##  Użyte Technologie

* **HTML5 & CSS3:** Modern Web Design, flexbox/grid layout, customowe fonty Google Fonts (*Montserrat*).
* **JavaScript (ES6+):** Logika interaktywna, obsługa modali oraz animacji canvas (`confetti`).
* **[Skulpt](http://www.skulpt.org/):** Biblioteka JavaScript umożliwiająca wykonywanie kodu Python 3 bezpośrednio w przeglądarce klienta.

---

##  Algorytmy w Projekcie

W ramach projektu można zapoznać się oraz przetestować następujące algorytmy:

1. **1671** — Metoda Newtona-Raphsona *(numeryczne szukanie miejsc zerowych)*
2. **1942** — Szybka Transformacja Fouriera / FFT *(analiza częstotliwości sygnałów)*
3. **1945** — Sortowanie przez Scalanie / Merge Sort *(dziel i zwyciężaj, $O(n \log n)$)*
4. **1947** — Algorytm Simplex *(programowanie liniowe)*
5. **1952** — Kodowanie Huffmana *(bezstratna kompresja danych)*
6. **1959** — Algorytm Dijkstry *(najkrótsza ścieżka w grafie)*
7. **1962** — Szybkie Sortowanie / Quick Sort *(rekurencyjne sortowanie wokół pivota)*
8. **1968** — Algorytm A* *(heurystyczne wyszukiwanie ścieżek)*
9. **1972** — Drzewa B i Drzewa Czerwono-Czarne *(zbalansowane struktury danych)*
10. **1973** — Szyfrowanie RSA *(kryptografia z kluczem publicznym)*
11. **1977** — Algorytm Boyera-Moorea *(wyszukiwanie wzorca w tekście)*
12. **1983** — Algorytm CART *(drzewa decyzyjne w uczeniu maszynowym)*
13. **1998** — Algorytm PageRank *(ocena ważności stron www)*

---

##  Jak uruchomić i korzystać z projektu?

### 1. Uruchomienie lokalne

Projekt nie wymaga instalacji żadnego środowiska uruchomieniowego (np. Node.js czy Python) ani serwera – działa w pełni w przeglądarce.

1. Pobierz lub sklonuj repozytorium na swój komputer:
   ```bash
   git clone https://github.com/twoj-nick/historia-algorytmow.git
   ```
2. Otwórz plik `index.html` w dowolnej nowoczesnej przeglądarce internetowej (Chrome, Firefox, Edge, Safari).

*Uwaga: Do poprawnego ładowania biblioteki Skulpt z CDN wymagane jest aktywne połączenie z Internetem.*

---

### 2. Instrukcja obsługi

1. **Przeglądanie:** Przewijaj stronę główną, aby czytać opisy oraz poznawać historię rozwoju algorytmów.
2. **Uruchamianie kodu:** Kliknij przycisk **„Wypróbuj”** przy wybranym algorytmie.
3. **Edycja:** W otwartym oknie edytora możesz dowolnie modyfikować kod w lewym panelu.
4. **Wynik:** Kliknij przycisk **„Run ❯”**, aby zobaczyć wygenerowany wynik wykonania skryptu w prawym panelu konsoli.

---

##  Źródła i Inspiracje

Podczas prac nad projektem wykorzystano materiały z następujących źródeł:

* [GeeksforGeeks – DSA Tutorial](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
* [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)
* [Red Blob Games – A* Pathfinding](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
* [3Blue1Brown – Fourier Transforms](https://www.3blue1brown.com/?topic=fourier-transforms&lesson=eulers-formula-poem)
* [Scikit-learn Decision Trees Documentation](https://scikit-learn.org/stable/modules/tree.html)
* UI/Design inspiration: [CodyHouse](https://codyhouse.co/), [UIverse](https://uiverse.io/)c
