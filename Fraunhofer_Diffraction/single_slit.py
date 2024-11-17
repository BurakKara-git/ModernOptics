import numpy as np
from functions import plot, sinc
import matplotlib.pyplot as plt


# Define Fraunhofer Diffraction Function
def fraunhofer_diffraction_single(x, y, lambda_, z, delta_x, delta_y, I_0):
    sinc_x = sinc(np.pi * (delta_x * x) / (lambda_ * z))
    sinc_y = sinc(np.pi * (delta_y * y) / (lambda_ * z))
    return (
        I_0 * (((delta_x * delta_y) / (lambda_ * z)) ** 2) * (sinc_x**2) * (sinc_y**2)
    )


def main():
    # Parameters
    lambda_ = 1e-6  # Wavelength(m)
    z = 1.0  # Distance to screen(m)
    delta_x = 0.1e-3  # Slit width(m)
    delta_y = 0.2e-3  # Slit height(m)
    I_0 = 1.0  # Intensity
    vmax = 1e-4 # Choose vmax for better visibility

    # Create meshgrid
    minimum = -0.02
    maximum = 0.02
    num = 1000
    r = np.linspace(minimum, maximum, num)
    X, Y = np.meshgrid(r, r)
    I = fraunhofer_diffraction_single(X, Y, lambda_, z, delta_x, delta_y, I_0)

    #Plot
    plt.figure(1,(16,9))
    plt.subplot(122)
    title = "Fraunhofer Diffraction Pattern for a Single Slit\n Normalized ColorBar"
    plt.contourf(
        X * 1e3, Y * 1e3, I, levels=100, cmap="plasma", vmin=0., vmax=vmax
    )  # Convert x, y to mm
    plt.colorbar(label="Intensity")
    plt.title(title)
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.grid(True)
    
    plt.subplot(121)
    title = "Fraunhofer Diffraction Pattern for a Single Slit\n"
    plt.contourf(
        X * 1e3, Y * 1e3, I, levels=100, cmap="plasma"
    )  # Convert x, y to mm
    plt.colorbar(label="Intensity")
    plt.title(title)
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.grid(True)

    plt.savefig("single_slit.png")


if __name__ == "__main__":
    main()
