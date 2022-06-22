import cv2
import numpy as np
import matplotlib.pyplot as plt

def salt_noise():
    """
    Adds salt noise to an image.
    """
    img_path = 'mountain.jpeg'
    rgb = cv2.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    noise = gray.copy()

    #avaraging filter
    avg_kernal = np.array([[1,1,1],[1,1,1],[1,1,1]]) / 9
    
    gaussain_kernal = np.array([[1,2,1],[2,4,2],[1,2,1]]) / 16

    avg_img = cv2.filter2D(gray, -1, avg_kernal)

    # Add salt noise to the image
    r,c = noise.shape
    t = (r*c)//50
    for i in range(t):
        x = np.random.randint(0,r)
        y = np.random.randint(0,c)
        if(i%2==0):
            noise[x,y] = 255
        else:
            noise[x,y] = 0
    #avaraging filter
    avg_noise = cv2.filter2D(noise, -1, avg_kernal)
    gaussain_noise = cv2.filter2D(noise, -1, gaussain_kernal)
    median_blur = cv2.medianBlur(noise, 3)

     # Display the images
    
    img_set = [gray, avg_img, noise, avg_noise, gaussain_noise, median_blur]
    img_tittle =['Gray','Avg_filter','Salt_noise','Avg_noise','Gaussain_noise','Median_blur']
    img_show(img_set,img_tittle)

def img_show(img_set,img_tittle):
    
    for i in range(len(img_set)):
        plt.subplot(3,2,i+1)
        plt.imshow(img_set[i],cmap='gray')
        plt.title(img_tittle[i])
    plt.tight_layout()   
    plt.savefig("A6")
    plt.show()


if __name__ == '__main__':
    salt_noise()
