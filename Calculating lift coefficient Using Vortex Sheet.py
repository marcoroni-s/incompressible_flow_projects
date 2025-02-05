import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.linalg import solve

alpha_vals = np.linspace(-5,10,40, dtype=np.intc)
Cl_vals = np.ones(alpha_vals.shape[0])
Cm_vals = np.ones(alpha_vals.shape[0])
num_panels = 2*(x_upper.shape[0]-1)-1


for i in range(alpha_vals.shape[0]):
  alpha = alpha_vals[i]
  alpha_rad = alpha/180 * np.pi;

  # coordinates of the vorticies
  xv_upper = x_upper[:-1] + 0.25 * (x_upper[1:] - x_upper[:-1])
  yv_upper = y_upper[:-1] + 0.25 * (y_upper[1:] - y_upper[:-1])
  # coordinates of the control points
  xc_upper = x_upper[:-1] + 0.75 * (x_upper[1:] - x_upper[:-1])
  yc_upper = y_upper[:-1] + 0.75 * (y_upper[1:] - y_upper[:-1])
  # coordinates of the vorticies
  xv_lower = x_lower[:-1] + 0.25 * (x_lower[1:] - x_lower[:-1])
  yv_lower = y_lower[:-1] + 0.25 * (y_lower[1:] - y_lower[:-1])
  # coordinates of the control points
  xc_lower = x_lower[:-1] + 0.75 * (x_lower[1:] - x_lower[:-1])
  yc_lower = y_lower[:-1] + 0.75 * (y_lower[1:] - y_lower[:-1])

  # make the two surfaces into one array again
  xv = np.concatenate((xv_upper[::-1], xv_lower))
  xc = np.concatenate((xc_upper[::-1], xc_lower))
  yv = np.concatenate((yv_upper[::-1], yv_lower))
  yc = np.concatenate((yc_upper[::-1], yc_lower))

  A = np.ones((num_panels, num_panels))
  B = np.ones((num_panels,1))

  for p in range(num_panels):
    for q in range(num_panels):
      dxp = xcont[p+1]-xcont[p]
      dyp = ycont[p+1]-ycont[p]
      L = np.sqrt((dxp**2)+(dyp**2))


      R = np.sqrt(((xv[q] - xc[p]) ** 2 + (yv[q] - yc[p]) ** 2))
      cos_d2pq = (xv[q] - xc[p]) / R
      sin_d2pq = (yv[q] - yc[p]) / R

      cos_thetap = dxp / L
      sin_thetap = dyp / L

      numerator = cos_d2pq*cos_thetap + sin_d2pq*sin_thetap
      denominator = 2*np.pi*R
      A[p,q] = numerator/denominator

    thetap = np.arctan2(ycont[p+1] - ycont[p], xcont[p+1] - xcont[p])

    B[p] = np.sin(thetap - alpha_rad)

  Gamma = solve(A,B)
  Cl = 2*np.sum(Gamma)
  Cl_vals[i] = Cl

plt.figure(1)
plt.plot(alpha_vals,Cl_vals,'r--', linewidth = 2,label=f'Vortex Panel Method NACA{naca_code}')
plt.plot(alpha_vals, 2*np.pi*((alpha_vals*np.pi/180) + 0.0326),label='Analytic TAT')
plt.title('Lift Coefficient as a Function of Angle of Attack')
plt.xlabel('Angle of Attack (degrees)')
plt.ylabel('Lift Coefficient')
plt.legend()
plt.grid()
plt.axhline(0,linewidth = 1, color = 'black')
plt.axvline(0,linewidth = 1, color = 'black')
plt.show()
