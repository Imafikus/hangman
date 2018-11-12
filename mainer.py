
from random import randint
print("Welcome to hangman game, please tell me you name")
pn = input()
print("Hello " + pn + " I hope that you'll have fun!")
ls = 5
won = False
f = open("words.txt", "r")
w = f.readlines()
w = w[randint(0, len(w)-1)].rstrip()
w = w.lower()
a1 = []
for _ in w:
    a1.append("_")
while True:
    print("Lives left: ", ls)
    a2 = ""
    for c in a1:
        a2 += c + " "
    print(a2)
    l = None
    while True:
        print("Please enter a letter")
        l = input()
        if l.isalpha() and len(l) == 1:
            break
        else:
            l = None
    if l in w:
        for i, c in enumerate(w):
            if c == l:
                a1[i] = l
    else:
        ls -= 1
        if ls == 0:
            print("You lost, better luck next time")
            print("Word was " + w)
            break
    if "_" not in a1:
        print("Congratulations, you won!")
        print("Word was " + w)
        break