import random

j = 0
rand = [0, 0, 0]
rand[0] = random.randint(0, 9)
rand[1] = random.randint(0, 9)
rand[2] = random.randint(0, 9)

print("Bagels, a deductive logic game.\nBy Al Sweigart al@inventwithpython.com\n\nI am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:\nWhen I say: That means:\n Pico One digit is correct but in the wrong position.\n Fermi One digit is correct and in the right position.\nBagels No digit is correct.\nI have thought up a number.\n You have 10 guesses to get it.\n")

i = 0
while i < 10:
    rslt = {'pico': 0, 'fermi': 0}
    x = input(f"Guess #{i+1}: ")
    
    if len(x) != 3:
        print("The number must be 3 digits.")
        continue
    
    if x.isalpha():
        print("The number must be digits only.")
        continue
    
    i += 1
    rslt['pico'] = 0
    rslt['fermi'] = 0
    
    for j in range(3):
        if rand[j] == int(x[j]):
            print("Fermi", end=" ")
            rslt['fermi'] += 1

    for j in range(3):
        if rand[j] != int(x[j]) and int(x[j]) in rand:
            print("Pico", end=" ")
            rslt['pico'] += 1

    if rslt['fermi'] + rslt['pico'] == 0 :
        print("bagels")
    
    if rslt['fermi'] == 3:
        print()
        print("You got it!")
        exit()


    if i == 10:
        print("Sorry, you've used all your guesses. The number was: {}{}{}".format(rand[0], rand[1], rand[2]))
