import numpy as np

a = [100]
b = [50]
c = [0]
dt = 0.1
t = 0
k1 = 0.008
k2 = 0.002

print("t = ", 0, " a = ", a[0], " b = ", b[0], " c = ", c[0])

for i in range(60):
    temp_a = a[-1]
    temp_b = b[-1]
    temp_c = c[-1]

    c.append(temp_c + (2*k1*temp_a*temp_b - k2*temp_c) * dt)     
    a.append(temp_a + (k2*temp_c - k1*temp_a*temp_b) * dt)
    b.append(temp_b + (k2*temp_c - k1*temp_a*temp_b) * dt)
    print("t = ", np.round(t, 2), " a = ", np.round(a[-1], 2), " b = ", np.round(b[-1], 2), " c = ", np.round(c[-1], 2))
    t += 0.1
    # c = c + (2*k1*a*b - k2*c) * t