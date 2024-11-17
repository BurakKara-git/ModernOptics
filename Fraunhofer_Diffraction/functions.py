import numpy as np
from scipy.special import j1
import matplotlib.pyplot as plt


# Define Jinc Function
def jinc(x):
    if x == 0:
        return 1 / 2
    return j1(x) / x


jinc = np.vectorize(jinc)

def sinc(x):
    if x == 0:
        return 1
    return np.sin(x)/x

sinc = np.vectorize(sinc)


# Define Normalize Intensities:
def normalize(x):
    x /= x.sum(axis=1)[:, np.newaxis]
    return x


def plot(X, Y, I, title):
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.contourf(
        X * 1e3, Y * 1e3, I, levels=100, cmap="plasma", vmin=0., vmax=1e-4
    )  # Convert x, y to mm
    plt.colorbar(label="Intensity")
    plt.title(title)
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.grid(True)
    plt.show()
    plt.clf
