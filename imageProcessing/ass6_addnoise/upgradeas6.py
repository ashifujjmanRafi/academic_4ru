import cv2
import matplotlib.pyplot as plt
import numpy as np

def salt_noise():

    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    #filters
    avarage_kernal = np.ones((3,3))/9
    gaussain_kernal = np.array([[1,2,1],[2,4,2],[1,2,1]])/16

    #making noise image
    salt = gray.copy()
    r,c = gray.shape
    t = (r*c) // 50
    for i in range(t):
        x = np.random.randint(0,r)
        y = np.random.randint(0,c)
        if(i % 2==0):
            salt[x][y] = 255
        else:
            salt[x][y] = 0

    #filtered image :
    avg_gray = cv2.filter2D(gray,-1,avarage_kernal)
    avarage_salt = cv2.filter2D(salt,-1,avarage_kernal)
    gaussain_salt = cv2.filter2D(salt,-1,gaussain_kernal)
    median_salt = cv2.medianBlur(salt,3)


    #image show :
    img_set = [gray,avg_gray,salt,avarage_salt,gaussain_salt,median_salt]
    img_tittle = ['Gray','Avg_filter','Salt_noise','Avg_noise','Gaussain_noise','Median_blur']

    for i in range(len(img_set)):
        plt.subplot(3,2,i+1)
        plt.title(img_tittle[i])
        
        plt.imshow(img_set[i],'gray')
    plt.savefig("upgrade assignment6")
    plt.tight_layout()
    plt.show()
     

if __name__ == '__main__':
    salt_noise()
