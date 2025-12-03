name = input("Sisesta oma nimi: ")

location = input("Tere, " + name + ", sisestage oma elukoht: ")

if location == "Saaremaa": age = float(input("See on väga lahe koht! Kui vana te olete?: "))
else: age = float(input("Palun sisestage vanus: "))

if age < 18: print("Olete liiga noor, et autot juhtida.")
else:
    if age == 18: print("Palju õnne täiskasvanuks saamise puhul!")
    else: 
        if age > 18: print("Teie võite autot juhtida.")
        else: print("oppaidi mdea see ple number")