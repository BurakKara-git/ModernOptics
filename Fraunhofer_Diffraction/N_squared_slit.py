import numpy as np
import matplotlib.pyplot as plt
from single_slit import fraunhofer_diffraction_single


def fraunhofer_diffraction_N_squared(x, y, lambda_, z, delta_x, delta_y, h, s, N, I_0):
    term_1 = np.sin(N * np.pi * h * x / (lambda_ * z)) / np.sin(
        np.pi * h * x / (lambda_ * z)
    )
    term_2 = np.sin(N * np.pi * s * y / (lambda_ * z)) / np.sin(
        np.pi * s * y / (lambda_ * z)
    )

    I_single_slit = fraunhofer_diffraction_single(
        x, y, lambda_, z, delta_x, delta_y, I_0
    )
    return I_single_slit * ((term_1 * term_2) ** 2)


def main():
    # Parameters
    lambda_ = 1e-6  # Wavelength(m)
    z = 1.0  # Distance to screen(m)
    delta_x = 0.1e-3  # Slit width(m)
    delta_y = 0.2e-3  # Slit height(m)
    I_0 = 1.0  # Intensity
    h = delta_x * 2
    s = delta_y * 2
    N = 5 # Number of slit in a row/column (for sanity check, try 1)
    vmax = 1e-1 # Choose vmax for better visibility

    # Create meshgrid
    minimum = -0.01
    maximum = 0.01
    num = 1000
    r = np.linspace(minimum, maximum, num)
    X, Y = np.meshgrid(r, r)

    I = fraunhofer_diffraction_N_squared(
        X, Y, lambda_, z, delta_x, delta_y, h, s, N, I_0
    )

    #Plot
    plt.figure(1,(16,9))
    plt.subplot(122)
    title = "Fraunhofer Diffraction Pattern for {} Slits in Array\n Normalized ColorBar".format(N**2)
    plt.contourf(
        X * 1e3, Y * 1e3, I, levels=100, cmap="plasma", vmin=0., vmax=vmax
    )  # Convert x, y to mm
    plt.colorbar(label="Intensity")
    plt.title(title)
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.grid(True)
    
    plt.subplot(121)
    title = "Fraunhofer Diffraction Pattern for {} Slits in Array".format(N**2)
    plt.contourf(
        X * 1e3, Y * 1e3, I, levels=100, cmap="plasma"
    )  # Convert x, y to mm
    plt.colorbar(label="Intensity")
    plt.title(title)
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.grid(True)

    plt.savefig("{}_slits.png".format(N**2))


if __name__ == "__main__":
    main()
