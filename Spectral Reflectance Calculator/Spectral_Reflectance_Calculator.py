import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin
from itertools import product
import os

# Constants
n_0 = 1  # Medium
n_t = 1.5  # Substrate
n_list = [1.35, 2.3]  # Index of Refractions to be Used
repeat = 8  # Total Number of Layers
initial_lambda = 600
L = initial_lambda / 4
lambdas = np.arange(200, 2000, 0.1, dtype=float)

# Create Plot Folder
path = "./plots_Spectral_Reflectance_Calculator"
if not os.path.exists(path=path):
    os.makedirs(path)


# Generate all Possible Orders
def find_orders(n_list=n_list, repeat=repeat):
    permutation = list(product(n_list, repeat=repeat))  # Cartesian Product
    result = []
    for candidate in permutation:
        # Use only repeat/2 many layers for each index of refraction
        if candidate.count(n_list[0]) == repeat / 2:
            result.append(candidate)
    return result


# Calculate reflectance
def calculate_r(M, n_0, n_t):
    numerator = M[0][0] * n_0 + M[0][1] * n_t * n_0 - M[1][0] - M[1][1] * n_t
    denominator = M[0][0] * n_0 + M[0][1] * n_t * n_0 + M[1][0] + M[1][1] * n_t
    r = numerator / denominator
    return r


# Plot and Save Figures
def plot(n_tuple, R_sublist, lambdas=lambdas):
    # Find Minimum and Maximum Values
    xmax = lambdas[np.argmax(R_sublist)]
    ymax = max(R_sublist)

    xmin = lambdas[np.argmin(R_sublist)]
    ymin = min(R_sublist)

    textmax = "max R={:.3f} at λ={:.2f}".format(ymax, xmax)
    textmin = "min R={:.3f} at λ={:.2f}".format(ymin, xmin)

    fig = plt.figure(figsize=(10, 5))

    # Plot Vertical Lines on Min and Max
    plt.axvline(x=xmax, color="red", label=textmax, linestyle="dotted")
    plt.axvline(x=xmin, color="blue", label=textmin, linestyle="dotted")

    # Plot Reflectance
    plt.plot(lambdas, R_sublist, label="Reflectance")
    plt.xlabel("Wavelength(nm)")

    # Calculate and Plot Transmittance
    T_sublist = [1 - r for r in R_sublist]
    plt.plot(lambdas, T_sublist, label="Transmittance")
    plt.xlabel("Wavelength(nm)")

    # Configure Plot and Save
    lgd = plt.legend(bbox_to_anchor=(1.0, 1), loc="upper left")
    plt.grid()
    plt.title("Configuration: {}".format(n_tuple))
    plt.savefig(
        "{}/{}.png".format(path, n_tuple),
        bbox_extra_artists=(lgd,),
        bbox_inches="tight",
    )

    # Close Plots
    plt.close()


# Loop Orderings and Lambdas to Calculate Reflectance
R_list = []
orders = find_orders()
print("Number of Coatings = ", len(orders))
for n_tuple in orders:
    R_sublist = []
    T_sublist = []
    for lammbda in lambdas:
        M_total = [[1, 0], [0, 1]]  # Identity Matrix
        for n in n_tuple:
            # Calculate Current Transfer Matrix
            k = 2 * np.pi * n / lammbda
            M_current = [
                [cos(k * L), -1j * sin(k * L) / n],
                [-1j * n * sin(k * L), cos(k * L)],
            ]

            # Multiple by Previous Matrix
            M_total = np.dot(M_total, M_current)

        # Calculate r and Reflectance
        r = calculate_r(M_total, n_0, n_t)
        R = np.absolute(r) ** 2
        R_sublist.append(R)

    # Plot the Reflectance/Transmittance
    plot(n_tuple, R_sublist)
    print(n_tuple)
    R_list.append(R_sublist)


max_ind = np.argmax(R_list, axis=None)
min_ind = np.argmin(R_list, axis=None)

max_row = int(max_ind / len(lambdas))
max_col = max_ind % len(lambdas)

min_row = int(min_ind / len(lambdas))
min_col = min_ind % len(lambdas)

print(
    "Min R = {}, for lambda = {}, order = {}".format(
        R_list[min_row][min_col], lambdas[min_col], orders[min_row]
    )
)
print(
    "Max R = {}, for lambda = {}, order = {}".format(
        R_list[max_row][max_col], lambdas[max_col], orders[max_row]
    )
)
