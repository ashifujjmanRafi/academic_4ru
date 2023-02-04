import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    #print(rgb.shape)
    plt.subplot(2,3,1)
    plt.title('RGB')
    plt.imshow(rgb)

    #convert image into grayscale
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY) 
    plt.subplot(2,3,2)
    plt.title('GRAY')
    plt.imshow(grayscale,cmap='gray')


    
    #first condition:
    row, col = grayscale.shape
    t1,t2 = 50,120
    s = np.zeros((row, col), dtype=np.uint8)
    print(s.shape)
    for x in range(row):
        for y in range(col):
            if grayscale[x][y]>=t1 and grayscale[x][y]<=t2:
                s[x][y]=100
            else:
                s[x][y]=10
    
    plt.subplot(2,3,3)
    plt.title('FIRST CONDITION')
    plt.imshow(s,cmap='gray')

    #second condition:
    # print(grayscale)
    s1 = np.zeros((row, col), dtype=np.uint8)
    for x in range(row):
        for y in range(col):
            if grayscale[x][y]>=t1 and grayscale[x][y]<=t2:
                s1[x][y]=100
            else:
                s1[x][y]=grayscale[x][y]
    
    plt.subplot(2,3,4)
    plt.title('SECOND CONDITION')
    plt.imshow(s1, cmap='gray')   

    #third condition:
    c = 3
    p = 2
    epsilon = 1e-6
    s3 = c * np.log(1 + grayscale)
    plt.subplot(2,3,5)
    plt.title('THIRD CONDITION')
    plt.imshow(s3, cmap='gray')

    #forth condition :
    s4 = c * ((epsilon + grayscale) ** p)
    plt.subplot(2,3,6)
    plt.title('FOURTH CONDITION')
    plt.imshow(s4, cmap='gray')
    plt.savefig("result")
    plt.show()

if __name__ == '__main__':
    main()
