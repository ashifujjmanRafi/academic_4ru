import numpy as np
a = 100
b = 50
c = 0
dt = .1
t = 0
k1 = .008
k2 = .002

print("Sate of chemical reaction at ,time = ",t,"A = ",a," B= ",b," C= ",c)

while(t<.5):
    a += (k2*c - k1*a*b)*dt
    b += (k2*c - k1*a*b)*dt
    c += (k1*a*b*2 - 2*k2*c)*dt
    t += dt
    print("Sate of chemical reaction at ,time=",np.round(t,2),"A= ",np.round(a,2),"B= ",np.round(b,2),"C= ",np.round(c,2))