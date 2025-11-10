import math

# print(math.pi)

raadius = float(input("Sisesta raadius: "))
raadiusruudus = raadius * raadius

pindala = math.pi * raadiusruudus
ümbermõõt = 2 * math.pi * raadius

print("Pindala on", pindala, "ja ümbermõõt on", ümbermõõt)