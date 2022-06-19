import random as rd
from matplotlib import pyplot as plt
import numpy as np

xb = rd.uniform(0, 1000)
yb = rd.uniform(0, 1000)

xf = rd.uniform(0, 1000)
yf = rd.uniform(0, 1000)

velocity = 20
t = 0

fighter_coordinatesX = []
fighter_coordinatesY = []
bomber_coordinatesX = []
bomber_coordinatesY = []

fighter_coordinatesX.append(xf)
fighter_coordinatesY.append(yf)
bomber_coordinatesX.append(xb)
bomber_coordinatesY.append(yb)

cought = False

while True:

    distance = np.sqrt((xb - xf)**2 + (yb - yf)**2)
    if distance <= 100:#escape
        cought = True
        break
    
    elif distance>=900:#caught by bomber
        cought = False
        break

    #calculate the angle
    sinx = (yb - yf)/distance
    cosx = (xb - xf)/distance

    t = t +1 
    xf = xf + velocity*cosx
    yf = yf + velocity*sinx

    fighter_coordinatesX.append(xf)
    fighter_coordinatesY.append(yf)

    xb = rd.uniform(0, 1000)
    yb = rd.uniform(0, 1000)

    bomber_coordinatesX.append(xb)
    bomber_coordinatesY.append(yb)


#plot the fighter and the bomber coordinates into an graph

plt.scatter(fighter_coordinatesX, fighter_coordinatesY)

plt.scatter(bomber_coordinatesX, bomber_coordinatesY)

print("The fighter is cought: ", cought)

plt.show()

print(fighter_coordinatesX,fighter_coordinatesY)

print(t)
    



