import matplotlib.pyplot as plt
last_num = []
x = 27
a = 17
c = 43
m = 100
last_num.append(x)
print("seed: "+ str(x))
for i in range(10):
    x1 = (last_num[-1]*a+c)%m
    print(x1)
    last_num.append(x1)
plt.subplot(1,1,1)
plt.plot(last_num)
plt.show()

