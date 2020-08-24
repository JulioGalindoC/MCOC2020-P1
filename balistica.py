#                                                         #
#      Materia: Metodos Computacionales en IOC            #
#                                                         #
#      Entrega 1 proyecto 1                               #
#                                                         #
#      Alumno: Julio Andres Galindo Carazas               #
#                                                         #
#      Fecha: 24/08/2020                                  #
#                                                         #
###########################################################
#
# Integración de ecuaciones diferenciales 
#########################################
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pylab as plt
import matplotlib.pyplot as plt1

# Unidades base:
cm = 0.01   #[m]
inch = 2.54 * cm
g = 9.8     #[m/s^2]

# Coef de arrastre:
rho = 1.225
cd = 0.47   #[Kg/m^3]
D = 8.5 * inch
r = D/2
A = sp.pi * r**2
CD = 0.5 * rho * cd * A

# Masa:
m = 15.     #[Kg]

# Funcion a integrar:
# z es el vector de estado

# z = [x, y, vx, vy]
# dz/dt = bala(z,t)     dz1/dt = z2
#           [z2         ]
# dz/dt =   [           ]   (modelo)
#           [FD/m -g    ]

# Vector de estado:
# z[0] -> x
# z[1] -> y
# z[2] -> vx
# z[3] -> vy

def bala(z,t) :
    zp = sp.zeros(4)
    zp[0] = z[2]
    zp[1] = z[3]
    v = z[2:4]  #saca los ultimos 2 componentes
    
    v[0] = v[0] - V

    v2 = sp.dot(v,v)
    vnorm = sp.sqrt(v2)
    FD = - CD * v2 * (v / vnorm)
    zp[2] = FD[0] / m
    zp[3] = FD[1] / m - g

    return zp

# Vector de tiempo:
t = sp.linspace(0,30,1001)

# Parte en el origen y tiene vx = vy =2 [m/s]
vi = 100*1000/3600.
z0 = sp.array([0,0,vi,vi])

# Viento:
V = 0   #[m/s]

while V <= 20 :
    
    sol = odeint(bala, z0, t)

    x = sol[:,0]
    y = sol[:,1]

    plt.figure(1)
    plt.plot(x,y)

    V+=10

# Grafico:
plt.legend(['V=0 m/s','V=10 m/s','V=20 m/s'])
plt.title('Trayectoria para distintos vientos')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.axis([0,150,0,50])
plt.grid(True)

plt.tight_layout()

# Guardar grafico como png sin abrir una ventana de visualizacion
plt1.savefig('Trayectoria para distintos vientos')
