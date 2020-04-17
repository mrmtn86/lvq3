import pickle


def oku(dosyaPath):
    with open(dosyaPath, "br") as fh:
        return pickle.load(fh)
