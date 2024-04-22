
def sayHi(): #nieko nepriima, nieko negrazina
    print("hello!")
    print("ką jūs?")


sayHi()
sayHi()
sayHi()

def sayHiTo(name):# priima, nieko negrazina
    print("hello " + name)

sayHiTo("Jonas")
sayHiTo("Petras")

vardas = "Naglis"
sayHiTo(vardas)

def sayHiToWhen(name = "incognito", when = ""):
    print(f"labas {when} {name}")

sayHiToWhen("Naglis","")
sayHiToWhen("Naglis","rytas")
sayHiToWhen("Naglis")
sayHiToWhen()

def simPI():#nieko nepriima, grazina reiksme
    return 3.1415

simplifiedPIValue = simPI()
print(simplifiedPIValue)
roundedNumber = round(14.4)

def countLetters(text):#kazka priima, grazina reiksme
    count = 0
    for letter in text:
        if letter.isalpha():
            count += 1
    return count

print( countLetters("123") )
print( countLetters("abc") )


def countDigits(text):#kazka priima, grazina reiksme
    count = 0
    for letter in text:
        if letter.isdigit():
            count += 1
    return count

print( countDigits("123") )
print( countDigits("abc") )



range(10)
round(14.4)
print("labas")
import random
random.random()
roundedNumber = round(14.4)
roundedNumber**2


