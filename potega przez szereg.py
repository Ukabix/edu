def podnies_do_potegi(podst, wykl):
    wynik = 1
    for liczba in range(wykl):
        wynik = wynik * podst
    return wynik


print(podnies_do_potegi(float(input("Podaj podstawę potęgi")), int(input("Podaj wykładnik potęgi"))))
## dla zmiennej wykl -> int a nie float, bo jest to argument funkcji for - chyba ?
