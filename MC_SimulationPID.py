import numpy as np
import matplotlib.pyplot as plt

# Transfer fonksiyonu
def transfer_function(P, t):
    Kp = 1.0
    Ki = 0.01
    Kd = 0.01
    Kt = 0.001
    I = Kp * (2 - P) + Ki * np.trapz(2 - P, t) + Kd * np.gradient(P, t) + Kt * (-0.45) * np.heaviside(2 - P, 1)
    return I

# Monte Carlo yöntemi ile 600 adet rastgele P(t) değeri üret
np.random.seed(0)
P = np.random.uniform(0, 12, size=600)
t = np.arange(600)

# Rastgele P(t) değerlerini kullanarak I(t) değerlerini hesapla
I = transfer_function(P, t)

# I(t) ve P(t) değerlerini grafik üzerinde göster
plt.plot(t, I, label="I(t) (N*s)")
plt.plot(t, P, label="P(t) (m/s)")
plt.xlabel("t")
plt.ylabel("I")
plt.legend()
plt.show()
