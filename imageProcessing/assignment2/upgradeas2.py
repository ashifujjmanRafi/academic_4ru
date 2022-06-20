import cv2
import numpy as np
import matplotlib.pyplot as plt

def condition():
    img_path ='mountain.jpeg'
    rgb = plt.imread(img_path)
    #convert to gray
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    #trashold value
    t1,t2 = 100,140
    c , p = 3 , 3
    epsilon = 1e-6
    row,col = gray.shape

    #first condition:s = 100, if r >= T1 and r <= T2; otherwise s = 10.
    condition1 = np.zeros((row,col),dtype=np.uint8)
    for x in range(row):
        for y in range(col):
            if(gray[x][y]>=t1 and gray[x][y]<=t2):
                condition1[x][y] = 100
            else:
                condition1[x][y]=10 
    
    #second condition:s = 100, if r >= T1 and r <= T2; otherwise s = r.
    condition2 = np.zeros((row,col),dtype = np.uint8)
    for x in range(row):
        for y in range(col):
            if(gray[x][y] >= t1 and gray[x][y] <= t2):
                condition2[x][y] = 100
            else:
                condition2[x][y] = gray[x][y]
    
    #third condition:s = c log(1 + r) .
    condition3 = np.zeros((row,col),dtype=np.uint8)
    condition3 = c * np.log(gray + 1)

    #fourth condition : s = c ( r + epsilon ) ^ p
    condition4 = np.zeros((row,col),dtype = np.uint8)
    condition4 = c * (epsilon + gray) ** p

    img_set = [rgb,gray,condition1,condition2,condition3,condition4]
    img_tittle = ['RGB','GRAY','FIRST CONDITION','SECOND CONDITION','THIRD CONDITION','FOURTH CONDITION']
    img_show(img_set,img_tittle)

def img_show(img_set,img_tittle):
    for i in range(len(img_set)):
        plt.subplot(2,3,i+1)
        plt.title(img_tittle[i])
        plt.imshow(img_set[i],cmap='gray')
    plt.savefig('condition.png')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    condition()

