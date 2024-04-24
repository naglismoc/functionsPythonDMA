import math
import time
from datetime import datetime


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

def countDigits(text:str = "") -> int:  #kazka priima, grazina reiksme
    count = 0
    for letter in text:
        if letter.isdigit():
            count += 1
    return count

print( countDigits("123") )
print( countDigits("abc") )
# import random as rnd
#
# rnd.random(5,10)


range(10)
round(14.4)
print("labas")
import random
random.random()
roundedNumber = round(14.4)
roundedNumber**2



# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
# Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.
# Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų. Funkcija priima tris int tipo kintamuosius, min, max ir length reikšmėms nustatyti.
# Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
# Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).

def printArr(arr = []):
    line = ""
    for i in arr:
        line += str(i) + ", "
    print(line[:-2] + ";")

printArr(["labas",'rytas','Jonas','vedarai'])
printArr([3,5,10,12,18,7])
'3, 5, 10, 12, 18, 7;' #?


def ArrSqrt(arr = []):
    for i in range(len(arr)):
        arr[i] = arr[i]**2
    return arr
printArr(ArrSqrt([3,5,10,12,18,7]))

def rndInt(min, max):
            #5 +        0.00         *  15-5= 10 = 0; = 5
            #5 +        0.99         *  15-5= 10 = 9.9 = 10 = 15
    return min + round(random.random() * (max - min))

print(rndInt(5,15))

def rndIntArr(min, max, length):
    arr = []
    for i in range(length):
        arr.append(rndInt(min,max))
    return arr

rndArr = rndIntArr(5,15,3)
printArr(rndArr)

def sumArr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print(sumArr(rndArr))

def avgArr(arr):
    return sumArr(arr) / len(arr)

print(avgArr(rndArr))


#Sugeneruokite masyvą iš 10 elementų,
# --kurie yra masyvai iš 10 elementų,+
# --kurie yra atsitiktiniai skaičiai nuo 1 iki 100.+
# Jeigu tokio didelio masyvo (ne atskirai mažesnių) pirminių skaičių vidurkis mažesnis už 70,
# --suraskite masyve mažiausią skaičių (nebūtinai pirminį)
# --ir prie jo pridėkite 3.
# Vėl paskaičiuokite masyvo pirminių skaičių vidurkį
# --ir jeigu mažesnis nei 70 viską kartokite.

def isPrimary(num):
    count = 0
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            count += 1
    return count == 0

print(isPrimary(4))
print(isPrimary(9))
print(isPrimary(11))

# start = time.perf_counter_ns()
# for i in range(1000):
#     isPrimary(10000)
# # do some work
# duration = time.perf_counter_ns() - start
# print(f"Your duration was {round(duration / 1000000000,3)}s.")


def doSomeWeirdStuff():
    arr = []
    for i in range(4):
        tempArr = []
        arr.append(rndIntArr(1,100,10))

    while True:
        sum = 0
        count = 0
        minVal = 100
        posI = 0
        posA = 0
        print(arr)
        for i in range(len(arr)):
            innerArr = arr[i]
            for a in range(len(innerArr)):
                element = innerArr[a]
                if element < minVal:
                    minVal = element
                    posI = i
                    posA = a
                if isPrimary(element):
                    sum += element
                    count += 1
        print(sum / count)
        if(sum / count >=70):
            return
        # print(f'posI = {posI} posA = {posA} minVal = {minVal}  arr[posI][posA] ={ arr[posI][posA]}')
        arr[posI][posA] += 3

doSomeWeirdStuff()


