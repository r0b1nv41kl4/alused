n1 = float(input("Sisesta 1 pikkus: "))
n2 = float(input("Sisesta 2 pikkus: "))
n3 = float(input("Sisesta 3 pikkus: "))

if n1 == n2 == n3: print("võrdkülgne")
else: 
    if n1 == n2 or n2 == n3 or n1 == n3: print("võrdhaarne")
    else:
        if n1 == 0 or n2 == 0 or n3 == 0: print('pole kolmnurk')
        else: print("erikülgne")