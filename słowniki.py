
osoba = {"wiek":20, "imię":"Ania", "nazwisko":"Kowalska"}

print(type(osoba))

print(osoba["wiek"])
print(osoba["imię"])
print(osoba["nazwisko"])

print(osoba.get("wzrost", 175))

keys = osoba.keys()
print(type(keys))

values = osoba.values()
print(type(values))

items = osoba.items()
print(type(items))