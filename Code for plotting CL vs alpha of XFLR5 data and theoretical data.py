file_path = 'CL vs alpha.csv'
data = pd.read_csv(file_path)
alpha = data.iloc[:, 0]
CL = data.iloc[:, 1]
elip = 4.71*(np.radians(alpha) + 0.03625)
taper = 4.361*(np.radians(alpha) + 0.03625)
straight = 4.204*(np.radians(alpha) + 0.03625)
plt.figure(figsize=(10, 6))
plt.plot(alpha, CL, linestyle='-', color='r', label="XFLR5 Data")
plt.plot(alpha, elip, label = "Eliptical Wing")
plt.plot(alpha, taper, label = "Tapered Wing")
plt.plot(alpha, straight, label = "Straight Wing")
plt.xlabel('$\\alpha$ (degrees)')
plt.ylabel('$C_L$')
plt.xlim(-8.5, 12.5)
plt.title('$C_L$ vs $\\alpha$')
plt.legend()
plt.grid(True)
plt.show()

Code for plotting CL vs CD of XFLR5 data and theoretical data

file_path = 'CL vs CD.csv'
data = pd.read_csv(file_path)
CD = data.iloc[:, 0]
CL = data.iloc[:, 1]
delta_taper = 0.01
delta_straight = 0.05
AR = 6
CDi_taper = CL**2 * (1 + delta_taper) / (np.pi * AR)
CDi_straight = CL**2 * (1 + delta_straight) / (np.pi * AR)
plt.figure(figsize=(10, 6))
plt.plot(CL, CD, linestyle='-', color='r', label="XFLR5 Data")
plt.plot(CL, CDi_taper, label = "Tapered Wing")
plt.plot(CL, CDi_taper, label = "Straight Wing")
plt.xlabel('$C_L$')
plt.ylabel('$C_D$')
plt.title('$C_D$ vs $C_L$')
plt.legend()
plt.grid(True)
plt.show()
