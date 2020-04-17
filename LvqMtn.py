import numpy as np
import matplotlib.pyplot as plt
import MAtrixOpp


class ReferansVektorSeti:

    def __init__(self, sayi):
        self.tekrarEdenVektor = None
        self.tekarEtmeSayisi = 0
        self.sayi = sayi
        self.vektorler = []

    def vektorEkle(self, vektor):
        self.vektorler.append(vektor)


class ReferansVektor:

    def __init__(self, sayi: int, vektor: [], set: ReferansVektorSeti):
        self.tekarEtmeSayisi = 0
        self.sayi = sayi
        self.vektor = vektor
        self.set = set
        self.set.vektorEkle(self)

    def tekrarSayisiGetir(self):
        #  if self.set.tekrarEdenVektor == self:
        return self.tekarEtmeSayisi

    # return 0

    def tekrarArttir(self):
        self.tekarEtmeSayisi += 1
    # def tekrarArttir(self):
    #
    #     if self.set.tekrarEdenVektor != self:
    #         self.set.tekrarEdenVektor = self
    #         self.set.tekarEtmeSayisi = 0
    #
    #     self.set.tekarEtmeSayisi += 1


class LvqMtn:

    def __init__(self, giris_vektor_uzunlugu, ciktiSayisi, ciktiBasinaAraElemanSayisi, ogrenmeKatsayisi, cezaKatsayisi):
        self.cezaKatsayisi = cezaKatsayisi
        self.setler = []
        self.tekrarSayisi = 1
        self.referansVektorler = []
        self.girisVektorUzunlugu = giris_vektor_uzunlugu
        self.ciktiSayisi = ciktiSayisi
        self.ciktiBasinaAraElemanSayisi = ciktiBasinaAraElemanSayisi
        self.ogrenmeKatsayisi = ogrenmeKatsayisi
        self.agiOlustur2()

    def agiOlustur2(self):

        uzakVektors = MAtrixOpp.uzakVektorleriOlustur(self.ciktiBasinaAraElemanSayisi)

        for i in range(self.ciktiSayisi):

            set = ReferansVektorSeti(i)
            self.setler.append(set)

            for j in range(self.ciktiBasinaAraElemanSayisi):
                ara_eleman = ReferansVektor(i, uzakVektors[i, j], set)
                self.referansVektorler.append(ara_eleman)


    # def agiOlustur(self):
    #
    #     for i in range(self.ciktiSayisi):
    #
    #         set = ReferansVektorSeti(i)
    #         self.setler.append(set)
    #
    #         for j in range(self.ciktiBasinaAraElemanSayisi):
    #             ara_eleman = ReferansVektor(i, np.random.rand(self.girisVektorUzunlugu), set)
    #             self.referansVektorler.append(ara_eleman)

    def egit(self, girdiler, etiketler):

        for i in range(len(girdiler)):
            self.tekrarSayisi += 1
            girdiItr = girdiler[i]
            etiketItr = etiketler[i]

            enYakinEleman = self.enYakinAraElemaniGetir(girdiItr)

            if enYakinEleman.sayi != etiketItr:
                self.uzaklastir(enYakinEleman, girdiItr)

            enUygunEleman = self.settekiEnUygunuGetir(girdiItr, etiketItr)
            enUygunEleman.tekrarArttir()
            self.yakinlastir(enUygunEleman, girdiItr)

            if i % 2000 == 0:
                print(i)

                self.araElemanlariGorsellestir(i)

    def settekiEnUygunuGetir(self, girdi, etiket):

        vektorler = self.setinVektorleriniGetir(etiket)

        enyakinEleman = vektorler[0]

        enYakindakiElemaninUzkligi = self.agirlikliUzaklikHesapla(enyakinEleman, girdi)
        # enYakindakiElemaninUzkligi += enYakindakiElemaninUzkligi * enyakinEleman.tekrarSayisiGetir() * self.cezaKatsayisi

        for i in range(len(vektorler)):
            araElemanItr = vektorler[i]

            uzaklikHesaplanan = self.agirlikliUzaklikHesapla(araElemanItr, girdi)

            dahaYakin = uzaklikHesaplanan < enYakindakiElemaninUzkligi

            if not dahaYakin:
                continue

            enyakinEleman = araElemanItr
            enYakindakiElemaninUzkligi = uzaklikHesaplanan

        return enyakinEleman

    def setinVektorleriniGetir(self, etiket):
        for i in range(len(self.setler)):
            setItr = self.setler[i]
            if setItr.sayi == etiket:
                return setItr.vektorler

    # def enUygunAraElemaniGetir(self, girdi, etiket, etiketZorla):
    #     enyakinEleman = self.referansVektorler[0]
    #     enYakindakiElemaninUzkligi = self.uzaklikHesapla(self.referansVektorler[0].vektor, girdi)
    #
    #     for i in range(len(self.referansVektorler)):
    #
    #         araElemanItr = self.referansVektorler[i]
    #
    #         ayniEtiket = etiket == araElemanItr.sayi
    #
    #         uzaklikHesaplanan = self.uzaklikHesapla(araElemanItr.vektor, girdi)
    #
    #         if ayniEtiket:
    #             uzaklikHesaplanan += uzaklikHesaplanan * araElemanItr.tekrarSayisiGetir() * self.cezaKatsayisi
    #
    #         dahaYakin = uzaklikHesaplanan < enYakindakiElemaninUzkligi
    #
    #         if not dahaYakin:
    #             continue
    #
    #         etiketUygun = not etiketZorla or (ayniEtiket and etiketZorla)
    #
    #         if etiketUygun:
    #             enyakinEleman = araElemanItr
    #             enYakindakiElemaninUzkligi = uzaklikHesaplanan
    #
    #     return enyakinEleman

    def enYakinAraElemaniGetir(self, girdi):
        enyakinEleman = ""
        enYakindakiElemaninUzkligi = float('inf')

        for i in range(len(self.referansVektorler)):

            araElemanItr = self.referansVektorler[i]
            uzaklikHesaplanan = self.uzaklikHesapla(araElemanItr.vektor, girdi)

            dahaYakin = uzaklikHesaplanan < enYakindakiElemaninUzkligi

            if dahaYakin:
                enyakinEleman = araElemanItr
                enYakindakiElemaninUzkligi = uzaklikHesaplanan

        return enyakinEleman


    def tumReferanslaraolanUzakliklariHesapla(self, girdi):
        referanslaraUzakliklar = []

        for i in range(len(self.referansVektorler)):
            araElemanItr = self.referansVektorler[i]
            uzaklikHesaplanan = self.uzaklikHesapla(araElemanItr.vektor, girdi)
            refUzakligi = uzaklikHesaplanan, araElemanItr
            referanslaraUzakliklar.append(refUzakligi)

        referanslaraUzakliklar.sort(key=lambda x: x[0])
        return referanslaraUzakliklar

    def agirlikliUzaklikHesapla(self, referansVektor, vektor2):
        uzaklikHesaplanan = np.sqrt(np.sum((referansVektor.vektor - vektor2) ** 2))
        tekrar = referansVektor.tekrarSayisiGetir()
        if tekrar > 0:
            ceza = np.sqrt(uzaklikHesaplanan * tekrar) * self.cezaKatsayisi / self.tekrarSayisi
            uzaklikHesaplanan += ceza
        return uzaklikHesaplanan

    def uzaklikHesapla(self, vektor1, vektor2):
        return np.sqrt(np.sum((vektor1 - vektor2) ** 2))

    def yakinlastir(self, oynakV, sabitV):
        v = oynakV.vektor
        for i in range(len(sabitV)):
            v[i] = v[i] + self.ogrenmeKatsayisi * (sabitV[i] - v[i])

    def uzaklastir(self, oynakV, sabitV):
        v = oynakV.vektor
        for i in range(len(sabitV)):
            v[i] = v[i] - self.ogrenmeKatsayisi * (sabitV[i] - v[i])

    def test(self, test_imgs, test_labels):
        basari = 0
        for i in range(len(test_imgs)):
            enYakinAraElaman = self.enYakinAraElemaniGetir(test_imgs[i])
            if enYakinAraElaman.sayi == test_labels[i]:
                basari = basari + 1
        return basari / len(test_imgs) * 100

    def tahminEt(self, tahminSayi):
        enyakinEleman = self.enYakinAraElemaniGetir(tahminSayi[1])
        uzaklik = self.uzaklikHesapla(tahminSayi[1], enyakinEleman.vektor)
        return enyakinEleman, uzaklik

    def araElemanlariGorsellestir(self, i):

        plt.rcParams["figure.figsize"] = (self.ciktiBasinaAraElemanSayisi, self.ciktiSayisi)
        for i in range(len(self.referansVektorler)):
            plt.subplot(self.ciktiSayisi, self.ciktiBasinaAraElemanSayisi,
                        i + 1)  # the number of images in the grid is 5*5 (25)
            referanVektor = self.referansVektorler[i]
            plt.imshow(referanVektor.vektor.reshape((28, 28)), cmap="Greys")
            plt.xlabel(referanVektor.tekarEtmeSayisi)

        plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[]);
        plt.show()
