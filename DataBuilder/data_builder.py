
import cv2
import os, shutil
from DataBuilder.augmentation import Augmentation

class Data_builder:
    def __init__(self, name, dir):
        self.name = name
        self.count = 0
        self.path = f"{dir}\\{self.name}\\"
    def check_file(self, file):
        if os.path.exists(file):
            print("File Exists")
            return True
        else:
            print("File Does not exist")
            return False
    def get_images(self, n):
        cap=cv2.VideoCapture(0)
        check = self.check_file(f"{self.path}")
        if check == False:  
            print(f"Creating directory for {self.name}") 
            os.mkdir(f"{self.path}")
            for _ in range(n):
                ret,test_img=cap.read()
                if not ret :
                    continue
                cv2.imwrite(f"{self.path}\\{self.name}%d.jpg" % self.count, test_img)     # save frame as JPG file
                self.count += 1
                resized_img = cv2.resize(test_img, (1000, 700))
                cv2.imshow('face detection Tutorial ',resized_img)
            cap.release()
            cv2.destroyAllWindows()
    def augment(self, n):
        Augmentation(f"{self.path}\\",f"{self.path}\\","aug",n)
    def Split(self, train_size = 0.8, ):

        images = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        images_train = []
        count = 0
        for img in images:
            if count ==  (int(len(images)*train_size)+1):
               break
            images_train.append(img)
            images.remove(img)
        images_test = images
        
        check1 = self.check_file(f"{self.path}\\Train")
        check2 = self.check_file(f"{self.path}\\Test")
        if check1&check2 == False:
            os.mkdir(f"{self.path}\\Train")
            os.mkdir(f"{self.path}\\Test")
            for img in images_train:
                old_image_path = f"{self.path}\\{img}"
                new_image_path = f"{self.path}\\Train\\"
                shutil.move(old_image_path, new_image_path)
            for img in images_test:
                old_image_path = f"{self.path}\\{img}"
                new_image_path = f"{self.path}\\Test\\"
                shutil.move(old_image_path, new_image_path)
                
                
            
            
        

# prajwal = Data_builder("Prajwal")
# prajwal.get_images()
# prajwal.augment()
# prajwal.Split()
    