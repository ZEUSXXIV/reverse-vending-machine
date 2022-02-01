import cv2 #pip install opencv-python
from tkinter import *
from tkinter import messagebox

quantity= 0    # number of bottles inserted

root = Tk()

root.geometry("1300x860")
root.title("REVERSE VENDING MACHINE")
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt' #file names  // architecture
frozen_model = 'frozen_inference_graph.pb'                   #           // model


model = cv2.dnn_DetectionModel(frozen_model,config_file) #load the model


classLabels = [] #empty list
file_name = 'labels.txt' # list of classes in coco dataset
with open(file_name,'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').rsplit('\n')
    
model.setInputSize(320,320)  # in config file specification
model.setInputScale(1/127.5) #255/2
model.setInputMean((127.5,127.5,127.5))  # mobile net takes input as [-1,1]
model.setInputSwapRB(True)

def save_image():

    cap = cv2.VideoCapture(0)

    success,img = cap.read()

    cv2.imshow('image',img)
    cv2.waitKey(1)
    cv2.imwrite('test.png',img)

    cap.release()
    cv2.destroyAllWindows()


def scan_image():
    global quantity
    global nob
    

    img = cv2.imread('test.png')
    z=0
    classIndex , confidece, bbox = model.detect(img,confThreshold= 0.5 )
    print(classIndex)
    bool = False
    for item in classIndex:
        if item==44:
            print("bottle")
            bool = True
            quantity+=1
            b2_window = c.create_window(830,400,anchor="nw",window=b2) 
                
            
            if(quantity>1):
                c.delete(nob)    # number of bottles
            
            nob=c.create_text(500,400,text="TOTAL NUMBER OF BOTTLES ENTERED:"+str(quantity),font = ("Copperplate",10),fill='black',anchor="nw")

            break
            
    if bool == False:
        messagebox.showinfo("Say Hello", "BOTTLE NOT FOUND")
            
            
def add():
    #save_image()
    scan_image()
    
def terminate():
    sys.exit()
    
# GUI 


    ##background

bg = PhotoImage(file="bg3.png",master = root)

c= Canvas(root,width=1300,height=860)
c.pack(fill="both",expand=True)
c.create_image(0,0,image = bg,anchor="nw")

    ##background>


c.create_text(650,290,text="WELCOME",font = ("Copperplate",50),fill='green')
    
b1=Button(root,command=add,bg='gray',activebackground='blue',height=3,width=10,text='ADD',font = ("Copperplate",20))
b2=Button(root,command=add,bg='gray',activebackground='blue',height=3,width=10,text='PROCEED',font = ("Copperplate",20))


b1_window = c.create_window(300,400,anchor="nw",window=b1)



root.mainloop()
