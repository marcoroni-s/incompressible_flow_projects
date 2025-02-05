# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the NACA2412 data
file_name = "Polar_Graph.xlsx"  
data = pd.read_excel(file_name)

# Convert columns to numeric values
alpha = pd.to_numeric(data['Alpha'], errors='coerce')
lift3 = pd.to_numeric(data['T1_Re3.000_M0.00_N9.0'], errors='coerce')
lift6 = pd.to_numeric(data['T1_Re6.000_M0.00_N9.0'], errors='coerce')
lift9 = pd.to_numeric(data['T1_Re9.000_M0.00_N9.0'], errors='coerce')

# Drop rows with NaN values
cleaned_data = pd.DataFrame({'Alpha': alpha, 'Lift3': lift3, 'Lift6': lift6, 'Lift9': lift9}).dropna()

# Extract data
alpha_cleaned = cleaned_data['Alpha']
lift3_cleaned = cleaned_data['Lift3']
lift6_cleaned = cleaned_data['Lift6']
lift9_cleaned = cleaned_data['Lift9']

# Create the plot
Code for plotting CD vs CL of XFLR5 data with different flap angles

file_path = 'CD vs CL flaps.csv'
data = pd.read_csv(file_path)
CL_40 = data.iloc[:, 0]
CD_40 = data.iloc[:, 1]
CL_20 = data.iloc[:, 3]
CD_20 = data.iloc[:, 4]
CL_10 = data.iloc[:, 6]
CD_10 = data.iloc[:, 7]
CL_0 = data.iloc[:, 9]
CD_0 = data.iloc[:, 10]
plt.figure(figsize=(10, 6))
plt.plot(alpha_cleaned, lift3_cleaned, label=r'Re = $3 \times 10^6$', linestyle='-')
plt.plot(alpha_cleaned, lift6_cleaned, label=r'Re = $6 \times 10^6$', linestyle='-')
plt.plot(alpha_cleaned, lift9_cleaned, label=r'Re = $9 \times 10^6$', linestyle='-')

# Set bounds for x-axis and ensure -8 and 12 are the bounds for our x-axis
plt.xlim(-8, 12)
plt.xticks(range(-8, 13, 2))  # Show ticks from -8 to 12 with step of 2

# Add labels, title, and legend
plt.xlabel(r'$\alpha$ (Angle of Attack in Degrees)')
plt.ylabel(r'Lift Coefficient ($C_l$)')
plt.title('Lift Coefficient vs Angle of Attack')
plt.plot(CL_40, CD_40, linestyle='-', color='r', label="40$^{\circ}$")
plt.plot(CL_20, CD_20, linestyle='-', color='y', label="20$^{\circ}$")
plt.plot(CL_10, CD_10, linestyle='-', color='g', label="10$^{\circ}$")
plt.plot(CL_0, CD_0, linestyle='-', color='b', label="0$^{\circ}$")
plt.xlabel('$C_L$')
plt.ylabel('$C_D$')
plt.title('$C_D$ vs $C_L$ Wing with 1/4 span flaps')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

