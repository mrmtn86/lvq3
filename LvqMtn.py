import numpy as np
import matplotlib.pyplot as plt
import time


class LvqMtn:
    def __init__(self, girisVektorUzunlugu, ciktiSayisi, ciktiBasinaAraElemanSayisi, ogrenmeKatsayisi):
        self.girisVektorUzunlugu = girisVektorUzunlugu
        self.ciktiSayisi = ciktiSayisi
        self.ciktiBasinaAraElemanSayisi = ciktiBasinaAraElemanSayisi
        self.ogrenmeKatsayisi = ogrenmeKatsayisi
        self.agiOlustur()

    def agiOlustur(self):
        self.araElemanlar = []
        for i in range(self.ciktiSayisi):
            for j in range(self.ciktiBasinaAraElemanSayisi):
                araEleman = i, np.random.rand(self.girisVektorUzunlugu)
                self.araElemanlar.append(araEleman)

    def egit(self, girdiler, etiketler):

        for i in range(len(girdiler)):
            girdiItr = girdiler[i]
            araEleman = self.enYakinAraElemaniGetir(girdiItr)
            if araEleman[0] == etiketler[i]:
                self.yakinlastir(araEleman, girdiItr)
            else:
                dogruAraEleman = self.enYakinAraElemaniGetir(girdiItr, etiketler[i])
                self.yakinlastir(dogruAraEleman, girdiItr)
                self.uzaklastir(araEleman, girdiItr)

            if i % 100 == 0:
                print(i)

                self.araElemanlariGorsellestir(i)

    def enYakinAraElemaniGetir(self, girdi, etiket=None):
        enyakinEleman = ""
        enYakindakiElemaninUzkligi = float('inf')

        for i in range(len(self.araElemanlar)):

            araElemanItr = self.araElemanlar[i]
            uzaklikHesaplanan = self.uzaklikHesapla(araElemanItr[1], girdi)

            dahaYakin = uzaklikHesaplanan < enYakindakiElemaninUzkligi
            etiketUygun = etiket is None or etiket == araElemanItr[0]

            if dahaYakin and etiketUygun:
                enyakinEleman = araElemanItr
                enYakindakiElemaninUzkligi = uzaklikHesaplanan

        return enyakinEleman

    def uzaklikHesapla(self, vektor1, vektor2):
        return np.sqrt(np.sum((vektor1 - vektor2) ** 2))

    def yakinlastir(self, oynakV, sabitV):
        for i in range(len(sabitV)):
            oynakV[1][i] = oynakV[1][i] + self.ogrenmeKatsayisi * (sabitV[i] - oynakV[1][i])

    def uzaklastir(self, oynakV, sabitV):
        for i in range(len(sabitV)):
            oynakV[1][i] = oynakV[1][i] - self.ogrenmeKatsayisi * (sabitV[i] - oynakV[1][i])

    def test(self, test_imgs, test_labels):
        basari = 0
        for i in range(len(test_imgs)):
            enYakinAraElaman = self.enYakinAraElemaniGetir(test_imgs[i])
            if (enYakinAraElaman[0] == test_labels[i]):
                basari = basari + 1
        return basari / len(test_imgs) * 100

    def tahminEt(self, tahminSayi):
        enyakinEleman = self.enYakinAraElemaniGetir(tahminSayi[1])
        uzaklik = self.uzaklikHesapla(tahminSayi[1], enyakinEleman[1])
        return enyakinEleman[0], uzaklik

    def araElemanlariGorsellestir(self, i):


        for i in range(len(self.araElemanlar)):
            plt.subplot(3, 4, i + 1)  # the number of images in the grid is 5*5 (25)
            plt.imshow(self.araElemanlar[i][1].reshape((28, 28)), cmap="Greys")


        plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[]);
        plt.show()

