##Data augmentation using python and keras
from keras_preprocessing.image import ImageDataGenerator, img_to_array, load_img
import os

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode= 'nearest'
)
def Augmentation(directory, save_to, save_as,n_augments):
   for imgname in os.listdir(directory):
        img_path  = str(f"{directory}\\{imgname}")
        print(img_path)
        img = load_img(img_path)
        x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
        x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

        # the .flow() command below generates batches of randomly transformed images
        # and saves the results to the `preview/` directory
        i = 0
        print("Augmenting....it may take around 2 to 3 minutes")
        for batch in datagen.flow(x, batch_size=1,
                                save_to_dir=save_to, save_prefix=f"{imgname}_{save_as}", save_format='jpeg'):
            i += 1
            if i > n_augments:
                # print(f"Augmentation Complete! Check your {save_to} directory")
                break  # otherwise the generator would loop indefinitely
   print("Augmentation done for all images!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
