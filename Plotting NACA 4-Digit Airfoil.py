import numpy as np
import matplotlib.pyplot as plt

def naca4_digit_airfoil(code, n_points=100):
    chord_length=1.0

    m = int(code[0]) / 100.0  # Maximum camber
    p = int(code[1]) / 10.0   # Position of maximum camber (x/c)
    t = int(code[2:]) / 100.0 # Maximum thickness

    beta = np.linspace(0, np.pi, n_points)
    x = (1 - np.cos(beta)) / 2 * chord_length

    # Thickness distribution
    yt = (t / 0.2) * (
        0.2969 * np.sqrt(x / chord_length)
        - 0.1260 * (x / chord_length)
        - 0.3516 * (x / chord_length)**2
        + 0.2843 * (x / chord_length)**3
        - 0.1015 * (x / chord_length)**4
    )

    # Camber line and slope
    yc = np.zeros_like(x)
    dyc_dx = np.zeros_like(x)
    for i in range(len(x)):
        if x[i] < p * chord_length:
            yc[i] = (m / p**2) * (2 * p * (x[i] / chord_length) - (x[i] / chord_length)**2)
            dyc_dx[i] = (2 * m / p**2) * (p - x[i] / chord_length)
        else:
            yc[i] = (m / (1 - p)**2) * ((1 - 2 * p) + 2 * p * (x[i] / chord_length) - (x[i] / chord_length)**2)
            dyc_dx[i] = (2 * m / (1 - p)**2) * (p - x[i] / chord_length)

    theta = np.arctan(dyc_dx)

    # Upper and lower surfaces
    y_upper = yc + yt * np.cos(theta)
    y_lower = yc - yt * np.cos(theta)

    return x, y_upper, y_lower, yc,n_points

#Usage
naca_code = "2412" #Input Desired Airfoil
x, y_upper, y_lower, yc,n_points = naca4_digit_airfoil(naca_code)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x, y_upper, label="Upper Surface", color="blue")
plt.plot(x, y_lower, label="Lower Surface", color="red")
plt.plot(x, yc, label="Camber Line", color="green", linestyle="--")
plt.fill_between(x, y_lower, y_upper, color="grey", alpha=0.5)
plt.title(f"NACA {naca_code} Airfoil")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
