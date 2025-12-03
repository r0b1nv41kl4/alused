string = input("Palun kirjuta midagi: ")

string = string.strip()

if len(string) < 7: print("Peab sisaldama vähemalt 7 sümbolit")
elif len(string) % 2 == 0: print("Peab olema paaritu")
else:
    symbols = len(string) // 2
    threeSymbols = string[symbols - 1 : symbols + 2]
    print("3 symbols in the middle are", threeSymbols)