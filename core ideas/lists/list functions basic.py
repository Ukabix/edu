
produkty = ["mleko","ser","parówki"]
print(produkty)
print(type(produkty))
print(produkty[0:3])

produkty.append("szyneczka")
print(produkty)

x = produkty.count("mleko")
print(x)
print(produkty)

print(produkty.count("mleko"))

inne_produkty = ["karabiny, granaty"]
produkty.extend(inne_produkty)
print(produkty)

produkty.insert(1, "majonez")
print(produkty)

produkty.pop(1)
print(produkty)

produkty.remove("mleko")
print(produkty)

produkty.clear()
print(produkty)
