import cv2
import numpy as np 
import matplotlib.pyplot as plt

def showingDifferntColorChannels():
    img_path = 'mountain.jpeg'

    rgb  = plt.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    _,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    red = rgb[:,:,0]
    green = rgb[:,:,1]
    blue = rgb[:,:,2]

    img_show = [rgb, gray,binary,red,green,blue]
    img_title = ['RGB', 'Gray', 'Binary','Red','Green','Blue']

    im_show(img_show, img_title)

#showing the output image
def im_show(img_show,img_title):
    plt.figure(figsize  = (30, 30))
    for i in range(len(img_show)):
        plt.subplot(3,2,i+1)
        plt.title(img_title[i])
        plt.imshow(img_show[i],cmap='gray')
    plt.tight_layout()
    plt.show()


def histogramOfImage():
    img_path =  'mountain.jpeg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    r = cv2.calcHist([rgb],[0],None,[256],[0,256])
    g = cv2.calcHist([rgb],[1],None,[256],[0,256])
    b = cv2.calcHist([rgb],[2],None,[256],[0,256])
    gr = cv2.calcHist([gray],[0],None,[256],[0,256])
    img_show = [r,g,b,gr]
    img_title = ['Red','Green','Blue','Grayscale']
    im_plot(img_show,img_title)
#plotting the histogram of image
def im_plot(img_show,img_title):
    plt.figure(figsize = (30,30))
    for i in range(len(img_show)):
        plt.subplot(2,2,i+1)
        plt.title(img_title[i])
        plt.plot(img_show[i])
    plt.tight_layout()
    plt.show()
    

if __name__ == "__main__":
   showingDifferntColorChannels()
   histogramOfImage()