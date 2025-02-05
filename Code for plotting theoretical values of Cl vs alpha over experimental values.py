import numpy as np
import matplotlib.pyplot as plt
 
# Load the background image
background_image_path = 'EXPDATA.png'  # Replace with your actual image file path
img = plt.imread(background_image_path)  # Load the image as an array

plt.figure(figsize=(10,10))
plt.imshow(img,extent=[-32,32,-2,3.6],aspect = 17)
plt.autoscale(False)


# Define constants for the functions
alpha_0_1 = -0.0362546 # Second function
alpha_0_2 = -0.032807   # Third function
 
# Define alpha range (x-axis values) in radians
alpha = np.linspace(-32, 32, 100)
 
# Calculate Cl for the three functions
Cl_main = 2 * np.pi * np.radians(alpha)
Cl_1 = 2 * np.pi * (np.radians(alpha) - alpha_0_1)
Cl_2 = 2 * np.pi * (np.radians(alpha) - alpha_0_2)
 
plt.plot(alpha, Cl_1, label=r'$NACA-2412$', color='r', linestyle='--', linewidth=2, zorder=2)

#Add labels, title, grid, and legend
plt.xlabel('Angle of Attack (α) [Degrees]', fontsize=12)
plt.ylabel('Lift Coefficient ($C_l$)', fontsize=12)
plt.title('Lift Coefficient vs Angle of Attack for NACA 2412', fontsize=14)
plt.legend(fontsize=12)

