1. create a conda envinoment
2. activate the conda envirnoment and run the following lines.
- conda install python==3.8
- conda env create -f environment.yml
- pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl
- install the pytesseract aplication at the default location (C:\Program Files\Tesseract-OCR)
the file is given at YOLO/Tesseract... run the .exe to install the application.

Note that your setup has been done properly and I expect there wont be any errors if you proceed the recommemded steps.


----------------NEW in version 2.0------------------------

1. Repeat Functionality
2. Increased Speed
3. Fixed many bugs
4. Named it Harry(changable)
5. Added the wake-up word (disha) need to call it when she is at standby (she goes in standby every 10 secs of silence)
6. Removed the SerpAPI thing (used for auto_correct but it was taking a lot of time)
7. Make sure you use different API ids everywhere


9. - 
1. as a shortcut to the starup procedure written below i have created cmd files that help doing the same task 
2. Go to the start.py file and execute it, it should do all the required things within the terminals and after 2 mins the bot shall start.
3. If you added any intent or need to re-train rasa, run the train_rasa.py file to train rasa model






---------------------------------------------------Starting the bot----------------------------------------


Now to make your application run or talk to your bot you must do the following things:

1 . Go to your anaconda prompt and cd to the folder also activate your envirnoment
2.   rasa run -m models --endpoints endpoints.yml --credentials credentials.yml --port 5005  // Run this command
3. Now open anotheranaconda prompt and cd to the folder also activate your envirnoment
4. rasa run actions // Run this command
5. Now open another anaconda prompt and cd to the folder also activate your envirnoment
6. and run the main file. 
                python main.py // Run this command

                OR
7. Run the main.py file in your Vs Code or any other IDE.
8. You can now conversate with your bot.


--------For those who are new to rasa-----------
Rasa helps us builiding our own chatbot for mulitple usecases.
It has its own framework and we can highly customize it

brief overview of rasa framework file structure:
 1. Domain.yml - It stores the list of evrything simgle thing that you have defined, like all your intents, entities, actions, etc.
 2. nlu.yml - It stores all the Natural Languange Understanding (NLU) related information. basically it sotores all the patterns that you want to your bot to learn and understand from. 
 3. stories.md - It stores all the stories that you want to train your bot with. having mulitple storis is good but make sure you maintain the variety
 4. config.yml - It stores all the configuration related information. the actual pipline through which the model is going  to be trained. If you are new to ML or NLP. "Stay away from this file."
 5. endpoints.yml - It stores all the endpoints related information.basically it has the API keys, API link, port number or your server link id etc things. It is mostly use in the case of deploying your bot to a server.
 6. credentials.yml - It stores all the credentials to your API's or your Database ID- Passwords, etc.
 7. actions.py - It stores all the actions that you have defined.
 this is the file where you can highly customize your models.
 8. rules - If you want your bot to do a certain action whenever a certain pattern is detected. you can simply create a rule to do so. it is done in the rules.yml



 ----Understanding the File structure -------------
 1. actions - This folder lists the actions file(where we writea ll our actions ) and the init file which RASA uses to run the commands
 2. data - This folder contain the nlu, stories and rules files. There usage are as defined above.
 3. Features.yml - This if perhaps the most important folder in the project, it lists all the features that the bot can provide within their own file.
 4. logs - This folder contains all the logs that the bot generates.
 it would later be used for debugging and probably for training purpose.
 5. models - This folder contains the trained model files.
 6. on_device_vision_classifier_landmarks_classifier_asia_V1_1 - it stores the landmark detection model
 7 tests - It has some testing stories, it is a default folder given by rasa
 8. YOLO - It has the YOLO model and the tesseract application.

------------Important commands----------
rasa train  // Train the model
rasa shell --debug // Run the interactive shell
rasa run actions #needed to run on a separate terminal


----------For any more quiries refer the course or the Rasa documentation(recommended)------------------





How to add a function??
- Add a class in Actions.py
- Add action name in domain.Actions
- crate an intent for the action
- write intent name in domain.intents
- add a rule similar to the other rules in the data.rules file
- then go to the nlu file and add as much as intents as you want with the name of the intent you wrote in the domain file. 




-----------Swithcing to external commands--------------

- This time we have to make changes to the 2 files that we were not using till now:
            credentials.yml and endpoints.yml 
- Write  'rest:' in your credentials.yml file or uncomment it if it is already there, you dont need to add anything below it
- also add 
        rasa:
          url:"http://localhost:5005/api"

- in the endpoints.yml file you must be having action_endpoint field, keep it intact
- createa a python script as shown in the external_events.py file and run it in the terminal.

- Once you setup your run the following command onto a you terminal

        rasa run -m models --endpoints endpoints.yml --credentials credentials.yml --port 5005 
        
- you can add --enable-api --debug at the end for further use.


TO -DO -
1. Reading a book
2. Traveling from source to destination







