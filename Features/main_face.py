from DataBuilder.data_builder import Data_builder
from DataBuilder.data_builder import Augmentation


def create_training_image_folder(person, n,dir, augment = False, augment_n = 15 ):
    data_builder = Data_builder(person, dir)
    data_builder.get_images(n)
    if augment == True:
        Augmentation(f"{data_builder.path}\\",f"{data_builder.path}\\","aug",augment_n)
    print("Images Captured Sucessfully...!")
   

