import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as npl
import scipy
from scipy.optimize import minimize

nTw, nRr, nRw = (15, 15, 15)
lb = [0.02, 0.06, 0.02]
ub = [0.06, 0.15, 0.08]
Tw = [0.022, 0.023, 0.0589, 0.0508, 0.0415, 0.0388, 0.0313, 0.0291, 0.0362, 0.0347, 0.0542, 0.0485, 0.0459, 0.0265, 0.0572]
Rr = [0.1196, 0.131, 0.1083, 0.1451, 0.1397, 0.0842, 0.102, 0.122, 0.0951, 0.1322, 0.0809, 0.0716, 0.0641, 0.0726, 0.097]
Rw = [0.0579, 0.0828, 0.0759, 0.0479, 0.0544, 0.0544, 0.0363, 0.0519, 0.0418, 0.0519, 0.0294, 0.0381, 0.042, 0.0266, 0.0426]

Temps_moyen = [4.87, 4.18, 3.14, 5.3, 5.00, 4.18, 5.5, 5.29, 4.75, 4.78, 4.13, 3.64, 3.22, 4.66, 4.30]
CD_moyen = [0.08012919148, 0.06630208165, 0.04913384757, 0.06599040388, 0.06631149562, 0.1018017543, 0.1022190386, 0.08650383828, 0.09276836241, 0.06315635805, 0.08254333051, 0.08664480866, 0.08509906233, 0.1129097545, 0.1024622672]

A = np.zeros((15,7))
Y_temps = np.zeros((15,1))
Y_CD  = np.zeros((15,1))

for i in range(15):
    A[i, 0] = 1
    A[i, 1] = Tw[i]
    A[i, 2] = Rr[i]
    A[i, 3] = Rw[i]
    A[i, 4] = Tw[i]*Rr[i]
    A[i, 5] = Tw[i]*Rw[i]
    A[i, 6] = Rw[i]*Rr[i]
    Y_temps[i, 0] = Temps_moyen[i]
    Y_CD[i, 0] = CD_moyen[i]



beta_CD = npl.solve(np.dot(A.transpose(),A), np.dot(A.transpose(),Y_CD))


def meta_model_temps(x, y, z):
    beta = npl.solve(np.dot(A.transpose(),A), np.dot(A.transpose(),Y_temps))
    return beta[0] + beta[1]*x + beta[2]*y + beta[3]*z + beta[4]*x*y + beta[5]*x*z + beta[6]*y*z

def objfun_temps(params):
    a, b, c = params
    return -meta_model_temps(a, b, c)

x0 = [0.0412, 0.0754, 0.0395]
bornes = ((0.02 , 0.045),(0.06 , 0.14),(0.045 , 0.085))
metamodel_temps = minimize(objfun_temps, x0, bounds = bornes)



def meta_model_CD(x, y, z):
    beta = npl.solve(np.dot(A.transpose(),A), np.dot(A.transpose(),Y_CD))
    return beta[0] + beta[1]*x + beta[2]*y + beta[3]*z + beta[4]*x*y + beta[5]*x*z + beta[6]*y*z

def objfun_CD(params):
    a, b, c = params
    return -meta_model_CD(a, b, c)

metamodel_CD = minimize(objfun_CD, x0, bounds = bornes)


print(metamodel_temps.x , metamodel_CD.x)
