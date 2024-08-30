from nt import remove
##### Odev 1 #####

##### Virtual Environment Oluşturma #####

## Görev 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.

## Cevap: conda create –n myenv faruk
##        conda install python 3


## Görev 2: Oluşturduğunuz environment'ı aktife diniz.
## Cevap:   conda activate env faruk


## Görev 3: Yüklü paketleri listeleyiniz.
## Cevap:   conda list


## Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
## Cevap:   conda install Numpy Pandas=1.2.1


## Görev 5: İndirilen Numpy'ın versiyonu nedir?
## Cevap:


## Görev 6: Pandas'ı upgrade ediniz. Yeni versiyonu nedir?
## Cevap:   conda uppgrade Pandas


## Görev 7: Numpy'ı environment'tan siliniz.
## Cevap:   conda remove Numpy


## Görev 8: Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.
## Cevap:   conda install Seaborn matplotlib


## Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
## Cevap:


## Görev 10: Oluşturduğunuz environment'i siliniz. Önce environment'i deactivate ediniz.
## Cevap:    conda deactivate
             conda remove env faruk