import random

terning1 = random.randint(1, 6)
terning2 = random.randint(1, 6)

print(f"Du trillet {terning1} og {terning2}")

if terning1 == terning2:
    print(f"Begge terningene ble {terning1}")
else:
    print("Prøv igjen!")
