import numpy as np 
import matplotlib.pyplot as plt 

xb = np.random.randint(0,1000)
yb = np.random.randint(0,1000)
xf = np.random.randint(0,1000)
yf = np.random.randint(0,1000)

fcx = []
fcy = []
bcx = []
bcy = []

fcx.append(xf)
fcy.append(yf)
bcx.append(xb)
bcy.append(yb)

v = 20
t = 0
caught = False
while True:
    d = np.sqrt((xf-xb)**2+(yf-yb)**2)
    if(d<=100):
        caught = True
        break
    elif(d>900):
        caught = False
        #break
    
    xf += v*(xb-xf)/d
    yf += v*(yb-yf)/d

    fcx.append(xf)
    fcy.append(yf)

    xb = np.random.randint(0,1000)
    yb = np.random.randint(0,1000)

    bcx.append(xb)
    bcy.append(yb)
    t+=1

print("at time",t)
print("the bomber is caught",caught)

plt.subplot(1,1,1)
plt.plot(fcx,fcy,'gray')
plt.plot(bcx,bcy,'red')
plt.show()