import numpy as np

a = 100
b = 50 
c = 0
k1  = .008
k2 = .002
dt = .1
t = 0

print("Substance at time = ",round(t,2),"   a = ",round(a,2),"    b = ",round(b,2),"    c = ",round(c,2))

while(t<1):
    t += dt
    a += (k2*c - k1*a*b)*dt
    b += (k2*c - k1*a*b)*dt
    c += (k1*2*a*b - k2*2*c)*dt
    print("Substance at time = ",round(t,2),"a = ",round(a,2)," b = ",round(b,2)," c = ",round(c,2))

