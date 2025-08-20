from math import*
import numpy as np

#------------------------------
#Calculo de insertidumbres de t
#------------------------------

#Tiempos por longitud

TIEMPOS = [[20.43,20.44,20.50,20.31,20.41], [20.90,20.82,21.07,20.97,21.06], [22.72,23.09,22.65,22.63,22.50], [23.37,23.37,23.54,23.44,23.34], [24.28,24.25,24.25,24.21,24.22], [24.78,24.94,24.74,24.66,24.88], [25.35,25.40,25.12,25.25,25.38], [26.32,26.50,26.63,26.47,26.47], [26.94,27.09,27.04,27.06,26.97], [29.60,29.50,29.59,29.59,29.57]]
Longitud = [1.000,1.074,1.200,1.351,1.400,1.462,1.582,1.600,1.800,1.950]
#Promendios de los tiempos por cada marca

Tiempos = []
Promedios = []

for tiempos in TIEMPOS:
    tiempos10 = []
    for t in tiempos:
        tiempos10 = tiempos10 + [float("%.2f" % float(t/10))]
    Tiempos = Tiempos + [tiempos10]

for tiempos in Tiempos:
    tiemposp = np.array(tiempos)
    pro = tiemposp.mean()
    Promedios = Promedios + [float("%.2f" % pro)]

print(Promedios, "Promedios")
print(Longitud, "Longitudes")

#Clculo de la incertidumbre tipo A. 

U_A = [] 

for m in range(0, len(Promedios)):
    n = len(Tiempos[m])
    Sum = 0
    for t in Tiempos[m]:
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

print(U_C, "Incertidumbre combinada")

#Caluclo de la incertidumbre propagada de L

L = []
for l in Longitud:
    l_1_2 = l**(1/2)
    L = L + [float("%.3f" % l_1_2)]

print(L, "L")

U_CL = []
for l in Longitud:
    u_cL = (1/l**(1/2))*(0.001)
    U_CL = U_CL + [float("%.3f" % u_cL)]

print(U_CL, "Propagacion para L")

print("---------------------------------")

#Pasando a formato TeX

for n in range(0, len(U_A)): 
    print(f"{n+1} & {Promedios[n]} ({U_C[n]}) s & {Longitud[n]} (0.001) m & {L[n]} ({U_CL[n]})" " " "$m^{\\frac{1}{2}}$ \\\\ \hline")

