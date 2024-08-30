from xmlrpc.client import boolean

print("hello world")
print("Hello AI Era")
# sanal ortamlarin listelenmesi
# conda env list
x=46
type(x)
x=10.3
type(x)
x=2j + 1
type(x)

x= "Hello AI era"
type(x)

True
False
type(True)

5 == 4
3==2
1==1
type(3==2)

x=["btc", "eth", "xrp"]
type(x)

x={"name": "Peter", "Age": 36}
type(x)

x= ("phyton", "ml", "ds")
type(x)
a=5
b= 10.5
a * 3
a / 7
a * b / 10
a ** 2


int(b)
float(a)
int(a * b / 10)

c = a * b / 10

int(c)


print("John")
"John"

name = "John"
name = 'John'

""" """
name
name[0]
name[1]

name[0:2]

long_str = Veri Yapilari

long_str[0:10]

"John"
name = "John"


name[0]
name[3]

name = "John"
type(name)
type(len)

len("faruktekbas")
"miuul".upper()
"MIUUL".lower()

hi = "Hello AI Era"
hi.replace("l", "p")


notes = [1, 2, 3, 4]

not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
notes[1] = 99
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
not_nam[0:4]

dir(notes)

len(notes)

notes.append(100)

notes.insert(2,99)



# key- value
dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}
dictionary["REG"]

dictionary.keys()
dictionary.items().update({"RF": 10})


t = ("john", "mark", 1, 2)
type(t)


t[0]
t[0:3]
t[0] = 99

t = list(t)
t[0] = 99
t = tuple(t)

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
set1.difference(set2)

set2.difference(set1)

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

set1.intersection(set2)
set2.intersection(set1)

set1 - set2

set1.union(set2)
set2.union(set1)

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)


set1.issubset(set2)
set2.issubset(set1)

set2.issuperset(set1)
set1.issuperset(set2)