import matplotlib.pyplot as plt


def resimGoster(vektorler, aciklama="", boyut=None, ):
    if boyut is None:
        boyut = (1, len(vektorler))
    plt.rcParams["figure.figsize"] = boyut

    for i in range(len(vektorler)):
        plt.subplot(boyut[1], boyut[0], i + 1)
        plt.imshow(vektorler[i].reshape((28, 28)), cmap="Greys")

    plt.xlabel(aciklama)
    plt.setp(plt.gcf().get_axes(), xticks=[456], yticks=[]);
    plt.show()
