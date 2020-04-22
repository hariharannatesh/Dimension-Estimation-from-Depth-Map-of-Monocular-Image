import cv2
import numpy as np 




count=0
X=[]
Y=[]

pic_num='_3_3_8'

def ROI(img,depth,X,Y):

	if(X[0]>X[1]):
		x2=X[0]
		x1=X[1]
	elif(X[1]>X[0]):
		x2=X[1]
		x1=X[0]

	else:
		x1=X[0]-3
		x2=X[0]+3



	if(Y[0]>Y[1]):
		y2=Y[0]
		y1=Y[1]
	elif(Y[1]>Y[0]):
		y2=Y[1]
		y1=Y[0]

	else:
		y1=Y[0]-3
		y2=Y[0]+3

	roi_image=img[y1:y2,x1:x2]
	roi_image_depth=depth[y1:y2,x1+5:x2+5]

	return roi_image,roi_image_depth



def draw_circle(event,x,y,flags,param):
	global count
	global X
	global Y
	global pic_num
	if event == cv2.EVENT_LBUTTONDOWN:
		count=count+1
		cv2.circle(img_resize,(x,y),2,(255,0,0),-1)
		#print("Depth intensity at [" + str(x) + "," + str(y) + "] is: " + str(img_depth_resize[y,x]))
		if(count>2):
			count=0
			target=input('Enter original dimension ')
			image_roi,img_depth_roi=ROI(img_copy,img_depth_resize,X,Y)
			X=[]
			Y=[]
			#cv2.imshow('ROI',image_roi)
			#cv2.imshow('ROI_depth',img_depth_roi)
			cv2.imwrite('/home/hariharan/Desktop/Spider/FYP/Color_dataset/color'+str(pic_num)+'_'+str(target)+'.png',image_roi)
			cv2.imwrite('/home/hariharan/Desktop/Spider/FYP/Depth_dataset/depth'+str(pic_num)+'_'+str(target)+'.png',img_depth_roi)
			#cv2.waitKey(0)
			#cv2.destroyAllWindows()
		else:
			X.append(x)
			Y.append(y)
			print(X)
			print(Y)
        






for i in range(21):

	print(i+1)
	img=cv2.imread('/home/hariharan/Desktop/Spider/FYP/Color_Raw/color'+str(pic_num)+'.png')
	img_depth=cv2.imread('/home/hariharan/Desktop/Spider/FYP/Depth_Raw/depth'+str(pic_num)+'.png')

	img_resize=cv2.resize(img,(512,424))
	img_depth_resize=cv2.resize(img_depth,(512,424))
	img_copy=cv2.resize(img,(512,424))
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',draw_circle)
	while(1):

		cv2.imshow('image',img_resize)
		#cv2.imshow('Depth',img_depth_resize)
		if cv2.waitKey(10)&0XFF==ord('q'):
			break

	cv2.destroyAllWindows()

