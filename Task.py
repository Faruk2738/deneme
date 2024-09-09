

##### Odev 1 #####

##### Virtual Environment Oluşturma #####

## Görev 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.

## Cevap: conda create –n farukenv python=3
#         conda install python 3
##        conda env list (tüm env görebilirsiniz)


## Görev 2: Oluşturduğunuz environment'ı aktife diniz.
## Cevap:   conda activate farukenv


## Görev 3: Yüklü paketleri listeleyiniz.
## Cevap:   conda list


## Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
## Cevap:   conda install Numpy Pandas=1.2.1


## Görev 5: İndirilen Numpy'ın versiyonu nedir?
## Cevap:   conda list  (versiyon 1.21.5)


## Görev 6: Pandas'ı upgrade ediniz. Yeni versiyonu nedir?
## Cevap:   conda upgrade Pandas


## Görev 7: Numpy'ı environment'tan siliniz.
## Cevap:   conda remove Numpy


## Görev 8: Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.
## Cevap:   conda install Seaborn matplotlib


## Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz
# ve yaml dosyasını inceleyiniz.
## Cevap: conda env export > environment.yaml


## Görev 10: Oluşturduğunuz environment'i siliniz. Önce environment'i deactivate ediniz.
## Cevap:    conda deactivate
             conda env remove -n faruk


Derya hocanin cevaplari
###############################################
# Virtual Environment Oluşturma
###############################################



# Görev 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında
python 3 kurulumu yapınız.
###############################################
# conda create -n deryaenv python=3
# conda env list (tüm env görebilirsiniz)
###############################################

# Görev 2: Oluşturduğunuz environment'ı aktif ediniz.
###############################################
#conda activate deryaenv
###############################################

# Görev 3: Yüklü paketleri listeleyiniz.
###############################################
# conda list
###############################################

# Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1
versiyonunu aynı anda indiriniz.
###############################################
# conda install numpy pandas=1.2.1
###############################################

# Görev 5: İndirilen Numpy'ın versiyonu nedir?
###############################################
# conda list
###############################################

# Görev 6: Pandas'ı upgrade ediniz. Yeni versiyon nedir?
###############################################
# conda upgrade pandas
# conda list
###############################################

# Görev 7: Numpy'ı environment'tan siliniz.
###############################################
# conda remove numpy
###############################################

# Görev 8: Seaborn kütüphanesini ve matplotlib kütüphanesini aynı anda güncel
versiyonları ile indiriniz.
###############################################
# conda install seaborn matplotlib
###############################################

# Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber
export ediniz ve yaml dosyasını inceleyiniz.
###############################################
# conda env export > enviroment.yaml
###############################################

# Görev 10: Oluşturduğunuz environment'i siliniz.
###############################################
# İpucu: Önce environment'i deactivate ediniz.
# conda deactivate
# conda env remove -n deryaenv



###### ODEV 2 #########

##### Python_Alistirmalar  #########

### Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.
### Type() metodunu kullanınız.

x = 8
type(x)
# int

y = 3.2
type(y)
# float

z = 8j + 18
type(z)
# complex

a = "Hello World"
type(a)
# str

b = True
type(b)
# bool

c = 23 < 22
type(c)
# bool

l = [1, 2, 3, 4]
type(l)
# list

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)
# dict

t = ("Machine Learning", "Data Science")
type(t)
# tuple

s = {"Python", "Machine Learning", "Data Science"}
type(s)
# set

##### Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
## kelime kelime ayırınız.

## text = "The goal is to turn data into information, and information into insight."

## Beklenen çıktı:
## ['THE', 'GOAL', 'IS', 'TO', 'TURN','DATA', 'INTO', 'INFORMATION','AND','INFORMATION','INTO', 'INSIGHT']

text = "The goal is to turn data into information, and information into insight."
new_text = text.upper().replace(",", " ").replace(".", " ").split()
print(new_text)


##### Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E","N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakınız.

len(lst)
# 11

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

print(lst[0])
print(lst[10])
# 'D'
# 'E'

print(f"Sifirinci indeks: {lst[0]}, Onuncu indeks: {lst[10]}")
## Sifirinci indeks: D, Onuncu indeks: E

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

new_list = lst[:4]
print(f"olusturulan liste: {new_list}")
## ["D", "A", "T", "A"]

# Adım 4: Sekizinci indeksteki elemanı siliniz.

lst.pop(8)
print(lst)
#['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E']

del lst[8]
print(f"new_list: {lst}")
## new_list: ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E']

# Adım 5: Yeni bir eleman ekleyiniz.

lst = ["D", "A", "T", "A", "S", "C", "I", "E","N", "C", "E"]
lst.append("F")
## ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E', 'F']

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8, "N")
print(lst)
## ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'N', 'C', 'E', 'F']


##### Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.


dict = {'Christian': ["America",18],
        'Daisy': ["England",12],
        'Antonio': ["Spain",22],
        'Dante': ["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()
# dict_keys(['Christian', 'Daisy', 'Antonio', 'Dante'])

# Adım 2: Value'lara erişiniz.

dict.values()
# dict_values([['America', 18], ['England', 12], ['Spain', 22], ['Italy', 25]])


# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict['Daisy'][1] = 13

#{'Christian': ['America', 18],
# 'Daisy': ['England', 13],
# 'Antonio': ['Spain', 22],
# 'Dante': ['Italy', 25]}


# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict['Ahmet'] = ['Turkey', 24]
# {'Christian': ['America', 18],
#  'Daisy': ['England', 13],
#  'Antonio': ['Spain', 22],
#  'Dante': ['Italy', 25],
#  'Ahmet': ['Turkey', 24]}

# Adım 5: Antonio'yu dictionary'den siliniz.

del dict['Antonio']

# {'Christian': ['America', 18],
# 'Daisy': ['England', 13],
# 'Dante': ['Italy', 25],
# 'Ahmet': ['Turkey', 24]}


## Görev 5: Argüman olarak bir liste alan, listenin içerisindeki
# tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]

def sayilar(l):
    cift_sayilar = []
    tek_sayilar = []

    for sayi in l:
        if sayi % 2 == 0:
            cift_sayilar.append(sayi)
        else:
            tek_sayilar.append(sayi)
    return cift_sayilar, tek_sayilar

print("Cift sayilar:", ciftler)
print("Tek sayilar:", tekler)


##### Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]


for index, ogrenci in enumerate(ogrenciler[:3], 1):
    print(f"Muhendislik Fakultesi {index}. ogrenci: {ogrenci}")
for index, ogrenci in enumerate(ogrenciler[3:], 1):
    print(f"Tip Fakultesi {index}. ogrenci: {ogrenci}")


##### Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu,
# kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for kod, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {kod} kodlu dersin kontenjani {kontenjan} kisidir.")

# beklenen cikti:

# Kredisi 3 olan CMP1005 kodlu dersin kontenjani 30 kisidir.
# Kredisi 4 olan PSY1001 kodlu dersin kontenjani 75 kisidir.
# Kredisi 2 olan HUK1005 kodlu dersin kontenjani 150 kisidir.
# Kredisi 4 olan SEN2204 kodlu dersin kontenjani 25 kisidir.




##### Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise
# ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.


kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


kume1.issuperset(kume2)
# kapsamiyor

kume1.intersection(kume2)
kume2.difference(kume1)



##### Odev 3 List Comprehension

##### Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
#  harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

new_columns = ["NUM_" + col.upper() if df[col].dtypes in ['float', 'int'] else col.upper() for col in df.columns]

print(new_columns)



##### Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
değişkenlerin isimlerinin sonuna "FLAG" yazınız


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns ]

df.columns = [col + "FLAG_" if "NO" not in col else col for col in df.columns]



##### Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
##    değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_df)





Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz












