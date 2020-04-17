# In[1]
import pickle
import numpy as np
import matplotlib.pyplot as plt


def uzaklikHesapla(vektor1, vektor2):
    return np.sqrt(np.sum((vektor1 - vektor2) ** 2))


with open("data/pickled_mnist.pkl", "br") as fh:
    data = pickle.load(fh)

imgs = data[0]
labels = data[2]

train_labels_one_hot = data[4]
test_labels_one_hot = data[5]

setler = [[], [], [], [], [], [], [], [], [], []]
matrixler = list(range(10))
for i in range(len(labels)):
    label = int(labels[i][0])
    setler[label].append(imgs[i])

for j in range(len(setler)):
    vektorler = setler[j]
    toplamVektor = len(vektorler)
    uzakliklarMatix = np.zeros((toplamVektor, toplamVektor), dtype=None)
    matrixler[j] = uzakliklarMatix

    for k in range(toplamVektor):
        if k % 100 == 0:
            print('sayi : ', j, '  sayac: ', k, '/', toplamVektor)

        for l in range(toplamVektor):
            if k == l:
                continue
            uzakliklarMatix[k, l] = uzaklikHesapla(vektorler[k], vektorler[l])

with open("data/uzaklikMatrix.pkl", "bw") as fh:
    data = (setler,
            matrixler)
    pickle.dump(data, fh)


