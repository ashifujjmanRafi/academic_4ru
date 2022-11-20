import cv2
import matplotlib.pyplot as plt
import numpy as np

def filterd_img():
    img_path = 'mountain.jpeg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    
    #horizontal filter
    hor = np.array([[2,10,2],[0,0,0],[-2,-10,-2]])
    #vertical filter
    ver = np.array([[-2,0,2],[-10,0,10],[-2,0,2]])
    #sharpen filter
    sharpen = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    #edge filter
    edge = np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])
    #avarage filter
    box = np.ones((3,3))/9
   
    #img after filter operation
    img1 = cv2.filter2D(gray,-1,hor)
    img2 = cv2.filter2D(gray,-1,ver)
    img3 = cv2.filter2D(gray,-1,sharpen)
    img4 = cv2.filter2D(gray,-1,edge)
    img5 = cv2.filter2D(gray,-1,box)

    #show the image
    img_set = [gray,img1,img2,img3,img4,img5]
    img_tittle = ['GRAY','HORIZONTAL_OP','VERTEX_OP','SHARPEN_OP','EDGE_OP','BLUR_OP']
    for i in range(len(img_set)):
        plt.subplot(2,3,i+1)
        plt.title(img_tittle[i])
        plt.imshow(img_set[i],cmap='gray')
    plt.savefig('result after convulation')
    plt.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    filterd_img()