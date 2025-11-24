n = float(input("Sisesta arv: "))

if n % 400 == 0: print("liigaasta")
else:
    if n % 4 == 0 and n % 100 != 0: print("liigaasta")
    else: print("lihtaasta")