print ("niniejszy program ustali czy podana przez Ciebie liczba jest parzysta lub nieparzysta. Proszę podać liczbę całkowitą")
x = input()
x = int(x)
print(type(x))

if x % 2 == 0 and x != 0:
    print ("liczba jest parzysta")

else:
    print ("liczba jest nieparzysta")