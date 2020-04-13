import numpy as np
import matplotlib.pyplot as plt


def veriHazirla():
    return np.random.randint(0, 255, (30, 3))


siniflar = ["KIRMIZI", "YEŞİL", "MAVİ"]

veriler = veriHazirla()

print(veriler)

plt.imshow([[(120, 120, 0)]])
plt.show()

