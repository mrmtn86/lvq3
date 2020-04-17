# In[1]

import numpy as np
from ResimGosterici import resimGoster
import DosyaIslemci

data = DosyaIslemci.oku("data/uzaklikMatrix.pkl")

setler = data[0]
matrixler = data[1]


def uzaklikHesapla(vektor1, vektor2):
    return np.sqrt(np.sum((vektor1 - vektor2) ** 2))


def enUZakVektoruHesapla(vektorlerIndexler, sayiIndex):
    uzakliklarMatix = matrixler[sayiIndex]
    toplam_vektor = len(uzakliklarMatix)

    enUZakVEktorDegeri = 0  # ilk degeri salla
    enuzakIndex = -1

    for i in range(toplam_vektor):
        uzaklikToplamTmp = 0

        for j in vektorlerIndexler:

            if (vektorlerIndexler.__contains__(i)):
                continue

            uzaklikToplamTmp += uzakliklarMatix[j, i]

        if enUZakVEktorDegeri < uzaklikToplamTmp:
            enUZakVEktorDegeri = uzaklikToplamTmp
            enuzakIndex = i

    return enuzakIndex


def enUzakVektorleriGetir(sayiIndex):
    uzakliklarMatix = matrixler[sayiIndex]
    toplam_vektor = len(uzakliklarMatix)
    v1, v2 = 0, 1
    for k in range(toplam_vektor):
        for l in range(toplam_vektor):
            if k == l:
                continue
            enUzakTemp = uzakliklarMatix[v1, v2]
            uzaklikItr = uzakliklarMatix[k, l]
            if uzaklikItr > enUzakTemp:
                v1, v2 = k, l
    return v1, v2


def uzakVektorleriOlustur(setBasinaAdet):
    result = np.zeros((10, setBasinaAdet, 28 * 28), dtype=float)
    for sayiIndexItr in range(len(matrixler)):
        # if True :
        #     sayiIndexItr = 2
        vektorSeti = setler[sayiIndexItr]

        v1, v2 = enUzakVektorleriGetir(sayiIndexItr)

        result[sayiIndexItr, 0] = vektorSeti[v1]
        result[sayiIndexItr, 1] = vektorSeti[v2]

        uzakVektorlerIndexler = [v1, v2]

        for i in range(setBasinaAdet - 2):
            enUzakVektorIndex = enUZakVektoruHesapla(uzakVektorlerIndexler, sayiIndexItr)
            result[sayiIndexItr, i + 2] = vektorSeti[enUzakVektorIndex]
            uzakVektorlerIndexler.append(enUzakVektorIndex)

        # resimGoster(uzakVektorler, (len(uzakVektorler), 1))
    return result


# In[1]
#vektors = uzakVektorleriOlustur(5)

