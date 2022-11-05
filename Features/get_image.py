import cv2 as cv

def get_image():
    camera = cv.VideoCapture(0)
    status, frame = camera.read()
    
    if status ==True:
        return frame