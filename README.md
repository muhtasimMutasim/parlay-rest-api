# Parlay rest

    The purpose of this project is to create a REST api using FastAPI that has the ability to 
    
    translate text with auto language detection and then use a natural language processing tool
    
    called vaderSentiment that analyze the text and returns polarity scores. 

    -------------------------------------------------------------------------------------------

    This project was deployed on Google Cloud Platform. It incorporates technology such as:
            - docker-machine
            - docker
            - dockerhub & gcp
            - python's FastAPI
            - python module Deep Translator (text translation): https://github.com/nidhaloff/deep-translator
            - python module vaderSentiment (text sentiment analysis):  https://github.com/cjhutto/vaderSentiment



# Run the /parlay-rest/app/main.py locally on computer.

        # Make sure you're in the parlay-rest directory where the requirements.txt is.
        run "pip install -r requirements.txt"

        # After the installs are complete.
        run:
                uvicorn main:app --host {insert ip address} --port {desired port number} --reload
               Ex: 
                uvicorn main:app --host 0.0.0.0 --port 5057 --reload


# Run on Container on Mac

        # This command is for creating a new docker-machine if on OSX
        docker-machine create --driver virtualbox {insert machine name}
        Ex: docker-machine create --driver virtualbox test

        # Starts desired machine 
        docker-machine start  {insert machine name}  
        Ex: docker-machine start test  

        # push to docker hub for gcp
        docker build -t {username}/parlay-rest:latest .
        
        #Before you push it to dockerhub run it locally. Run Tests.
        docker run --name {username}/parlay-rest:latest -p5057:5057 --rm {username}/parlay-rest:latest

        # To make updates to this code and push them to gcp:
        docker push {username}/parlay-rest:latest




# Endpoints

    /test
        - Purpose is to check if the application is alive.

    /vader/{data}
            - Purpose is to recieve text, which it then processes and returns with a polarity score.
    
    /translate/{input_language}/{output_language}/{data}
            - Purpose is to translate language text is wriiten in to output or desired language.
    
    /vader-non-english/{input_language}/{output_language}/{data}
            - Purpose is to use vader with non-english based languages and have it return with a polarity scores after translating the initial non-english based text to english.
    
    
   # test

        In the test directory there is a python script called "test.py" that has functions that and test cases to check if everything on the REST api is 
        working and returning properly.


        usage example:

            cd tests
            python test.py {Ip address} {Port Number}
            python test.py 0.0.0.0 5050

         usage of custom_mesaage():

            python test.py {Ip address} {Port Number} "Insert desired message you want to send"

            python test.py 0.0.0.0 5050 "This movie is not very good."


    
