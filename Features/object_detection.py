

"""
Objects Detection with yolo on webcam

"""
# Detecting Objects on Image with OpenCV deep learning library
# Reading RGB image
# Loading Yolo v3 Network
##Inferencing the image
# Getting Bounding Boxes
#NMR -Non Max suppression
# Drawing Bounding Boxes with Labels
# Importing needed libraries
import numpy as np
import cv2
from requests import delete

from Features.csv_writer import append_data
from Features.time_checker import inactive
import pandas as pd
from Features.save_snapshot import SaveImageFromArray
from Features.FaceRecognition import FaceRecognition
coco_names = 'YOLO\coco.names'
yolo_config = 'YOLO\yolov3.cfg'
yolo_weights = 'YOLO\yolov3.weights'




#Function 
def object_detection():
    print("Entered the Execution Function")
    try:
        with open(coco_names) as f:
        # Getting labels reading every line
        # and putting them into the list
        # __________OUR ADDITION__________________
            predictions = ['a', 'b', 'c','d']
            labels_person = ['person', 'man', 'woman ','child', 'children', 'boy', 'girl', 'lady','human', 'baby']
            append_data('logs/object_detect_data.csv', "started", "None")
            labels = [line.strip() for line in f]
    except Exception as e:
        delete(labels)
        print("Exception", e)
        print("Model loading Faild check the model files and wights.")
       
#loading config file and weights
    try:
        network = cv2.dnn.readNetFromDarknet(yolo_config, yolo_weights)
    except Exception as e:
        print("Exception", e)
    # Getting list with names of all layers from YOLO v3 network
    layers_names_all = network.getLayerNames()
    
    # Defining 'VideoCapture' object
    # and reading stream video from camera
    camera = cv2.VideoCapture(0)


    # Preparing variables for spatial dimensions of the frames
    h, w = None, None
    # Getting only output layers' names that we need from YOLO v3 algorithm
    # with function that returns indexes of layers with unconnected outputs
    layers_names_output = \
        [layers_names_all[i - 1] for i in network.getUnconnectedOutLayers()]


    # Setting minimum probability to eliminate weak predictions
    probability_minimum = 0.5

    # Setting threshold for filtering weak bounding boxes
    # with non-maximum suppression
    threshold = 0.3

    # Generating colours for representing every detected object
    # with function randint(low, high=None, size=None, dtype='l')
    colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')
    # Defining loop for catching frames
    status =True
    # while status==True:
    
    _, frame = camera.read()
    SaveImageFromArray(frame, "logs/object_detect_images")
    if w is None or h is None:
        h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                swapRB=True, crop=False)

    network.setInput(blob)  # setting blob as input to the network
    
    output_from_network = network.forward(layers_names_output)
    bounding_boxes = []
    confidences = []
    class_numbers = []

    # Going through all output layers after feed forward pass
    for result in output_from_network:
        # Going through all detections from current output layer
        for detected_objects in result:
            # Getting 80 classes' probabilities for current detected object
            scores = detected_objects[5:]
            # Getting index of the class with the maximum value of probability
            class_current = np.argmax(scores)
            # Getting value of probability for defined class
            confidence_current = scores[class_current]


            # Eliminating weak predictions with minimum probability
            if confidence_current > probability_minimum:
                
                box_current = detected_objects[0:4] * np.array([w, h, w, h])

                # Now, from YOLO data format, we can get top left corner coordinates
                # that are x_min and y_min
                x_center, y_center, box_width, box_height = box_current
                x_min = int(x_center - (box_width / 2))
                y_min = int(y_center - (box_height / 2))

                # Adding results into prepared lists
                bounding_boxes.append([x_min, y_min,
                                    int(box_width), int(box_height)])
                confidences.append(float(confidence_current))
                class_numbers.append(class_current)


    results = cv2.dnn.NMSBoxes(bounding_boxes, confidences,
                            probability_minimum, threshold)

    # Checking if there is at least one detected object
    # after non-maximum suppression
    if len(results) > 0:
        # Going through indexes of results
        for i in results.flatten():
            # Getting current bounding box coordinates,
            # its width and height
            x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
            box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]

            # Preparing colour for current bounding box
            # and converting from numpy array to list
            colour_box_current = colours[class_numbers[i]].tolist()


            cv2.rectangle(frame, (x_min, y_min),
                        (x_min + box_width, y_min + box_height),
                        colour_box_current, 2)

            # Preparing text with label and confidence for current bounding box
            text_box_current = '{}: {:.4f}'.format(labels[int(class_numbers[i])],
                                                confidences[i])
            # print(text_box_current)
            # Putting text with label and confidence on the original image
            cv2.putText(frame, text_box_current, (x_min, y_min - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, colour_box_current, 2)
            
            
            SaveImageFromArray(frame, "logs/object_detect_images")
            
            #________________Our_Additions________________________________
            if predictions[-1] != labels[int(class_numbers[i])]:
                predictions.append(labels[int(class_numbers[i])])
                append_data('logs/object_detect_data.csv',labels[int(class_numbers[i])],"None")
            #prediction = [a,b,c,d,'person', 'boottle','car','bus']
                
                if labels[int(class_numbers[i])] in labels_person:
                    print("Going for face Recognition")
                    FaceRecognition()
                print("Detected Object:", predictions[-1])
                
                
            # status = inactive("object_detect_data.csv",60)
                
        

    camera.release()
    # Destroying all opened OpenCV windows
    cv2.destroyAllWindows()

def get_object():
    try:
       data = pd.read_csv("logs/object_detect_data.csv")
       return (data.iloc[-1]['prediction'])
    except Exception as e:
        print("Exception", e)  
