#!/usr/bin/env python

import joblib
import cv2
import numpy as np
from PIL import Image
from face_recognition import preprocessing
from .util import draw_bb_on_img
from .constants import MODEL_PATH
from PIL import ImageDraw, ImageFont
from Features.csv_writer import append_data
from Features.save_snapshot import SaveImageFromArray
from Features.csv_writer import prev_time
from Features.time_checker import inactive

def get_lables(faces):
    
    for face in faces:
        text = "%s %.2f%%" % (face.top_prediction.label.upper(), face.top_prediction.confidence * 100)
        text = text.split(" ")
        return text[0], text[1].strip("%")
def build_dictionary(label, confidence):
    
    if label not in label_confidences.keys():
        label_confidences[label] = []
    label_confidences[label].append(confidence)
    #Labels create sucessfully
    
def get_prediction():
    #now, we have to get the average confidence of the labels
    final_confidence_with_labels = {}
    for person in label_confidences.keys(): 
        final_confidence_with_labels[person] = np.mean(list(map(float, label_confidences[person])))
    try:
        max_key = max(final_confidence_with_labels, key=final_confidence_with_labels.get)
        return max_key, final_confidence_with_labels[max_key]
    except Exception as e:
        print("Exception: ", e)
        
        
label_confidences = {}
def face_recongizer():
    
    cap = cv2.VideoCapture(0)
    face_recogniser = joblib.load(MODEL_PATH)
    preprocess = preprocessing.ExifOrientationNormalize()
    
    ret, frame = cap.read()
    SaveImageFromArray(frame, "logs\Face_recog_images")
    status = True
    append_data("logs\\face_recognition_data.csv","Entered","entered")
    while status ==True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        img = Image.fromarray(frame)
        faces = face_recogniser(preprocess(img))
        
        if faces is not None and len(faces) > 0:
            lable, confidence  = get_lables(faces)
            build_dictionary(lable, confidence)
            # draw_bb_on_img(faces, img)

        # Display the resulting frame
        # cv2.imshow('video', np.array(img))
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        
        status = inactive("logs\\face_recognition_data.csv", 5)
        
    
    
    cap.release()
    # cv2.destroyAllWindows()
    person, confidence = get_prediction()
    append_data("logs\\face_recognition_data.csv",person,confidence)
    return get_prediction()
    
        

    # When everything done, release the captureq
    
    



