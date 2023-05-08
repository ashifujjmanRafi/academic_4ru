import matplotlib.pyplot as plt
last_num = []
x = 11
a = 17
c = 13
m = 100
last_num.append(x)
print("seed:",x)
for i in range(10):
    x = (x*a+c)%m
    print(x)
    last_num.append(x)
plt.subplot(1,1,1)
plt.plot(last_num)
plt.show()

