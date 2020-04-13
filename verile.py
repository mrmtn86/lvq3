import numpy as np
import matplotlib.pyplot as plt

image_size = 28
no_of_different_labels = 10
image_pixels = image_size * image_size
data_path = "data/"

train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")
# In[0]

fac = 0.99 / 255
train_imgs = np.asfarray(train_data[:, 1:]) * fac + 0.01
test_imgs = np.asfarray(test_data[:, 1:]) * fac + 0.01

train_labels = np.asfarray(train_data[:, :1])
test_labels = np.asfarray(test_data[:, :1])

for i in range(10):
    img = train_imgs[i].reshape((28, 28))
    plt.imshow(img, cmap="Greys")
    plt.show()

lr = np.arange(10)

for label in range(10):
    one_hot = (lr == label).astype(np.int)
    print("label: ", label, " in one-hot representation: ", one_hot)

lr = np.arange(no_of_different_labels)

# transform labels into one hot representation
train_labels_one_hot = (lr == train_labels).astype(np.float)
test_labels_one_hot = (lr == test_labels).astype(np.float)

# we don't want zeroes and ones in the labels neither:
train_labels_one_hot[train_labels_one_hot == 0] = 0.01
train_labels_one_hot[train_labels_one_hot == 1] = 0.99
test_labels_one_hot[test_labels_one_hot == 0] = 0.01
test_labels_one_hot[test_labels_one_hot == 1] = 0.99
# In[1]
import pickle

with open("data/pickled_mnist.pkl", "bw") as fh:
    data = (train_imgs,
            test_imgs,
            train_labels,
            test_labels,
            train_labels_one_hot,
            test_labels_one_hot)
    pickle.dump(data, fh)
