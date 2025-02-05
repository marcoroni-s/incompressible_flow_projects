import numpy as np
import matplotlib.pyplot as plt
 
alpha_0_1 = -0.0362546*1.5      # Second function
alpha_0_2 = -0.032807*2.5  # Third function
 
# Define alpha range (x-axis values) in radians
alpha = np.linspace(-10, 10, 100)
 
# Calculate Cl for the three functions
Cl_main = 2 * np.pi * (alpha)
Cl_1 = 2 * np.pi * (alpha - alpha_0_1)
Cl_2 = 2 * np.pi * (alpha - alpha_0_2)
 
# Create the plot
plt.figure(figsize=(8, 6))
 
# Plot the three functions
plt.plot(alpha, Cl_main, label=r'$NACA-0012$', color='b', linewidth=2)
plt.plot(alpha, Cl_1, label=r'$NACA-2412$', color='r', linestyle='--', linewidth=2)
plt.plot(alpha, Cl_2, label=r'$P2-Individual$', color='g', linestyle='-.', linewidth=2)
plt.xlim(-0.75, 0.75)
plt.ylim(-3.6, 3.6)    
 
tick_positions = np.linspace(-0.75, 0.75, 11)  # Tick positions in radians
tick_labels = np.degrees(tick_positions)   # Convert tick positions to degrees
plt.xticks(tick_positions, [f"{int(tick)}°" for tick in tick_labels])
 
plt.xlabel('Angle of Attack (α) [Degrees]', fontsize=12)
plt.ylabel('Lift Coefficient ($C_l$)', fontsize=12)
plt.title('Lift Coefficient vs Angle of Attack for NACA 0012, NACA 2412, and P2', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.show()
