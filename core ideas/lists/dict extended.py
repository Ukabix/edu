# różnice lista - słownik: przyporządkowanie do lokacji - przyporządkowanie do klucza (key:value)

my_dict = {'key1':'value1', 'key2':'value2'}

# wyszukiwanie po kluczu
print(my_dict['key1'])

prices_lookup = {'apple': 2.99, 'orange':1.99, 'milk': 5.80}
print(prices_lookup['apple'])

d = {'k1':123, 'k2':[0,1,2],'k3':{'insideKey':100}}

print(d['k2'])
print(d['k3'])
print(d['k3']['insideKey']) # stacking
print(d['k2'][2])

e = {'key1' : ['a', 'b', 'c']}
print(e)
mylist = e['key1']
letter = mylist[2]
print(letter.upper())
print(e) # dict niezmieniony!

f = {'key1' : ['a', 'b', 'c']}
print(f['key1'][2].upper())
print(f)

# dict rozszerzenie
g = {'k1':100, 'k2':200}
g['k3'] = 300
print(g)
g['k1'] = 'COŚ'
print(g)

# dict odczyt
h = {'k1':100, 'k2':200, 'k3':300}
print(h.keys())
print(h.values())
print(h.items())