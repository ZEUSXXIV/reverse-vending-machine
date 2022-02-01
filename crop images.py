import cv2 #pip install opencv-python
from tkinter import *
from tkinter import messagebox
import matplotlib
from matplotlib import pyplot as plt
import os
import shutil
count= 0    # number of bottles inserted

root = Tk()

root.geometry("1300x860")
root.title("REVERSE VENDING MACHINE")
config_file = './ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt' #file names  // architecture
frozen_model = './frozen_inference_graph.pb'                   #           // model


model = cv2.dnn_DetectionModel(frozen_model,config_file) #load the model


classLabels = [] #empty list
file_name = 'labels.txt' # list of classes in coco dataset
with open(file_name,'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').rsplit('\n')
    
model.setInputSize(320,320)  # in config file specification
model.setInputScale(1/127.5) #255/2
model.setInputMean((127.5,127.5,127.5))  # mobile net takes input as [-1,1]
model.setInputSwapRB(True)


count = 0

def scan_image(img_path):

    img = cv2.imread(img_path)
    #
    
    plt.imshow(img)
    print(img.shape)
    
    
    #
    z=0
    classIndex , confidece, bbox = model.detect(img,confThreshold= 0.5 )
    print(classIndex)
    for item in classIndex:
        if item==44:
            print("bottle")
            #break
            
            #cv2.rectangle(img,bbox,(255,0,0),2)
            
            plt.imshow(img)
            x = (bbox[0][0])     # gets coordinates of the bottles to crop the image
            y = (bbox[0][1])
            w = (bbox[0][2])
            h = (bbox[0][3])
            #bb
            print(bbox)
            cropped_img = img[y:y+h, x:x+w]       # crops the image

            plt.imshow(cropped_img)
            
            return cropped_img
        else:
            return img
    return img;

#scan_image() 

 
####  saving

img_dir = []

path_data = "./dataset/"
path_cropped = "./dataset/cropped/"

for entry in os.scandir(path_data):
    if entry.is_dir():
        img_dir.append(entry.path)
        print(entry.path)

if os.path.exists(path_cropped):
    shutil.rmtree(path_cropped)
os.mkdir(path_cropped)




cropped_img_dir = []

for im in img_dir:
    bottle_name = im.split('/')[-1]
    print(bottle_name)
    
    
    for entry in os.scandir(im):
        if not (bottle_name == "cropped"):
            img = scan_image(entry.path)
            cropped_folder = path_cropped + bottle_name
            if not os.path.exists(cropped_folder):
                os.mkdir(cropped_folder)
                print(cropped_folder)
            if img is not None:
                cropped_file_name = bottle_name + str(count) + ".png"
                cropped_path_name = cropped_folder + '/' + cropped_file_name
                count+=1
                cv2.imwrite(cropped_path_name , img)
                print("successful")            
            
    
