from matplotlib.pylab import *
from scipy.integrate import odeint

# datos:
m = 1   #[kg]
f = 1   #[Hz]
e = 0.2
w = 2 * pi * f
k = m * w**2
c = 2 * e * w * m

def eulerint(ocilador, f0, t, N_sub_div = 1) :
    Nt = len(t)
    Ndim = len(f0)

    vector = zeros((Nt, Ndim))
    vector[0,:] = f0[0]

    for i in range(1, Nt) :
        t_anterior = t[i-1]
        
        dt = (t[i] - t[i-1])/N_sub_div

        vector_temp = vector[i-1, :].copy()
        for j in range(N_sub_div) :
            vector_temp += dt * ocilador(vector_temp, t_anterior + j*dt)[1]
        vector[i,:] = vector_temp
        
    return vector

def ocilador(vector, t) :
    x = vector[0]
    y = vector[1]
    return [y, -(k/m)*x - (c/m) * y] 

f0 = [1., 1.]

t = linspace(0,4.,100)

sol = odeint(ocilador, f0, t)
z_odeint = sol[:,0]
#z_real = f0[0]*exp(t)

sol = eulerint(ocilador, f0, t, N_sub_div=1)
z_euler = sol[:,0]

sol = eulerint(ocilador, f0, t, N_sub_div=10)
z_euler2 = sol[:,0]

sol = eulerint(ocilador, f0, t, N_sub_div=100)
z_euler3 = sol[:,0]

plot(t,z_odeint, label="odeint", color="blue")
plot(t,z_euler, label="eulerint S = 1",color="green")
plot(t,z_euler2, label="eulerint S = 10", color="red")
plot(t,z_euler3, label="eulerint S = 100", color="orange")
#plot(t,z_real, "--",label="real", color = "black")
legend()
show()
