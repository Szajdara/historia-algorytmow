import math

def dft(sygnal):
    N = len(sygnal)
    wyniki = []
    
    # k = numer częstotliwości (prążka)
    for k in range(N):
        suma_real = 0.0
        suma_imag = 0.0
        
        # n = kolejna próbka sygnału w czasie
        for n in range(N):
            kat = 2 * math.pi * k * n / N
            
            # Wzór Eulera: cosinus to część rzeczywista, sinus to urojona
            suma_real += sygnal[n] * math.cos(kat)
            suma_imag -= sygnal[n] * math.sin(kat)
            
        # Obliczamy moc/siłę danej częstotliwości (amplitudę)
        amplituda = math.sqrt(suma_real**2 + suma_imag**2)
        
        wyniki.append({
            "k": k,
            "real": round(suma_real, 2),
            "imag": round(suma_imag, 2),
            "amplituda": round(amplituda, 2)
        })
        
    return wyniki

sygnal = [1, 2, 1, -1]
widmo = dft(sygnal)

print("k | Część Re | Część Im | Sila (Amplituda) | Wykres mocy")
print("-" * 55)

for p in widmo:
    # Rysujemy prosty wykres z gwiazdek
    wykres = "*" * int(p["amplituda"] * 2)
    print(f"{p['k']} | {p['real']:8.2f} | {p['imag']:8.2f} | {p['amplituda']:16.2f} | {wykres}")

    #Ten kod to Dyskretna Transformata Fouriera (DFT),
    #  która działa jak pryzmat rozszczepiający światło
    #  na kolory tęczy: bierze surowy sygnał zmieniający
    #  się w czasie (tutaj 4 próbki: [1, 2, 1, -1]) i
    #  sprawdza po kolei dla każdej możliwej częstotliwości
    #  ($k$), jak mocno jest ona obecna w całym sygnale —
    #  robi to, mnożąc każdą próbkę przez fale testowe o 
    # różnym tempie drgań (za pomocą funkcji $\cos$ i $\sin$ 
    # ze wzoru Eulera), a następnie sumując te dopasowania 
    # w części rzeczywiste (real) i urojone (imag), z których
    #  na koniec twierdzeniem Pitagorasa wylicza amplitudę 
    # (czyli głośność/siłę danego tonu); dzięki temu z pozoru
    #  chaotycznego ciągu liczb dowiadujesz się, z jakich 
    # prostych czystych fal składa się Twój dźwięk lub wykres.