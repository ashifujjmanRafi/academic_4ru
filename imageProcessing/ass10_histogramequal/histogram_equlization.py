
import matplotlib.pyplot as plt
import cv2

def main():
    img_path = "mountain.jpeg"
    rgb = plt.imread(img_path)


    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY) 
    equ = cv2.equalizeHist(gray)

    #histogram
    img1 = cv2.calcHist([gray],[0],None,[256],[0,256])
    img2 = cv2.calcHist([equ],[0],None,[256],[0,256])

    img_set =[gray,equ,img1,img2]
    img_title =["Gray_img","Equlized_img","Gray_histogram","Equlized_histogram"]

    for i in range(len(img_set)):
        plt.subplot(2,2,i+1)
        plt.title(img_title[i])
        if(img_set[i].shape[1]==1):
            plt.plot(img_set[i],'r')
        else:
            plt.imshow(img_set[i],'gray')

    plt.tight_layout()
    plt.savefig('result')
    plt.show()
if __name__ == '__main__':
    main()