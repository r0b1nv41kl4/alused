sentence = 'Leia muutuja abil etteantud tekstis olevate täishäälikute arv.' 
characters = 'aeiouõäöü'

counter = 0

for letter in sentence:
    if letter in characters:
        counter += 1

print(counter)