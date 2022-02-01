import cv2 #pip install opencv-python
import matplotlib.pyplot as plt #pip install matplotlib

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt' #file names
frozen_model = 'frozen_inference_graph.pb'


model = cv2.dnn_DetectionModel(frozen_model,config_file) #load the model


classLabels = [] #empty list
file_name = 'labels.txt' # list of classes in coco dataset
with open(file_name,'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').rsplit('\n')
    
    
print(classLabels)
    
