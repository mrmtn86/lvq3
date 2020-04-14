# In[2]
import pickle

with open("data/pickled_mnist.pkl", "br") as fh:
    data = pickle.load(fh)

train_imgs = data[0]
test_imgs = data[1]
train_labels = data[2]
test_labels = data[3]
train_labels_one_hot = data[4]
test_labels_one_hot = data[5]

image_size = 28  # width and length
no_of_different_labels = 10  # i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size


# In[3]
import LvqMtn


ysa = LvqMtn.LvqMtn(len(train_imgs[0]), 10, 30, 0.01, 1500)

# In[4]
import matplotlib.pyplot as plt

ysa.egit(train_imgs, train_labels)




# In[5]
basari = ysa.test(test_imgs, test_labels)
print(basari)

# In[6]
tahminIndex = 200
tahminSayi = test_labels[tahminIndex], test_imgs[tahminIndex]
tahminSonuc = ysa.tahminEt(tahminSayi)

print("", tahminSayi[0], "->", tahminSonuc)
