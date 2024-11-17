import numpy as np
import matplotlib.pyplot as plt
from functions import normalize, sinc


# Define Fraunhofer Diffraction Function
def grating(x, y, lambda_, z, delta_x, delta_y, h, N, I_0):
    I_peak = I_0 * (N * delta_x * delta_y / (lambda_ * z)) ** 2
    I = (
        I_peak
        * (
            sinc(np.pi * delta_x * x / (lambda_ * z))
            * np.sin(N * np.pi * h * x / (lambda_ * z))
            / np.sin(np.pi * h * x / (lambda_ * z))
        )
        ** 2
    )
    return I


def main():
    # Parameters
    I_0 = 1
    delta_x = 5e-6
    delta_y = 1.0
    lambda_ = 500e-9
    h = 2 * delta_x
    N_tuple = (1, 2, 5, 10, 100, 1000)
    num_tuple = (50, 100, 250, 500, 1000, 5000)
    f = 1.0
    z = f
    scale = z*lambda_/h

    # Create meshgrid
    minimum = -2
    maximum = 2

    for i in range(len(N_tuple)):
        N = N_tuple[i]
        num = num_tuple[i]
        r = np.linspace(minimum*scale, maximum*scale, num)
        X, Y = np.meshgrid(r, r)
        I = grating(X, Y, lambda_, z, delta_x, delta_y, h, N, I_0)
        title = "Grating Diffraction Intensity for N = {}".format(N)
        plt.figure(1,(16,9))

        plt.subplot(121)
        plt.plot(X[0]/scale,I[0]) # Convert x to x/z in units of lambda/h
        plt.title(title)
        plt.xlabel("x/z in units of lambda/h")
        plt.ylabel("Intensity")
        
        
        plt.subplot(122)
        plt.contourf(
            X/scale, Y, I, levels=100, cmap="plasma"
        )  # Convert x to x/z in units of lambda/h 
        plt.colorbar(label="Intensity")
        plt.title(title)
        plt.xlabel("x/z in units of lambda/h")
        plt.ylabel("y (mm)")
        plt.grid(True)
        plt.savefig("grating_{}.png".format(N))
        plt.clf()


if __name__ == "__main__":
    main()
