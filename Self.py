from xmlrpc.client import boolean

from pyarrow import dictionary

print("hello world")
print("Hello AI Era")
# sanal ortamlarin listelenmesi
# conda env list

## integer
x = 46
type(x)


## float
x =10.3
type(x)

## complex
x = 2j + 1
type(x)

## string
x= "Hello AI era"
type(x)


## Boolean
True
False
type(True)

5 == 4
3 == 2
1 == 1
type(3 == 2)


## Liste
x = ["btc", "eth", "xrp"]
type(x)

## Dict
x = {"name": "Peter", "Age": 36}
type(x)

## Tuple
x = ("phyton", "ml", "ds")
type(x)


## Set
x = {"python", "ml", "ds"}
type(x)


## Not: Liste, tuple, set ve dictionary veri yapilari Python Collections (Arrays) olarak da gecer.


## Sayilar (Numbers): int, float, complex

a = 5
b = 10.5
a * 3
a / 7
a * b / 10
a ** 2
a


## tipleri degistirmek
int(b)
float(a)
int(a * b / 10)

c = a * b / 10

int(c)


## Karakter Dizileri (Strings)

print("John")
"John"

name = "John"
name = 'John'


## Cok satirli karakter dizileri
"""Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""


## Karakter dizilerinin elemanlarina erismek
name
name[0]
name[1]


## Karakter dizilerinde slice islemi

name[0:2]
long_str = "Veri Yapilari"
long_str[0:10]


## String icinde karakter sorgulamak

long_str
"Ver" in long_str


## String metodlari

dir(str)

## Len

name = "john"
type(name)
type(len)

len(name)
len("faruktekbas")
len("miuul")


##  upper() & lower(): kucuk-buyuk donusumleri

"miuul".upper()
"MIUUL".lower()


## replace: karakter degistirir

hi = "Hello AI Era"
hi.replace("l", "p")


## split: boler

"Hello AI Era".split()


## strip: kirpar

" ofofo ".strip()
"ofofo".strip("o")


## capitalize: ilk harfi buyutur
"foo".capitalize()



## liste (list)
# - Degistirilebilir.
# - Siralidir. Index islemleri yapilabilir.
# - Kapsayicidir.

notes = [1, 2, 3, 4]
type(notes)

names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]

not_nam[6][1]
type(not_nam[6])
type(not_nam[6][1])

notes[0] = 99
print(notes)
notes[0] = 99

not_nam[0:4]

## Liste metodlari (List Methods)

dir(notes)

len(notes)
len(not_nam)


## append: eleman ekler

notes.append(100)
print(notes)


## pop: indexe gore siler

notes.pop(0


## insert: indexe ekler

notes.insert(2, 99)


## Sozluk (Dictionary)
# Degistirilebilir
# Sirasiz. (3.7 surumunden sonra sirali.)
# Kapsayici.

# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]


dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["REG"]


## Key sorgulama

"REG" in dictionary


## Demet (Tuple)

# Degistirilemez
# Siralidir.
# Kapsayicidir.

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

t[0] = 99

t = list(t)
t[0] = 99
t = tuple(t)
t


## Set

# Degistirilebilir
# Sirasiz + Essizdir
# Kapsayicidir.


## difference(): Iki kumenin farki

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.difference(set2)
set2.difference(set1)


## symmetric_difference(): Iki kumede de birbirlerine gore olmayanlar

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)


## intersection(): Iki kumenin kesisimi


set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)


## union(): Iki kumenin birlesimi

set1.union(set2)
set2.union(set1)

## isdisjoint(): Iki kumenin kesisimi bos mu?

set1.isdisjoint(set2)
set2.isdisjoint(set1)

## issubset(): Bir kume diger kumenin alt kumesi mi?

set1.issubset(set2)
set2.issubset(set1)

## issuperset(): Bir kume diger kumeyi kapsiyor mu?

set1.issuperset(set2)
set2.issuperset(set1)


##################################################
# FONKSIYONLAR, KOSULLAR, DONGULER, COMPREHENSIONS
##################################################

# - Fonksiyonlar (Functions)
# - Kosullar (Conditions)
# - Donguler (Loops)
# - Comprehensions

###  FONKSIYONLAR (FUNCTIONS)

## Fonksiyon okuryazarligi

print("a")
print("a", "b")
print("a", "b", sep="__")


## Fonksiyon Tanimlama


def calculate(x):
    print(x*2)


calculate(5)


## Iki arguman/parametreli bir fonksiyon tanimlayalim.

def summer(arg1, arg2):
    print(arg1 + arg2)

summer(7, 8)

summer(8, 7)

summer(arg2=8, arg1=7)


## Docstring


def summer(arg1, arg2):
    print(arg1 + arg2)


def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float

    """

    print(arg1 + arg2)

summer(1, 3)


## Fonksiyonlarin Statement/Body Bolumu

## def function_name(parameters/arguments):
#      statements (function body)

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")

say_hi("miuul")


def multiplication(a, b):
    c = a * b
    print(c)

multiplication(10, 9)

## girilen degerleri bir liste icinde saklayacak fonksiyon

list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 8)
add_element(18, 8)
add_element(180, 10)



## On tanimli Argumanlar/parametreler (Default Parameters/Arguments)

def divide(a, b):
    print(a / b)

divide(1, 2)

def divide(a, b=1):
    print(a / b)

divide(1)


def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")

say_hi("mrb")



## Ne zaman fonksiyon yazma ihtiyacimiz olur?

## varm, moisture, charge

(56 + 15) / 80
(17 + 45) / 70
(52 + 45) / 80

# Dry

def calculate(varm, moisture, charge):
    print((varm + moisture)/charge)

calculate(98, 12, 78)


## Return: Fonksiyon ciktilrini Girdi olarak kullanmak

def calculate(varm, moisture, charge):
    print((varm + moisture)/charge)

# calculate(98, 12, 78) * 10


# def calculate(varm, moisture, charge):
      return (varm + moisture) / charge


# calculate(98, 12, 78) * 10

# a = calculate(98, 12, 78)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

calculate(98, 12, 78)
type(calculate(98, 12, 78))


## Fonksiyon icerisinden fonksiyon cagirmak

