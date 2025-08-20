from math import*
import numpy as np

#------------------------------
#Calculo de insertidumbres de t
#------------------------------

#Tiempos por cada marca

TIEMPOS = [[0.72, 0.66, 0.66, 0.65, 0.82], [1.47, 1.50, 1.47, 1.50, 1.50], [2.06, 1.87, 1.94, 1.94, 2.20], [2.25, 2.28, 2.15, 2.22, 2.22], [2.59, 2.50, 2.68, 2.56, 2.56], [2.97, 2.88, 2.81, 2.90, 2.97], [3.25, 3.06, 3.25, 3.09, 3.00], [3.37, 3.38, 3.41, 3.31, 3.35], [3.44, 3.56, 3.53, 3.22, 3.47], [3.44, 3.79, 3.71, 3.75, 3.69]]
Distancias = [5.2, 17.7, 30.2, 42.7, 55.2, 67.7, 80.2, 92.7, 105.2, 117.7]
#Promendios de los tiempos por cada marca

Promedios = []

for tiempos in TIEMPOS:
    tiemposp = np.array(tiempos)
    pro = tiemposp.mean()
    Promedios = Promedios + [float("%.2f" % pro)]

print(Promedios, "Promedios")

#Clculo de la incertidumbre tipo A. 

U_A = [] 

for m in range(0, len(Promedios)):
    n = len(TIEMPOS[m])
    Sum = 0
    for t in TIEMPOS[m]:
        s = (t - Promedios[m])**2
        Sum = Sum + s
    Sum = (Sum / ((n)*(n-1)))**(1/2)
    U_A = U_A + [float("%.2f" % Sum)]



print(U_A, " Incertidumbre tipo A")

#Calculo de incertidumbre convinada para t

U_C = []            #lista de las incertidumbres combinadas de t
U_B = 0.16          #incertidumbre tipo B 

for u_A in U_A:
    u_C = (u_A**2 + U_B**2)**(1/2)
    U_C = U_C + [float("%.2f" % u_C)]

print(U_C, "Incertidumbre comvinada")

#Calculo de la incertidumbre de T

U_CT = []            #lista de las incertidumbres combinadas de T
Tiempos = []

for n in range(0, len(U_A)):
    u_CT = 2*Promedios[n]*U_C[n]
    Tiempos = Tiempos + [float("%.2f" %Promedios[n]**2)]
    U_CT = U_CT + [float("%.2f" % u_CT)]

print(U_CT, "Propagacion de incertidumbre" )
print(Tiempos, "Tiempos T")


print("---------------------------------")

#Pasando a formato TeX

for n in range(0, len(U_A)):
    print(f"{n+1} & {Distancias[n]} (0.1) cm & {Promedios[n]} ({U_C[n]}) s & {Tiempos[n]} ({U_CT[n]}) $s^2$ \\\\ \\hline")


