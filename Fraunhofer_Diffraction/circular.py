import numpy as np
from functions import jinc
import matplotlib.pyplot as plt


def fraunhofer_diffraction_circular(x, y, lambda_, z, D, b, I_0):
    r = np.sqrt(x**2 + y**2 + z**2)
    I = (
        I_0
        * (jinc(np.pi * D * r / (lambda_ * z)) * (np.pi * D**2) / (4 * lambda_ * z))
        ** 2
    )
    return I


def main():
    # Parameters
    lambda_ = 1e-6  # Wavelength(m)
    z = 1.0  # Distance to screen(m)
    I_0 = 1.0  # Intensity
    D = 0.1e-3  # Diameter
    b = 5 * D / 2  # Positions

    # Create meshgrid
    minimum = -0.5
    maximum = 0.5
    num = 1000
    r = np.linspace(minimum, maximum, num)
    X, Y = np.meshgrid(r, r)

    I = fraunhofer_diffraction_circular(X, Y, lambda_, z, D, b, I_0)

    # Plot
    plt.figure(1,(16,9))
    title = "Fraunhofer Diffraction Pattern for Circular Aperture of Diameter {}mm\n".format(D*1e3)
    plt.contourf(
        X * 1e3, Y * 1e3, I, levels=100, cmap="plasma"
    )  # Convert x, y to mm
    plt.colorbar(label="Intensity")
    plt.title(title)
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.grid(True)
    
    plt.savefig("circular.png")


if __name__ == "__main__":
    main()
