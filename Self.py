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


def calculate(varm, moisture, charge):
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


def calculate(varm, moisure, charge):
    return int(varm + moisure) / charge

calculate(90, 12, 12) * 10



## Kosullar (Conditions)

# True- False hatirlayalim

1 == 1
1 == 2

if 1 == 1:
    print("something")


number = 11
if number == 10:
    print("number is 10")


def number_check(number):
    if number == 10:
        print("number is 10")

number_check(12)


def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(12)


## DONGULER

## for loop

students = ["John", "Mark", "Venessa", "Mariam"]

students[0]
students[1]
students[2]


for student in students:
    print(student)


for student in students:
    print(student.upper())


salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)


for salary in salaries:
    #print(salary*20/100 + salary)
    print(int(salary * 50 / 100 + salary))


def new_salary(salary, rate):
    return int(salary*rate/100 + salary)

new_salary(1500, 10)
new_salary(2000, 20)


salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 15))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))
print(salaries)


#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

range(len("miuul"))
range(0, 5)

# 4 % 2 == 0

# for i in range(0, 5):
    print(i)

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)

        print (string_index)
alternating("miuul")


#######################
# break & continue & while
#######################

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)


for salary in salaries:
    if salary == 3000:
        continue
    print(salary)


# while

number = 1
while number < 5:
    print(number)
    number += 1

#######################
# Enumerate: Otomatik Counter/Indexer ile for loop
#######################

# students = ["John", "Mark", "Venessa", "Mariam"]

# for student in students:
    print(student)

# for index, student in enumerate(students):
    print(index, student)


students = ["John", "Mark", "Venessa", "Mariam"]

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)


#######################
# Uygulama - Mülakat Sorusu
#######################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups
divide_students(students)

st = divide_students(students)
st[0]
st[1]


#######################
# alternating fonksiyonunun enumerate ile yazılması
#######################

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")

#######################
# Zip
#######################

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages))

###############################################
# lambda, map, filter, reduce
###############################################

def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b

new_sum(4, 5)

# map
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x


new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))


# del new_sum
list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2 , salaries))

# FILTER
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# REDUCE
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)

###############################################
# COMPREHENSIONS
###############################################

#######################
# List Comprehension
#######################

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))


null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]
[salary * 2 for salary in salaries]
[salary * 2 for salary in salaries if salary < 3000]
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]
[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

####
students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]


[student.lower() if student in students_no else student.upper() for student in students]
[student.upper() if student not in students_no else student.lower() for student in students]


#######################
# Dict Comprehension
#######################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}
{k.upper(): v for (k, v) in dictionary.items()}
{k.upper(): v * 2 for (k, v) in dictionary.items()}


#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir
# Key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacak.


numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for in numbers if n % 2 == 0}



#######################
# List & Dict Comprehension Uygulamalar
#######################

#######################
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek
#######################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.lower())


A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]


#######################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
#######################

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]



#######################
# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.
#######################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

## kisa yol

{col: agg_list for col in num_cols}

new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()
df[num_cols].agg(new_dict)



###############################################
# PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WITH PYTHON)
###############################################
# - NumPy
# - Pandas
# - Veri Görselleştirme: Matplotlib & Seaborn
# - Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis)

#############################################
# NUMPY
#############################################

# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

#############################################
# Neden NumPy?
#############################################

import numpy as np
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])


a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

