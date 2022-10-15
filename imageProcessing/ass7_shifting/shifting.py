import matplotlib.pyplot as plt
import cv2

def shifting():
	
	img_path = 'mountain.jpg'
	print(img_path)
	
	rgb = cv2.imread(img_path)
	print(rgb.shape)
	gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
	print(gray.shape)
	r,c = gray.shape

	left,right,narrow = gray.copy(),gray.copy(),gray.copy()
	#narrow band shifting
	for i in range(r):
		for j in range(c):
			if(narrow[i][j]<=100):
				narrow[i][j]=100
			elif(narrow[i][j]>=180):
				narrow[i][j]=180
	
	
	#print(right.shape)
	#left shifting
	left = left -80
	#right shifting
	right = right+50
	
	org_calchist = cv2.calcHist([gray],[0],None,[256],[0,255])
	lef_hist = cv2.calcHist([left],[0],None,[256],[0,255])
	ri_hist = cv2.calcHist([right],[0],None,[256],[0,255])
	nr_hist = cv2.calcHist([narrow],[0],None,[256],[0,255])
	
	img_set = [gray,left,right,narrow]
	img_title = ["ORIGINAL","LEFT SHIFTING","RIGHT SHIFTING","SPECIFIC SHIFTING"]
	plot_set = [org_calchist,lef_hist,ri_hist,nr_hist]
	
	for i in range(len(img_set)):
		plt.subplot(2,4,i+1)
		plt.title(img_title[i])
		plt.imshow(img_set[i],'gray')
		
	for i in range(len(plot_set)):
		plt.subplot(2,4,i+5)
		plt.plot(plot_set[i])
	plt.tight_layout()
	plt.savefig("result")
	plt.show()
	
	



if __name__ == '__main__':
	shifting()
