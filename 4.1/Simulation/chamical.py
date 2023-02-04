import numpy as np
dt = 0.1
a0 = 100
b0 = 50
c0 = 0
k1 = .008
k2 = .002

t = 0.0
T = 1.0
print("t = ",0,"a = ",a0,"b = ",b0,"c = ",c0)

while(t<T):
    a = a0 + (k2*c0-k1*a0*b0)*dt
    b = b0 + (k2*c0-k1*a0*b0)*dt
    c = c0 + (k1*a0*b0*2-2*k2*c0)*dt

    a0,b0,c0 = a,b,c
    t += dt
    print("t = ",np.round(t,2),"a = ",np.around(a0,2),"b = ",np.around(b0,2),"c = ",np.around(c0,2))


