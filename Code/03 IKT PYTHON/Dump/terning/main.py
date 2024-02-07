import random

terninger = int(input("Hvor manger terninger vil du trille?\n"))

resultater = []
for i in range(terninger):
    resultater.append(random.randint(1,6))

print(f"En: {resultater.count(1)}")
print(f"To: {resultater.count(2)}")
print(f"Tre: {resultater.count(3)}")
print(f"Fire: {resultater.count(4)}")
print(f"Fem: {resultater.count(5)}")
print(f"Seks: {resultater.count(6)}")