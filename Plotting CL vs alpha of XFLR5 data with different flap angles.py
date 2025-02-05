file_path = 'CL vs alpha flaps.csv'
data = pd.read_csv(file_path)
alpha = data.iloc[:, 0]
CL_40 = data.iloc[:, 1]
CL_20 = data.iloc[:, 4]
CL_10 = data.iloc[:, 7]
CL_0 = data.iloc[:, 10]
plt.figure(figsize=(10, 6))
plt.plot(alpha, CL_40, linestyle='-', color='r', label="40$^{\circ}$")
plt.plot(alpha, CL_20, linestyle='-', color='y', label="20$^{\circ}$")
plt.plot(alpha, CL_10, linestyle='-', color='g', label="10$^{\circ}$")
plt.plot(alpha, CL_0, linestyle='-', color='b', label="0$^{\circ}$")
plt.xlabel('$\\alpha$ (degrees)')
plt.ylabel('$C_L$')
plt.xlim(-8.5, 12.5)
plt.title('$C_L$ vs $\\alpha$ with 1/4 span flaps ')
plt.legend()
plt.grid(True)
plt.show()
#Set Airfoil Coordinates
x_upper = x
x_lower = x
y_upper = y_upper
y_lower = y_lower
ycont = np.concatenate((y_upper[::-1], y_lower[1:n_points]))
xcont = np.concatenate((x_upper[::-1], x_lower[1:n_points]))

