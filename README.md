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


    
