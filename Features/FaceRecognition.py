from Features.speak import speak
from inference.video_classifier import face_recongizer
from Features.main_face import create_training_image_folder
from deepface import DeepFace
from Features.get_image import get_image
from Features.csv_writer import append_data
import os
import shutil

def verify_face():
    print("Verifying Face")
    if len(os.listdir("Verification Buffer")) > 0:
        for folder in  os.listdir("Verification Buffer"):
            print("Verifying: ", folder)
            if len(os.listdir(os.path.join("Verification Buffer", folder))) > 0:
                images = os.listdir(os.path.join("Verification Buffer", folder))
                print("Images: ", images)
                result = DeepFace.verify(get_image(), 
                                        f"Verification Buffer\\{folder}\\{images[0]}",
                                        model_name = 'Facenet512',
                                        distance_metric = 'cosine', 
                                        enforce_detection = False,
                                        detector_backend = 'mtcnn',
                                        normalization = 'Facenet512')
                print("Result: ", result)
                if result['verified']:
                    return result, folder
            else:
                print("No images in folder: ", folder)
                return False, False
    else:
        print("No images to verify")
        return False, False
           
 
def train_new_face():
    speak("Please provide a name")
    name = input('Enter your name \n')
    name_final = name.replace(" ", "_")
    create_training_image_folder(name_final, 10, "Verification Buffer")
    
    if len(os.listdir("Verification Buffer")) > 10:
        #take all data from Verification Buffer and move it to Training Buffer and train
        for i in os.listdir("Verification Buffer"):
            shutil.move(os.path.join("Verification Buffer", i), "images")
        print("Verification Buffer Moved to training buffer")
        os.system('start cmd /k start\\face_training.cmd')
    #Training the new images(will look for time constraints)
  
    return name

def FaceRecognition():
    result, folder = verify_face()
    if result != False:
         speak(folder)
    else:
        try:
            person, confidence =  face_recongizer()
            print("Person: ", person)
            print("Confidence: ", confidence)
        except Exception as e:
            person = "unkwnown"
            confidence = 0
            print("Exception: ", e)
        try:
            if int(confidence) > 50:
                if person == 'OTHERS':
                    speak('You seem new to me')
                    speak('Do you want to save your face?')
                    user_choice = input('say "YES" or "NO"\n')
                    if user_choice.lower() == 'yes':
                        try:
                            train_new_face()
                            speak( f'Thankyou {name}')
                        except Exception as e:
                            print('Exception: ', e)
                else:
                    speak(person)
            elif int(confidence) < 50 and int(confidence) > 25:
                if person == 'OTHERS':
                    speak('You seem new to me')
                    speak('Do you want to save your face?')
                    user_choice = input('say "YES" or "NO" \n')
                    if user_choice.lower() == 'yes':
                        name =  train_new_face()
                        speak(f'Thankyou {name.lower().capitalize()}')
                else:
                    speak('You look similar to ' + person.lower().capitalize() + ' Though I am not much sure')
                    speak("lend me a minute so i can verify your identity")
                    person = person.lower() 
                    person = person.capitalize()
                    result = DeepFace.verify(get_image(), 
                                            os.listdir("images/" + person)[0],
                                            model_name = 'Facenet512',
                                            distance_metric = 'cosine', 
                                            enforce_detection = False,
                                            detector_backend = 'mtcnn',
                                            normalization = 'Facenet512' )
                    if result['verify']:
                        speak(f'Thankyou {person}')
                    else:
                        speak('Sorry I am not sure')
                        speak('Do you want to save your face?')
                        user_choice = input('say "YES" or "NO" \n')
                        if user_choice.lower() == 'yes':
                            name =  train_new_face()
                            speak(f'Thankyou {name.lower().capitalize()}')
                        else:
                            speak('Thankyou very much')
                        
                
            else:
                ('Unable to detect faces clearly')
        except Exception as e:
            print("Exception: ", e)
def FaceRecognitionWOSpeak():
    
    result, folder = verify_face()
    if result != False:
        return [str(folder),result['distance']] 
      
    try:
        person, confidence =  face_recongizer()
        print("Person: ", person)
        print("Confidence: ", confidence)
    except Exception as e:
        person = "unkwnown"
        confidence = "0"
        print("Exception: ", e)
    try:
        if int(confidence) > 25:
            if person == 'OTHERS':
                speak('You seem new to me')
                speak('Do you want to save your face?')
                user_choice = input('say "YES" or "NO"\n')
                if user_choice.lower() == 'yes':
                    try:
                        name = train_new_face()
                        speak( f'Thankyou {name}')
                        return [str(name),'new entry']
                    except Exception as e:
                        print('Exception: ', e)
            else:
                return [person, confidence]
        else:
            return ['Unknown',0]
                    
    except Exception as e:
        print("Exception: ", e)