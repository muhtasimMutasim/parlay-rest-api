
"""

    This is the main file that is being sent requests.
        
"""



import sys
import os
from fastapi import FastAPI, APIRouter, Request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


from deep_translator import (GoogleTranslator, MicrosoftTranslator,
                             PonsTranslator, LingueeTranslator,
                             MyMemoryTranslator, batch_detection)
app = FastAPI()
# router = APIRouter()


# @router.get("/test")
@app.get("/test")
def test():
    return {"Test": "Test for API"}



def vader_analyze( text ):
    """
        Function is to analyze a piece of text
        and return a polarity score.
    """
    data = text.split("\n")
    
    # analyzer creates Vader object and then
    # analyzer.polarity_scores( text ) returns dictionary of scores
    analyzer = SentimentIntensityAnalyzer()
        
    # Lambda function to create a dictionary and add the polarity scores
    # along with the "line" key
    merge_dict = lambda xkey, yval: {"line": xkey, **yval }
    
    # map function iterated thorough request data that was split on new lines.
    # lambda function inside map helped merge the data sets and list function converted to list.
    result = list(map( lambda line : merge_dict( line, analyzer.polarity_scores(line) ), data ))
    
    # print( f"\n\nInside Vader Analyze Function: \n{result}\n\n" )
    
    return result
    
    


def language_analyze( input_language, output_language, data ):
    """
        Function is to analyze a piece of text.
        Convert input text langauge to desired
        output text language.
    """
    # Automatically detects the langauge 
    gt = GoogleTranslator(source='auto', target=output_language)
    
    # check if language is supported
    supported_languages = gt.supported_languages
    if input_language in supported_languages and output_language in supported_languages:
        print( f"YES {input_language} & {output_language}is supported." )
    else:
        return False
    
    # translate text
    translated_txt = gt.translate(text=data)

       
    print( f"\n\n\nTRANSLATION language_analyze:\n {translated_txt}\n\n" )
    return translated_txt
    
    



# @router.get("/vader/{data}")
@app.post("/vader-non-english/{input_language}/{output_language}/{data}")
def translated_sentiment(data: str, input_language: str, output_language: str, request: Request):
    
    """
    Route to vader analysis for non-english sentiment analysis. returns a translated english sentiment analysis.
    
    """
    
    # Automatically detects the langauge 
    gt = GoogleTranslator(source='auto', target=output_language)
    
    # check if language is supported
    supported_languages = gt.supported_languages
    if input_language in supported_languages and output_language in supported_languages:
        print( f"YES {input_language} & {output_language}is supported." )
    else:
        resp = f"The Language(s) is not supported, please try again with different language."
        return {"input Language": input_language, "output language": output_language, "data": resp}

    # Translates and returns text
    translated_txt = gt.translate(text=data)
    print( f"\n\n\nTRANSLATION translated_sentiment:\n {translated_txt}\n\n" )
    sentiment_analysis = vader_analyze( translated_txt )
    return {"input Language": input_language, "output language": output_language, "data": sentiment_analysis }




# @router.get("/vader/{data}")
@app.post("/vader/{data}")
def query(data: str, request: Request):
    """
    Route to vader analysis.
    """
    # print(f"\n\nRESPONSE: {data}\n\n")
    # return {"client_host": client_host, "response": a}
    
    sentiment_analysis = vader_analyze( data )
    
    # return { "data": vader_result }
    return { "data": sentiment_analysis }





# @router.get("/translate/{input_language}/{output_language}/{data}")
@app.post("/translate/{input_language}/{output_language}/{data}")
def translate(data: str, input_language: str, output_language: str, request: Request):
    
    client_host = request.client.host
    
    resp = language_analyze( input_language, output_language, data )
    
    if resp == False:
        # If desired language is not supported then 
        resp = f"The Language(s) is not supported, please try again with different language."
        print(f"\n\n{resp}\n\n")
        return {"input Language": input_language, "output language": output_language, "data": resp}
        
    
    # return { "translation",  response}
    return {"input Language": input_language, "output language": output_language, "data": resp}
