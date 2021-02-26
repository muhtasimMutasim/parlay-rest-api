#!/usr/bin/env python

"""
This script was created to test the REST API.

This script also allows text to be translated with
functionality that aut detects the language being
pushed through the

"""

import requests
import pathlib
import re
import sys

# Path of current directory script is located in
script_dir = pathlib.Path(__file__).parent.absolute()




def send_data( end_point, message ):

    ip = sys.argv[1]
    port = sys.argv[2]
    url = f"http://{ip}:{port}/"
    url = url + end_point + "/"+ message
    print( f"\n\nTarget Url + Endpoint:\n{url}\n\n" )

    r = requests.post(url)
    json_data = r.json()
    resp_text = r.text

    return json_data


def test():

    """
        Inital test function to confirm if API is alive and running
    """
    ip = sys.argv[1]
    port = sys.argv[2]
    url = f"http://{ip}:{port}/test"

    print( f"\n\nSending request to url {url} for testing API\n\n\n" )
    r = requests.get(url)
    # data = r.json()
    resp_text = r.text
    print( f"\nTest 1)  Update response:\n{resp_text} " )


def file_data(file_path):

    """
    Function Reads in data for a target IP address.
    """
    with open(file_path) as f:
        
        read_data = f.read()
        # print(read_data)
        
        return read_data


def lyric_translation():


    """
        This function sends spanish song lyrics to REST API
        for text translation.
    """
    data_path = f"{script_dir}/data/song_lyrics"
    data = file_data(data_path)
    # Cleans data and takes out the parathesis and words in parathensis
    data = re.sub("[\(\[].*?[\)\]]", "", data)
    # data = data.split("\n")

    endpoint = "translate"
    in_lang = "spanish"
    out_lang = "english"
    ep = f"{endpoint}/{in_lang}/{out_lang}"

    return send_data( ep, data )


def vader_response( data ):
    
    """
        Vader Test Function.
    """
    endpoint = "vader"
    return send_data( endpoint, data )


def vader_non_english_response( data ):
    
    """
        Vader Test Function to test non-english text.
    """

    ip = sys.argv[1]
    port = sys.argv[2]
    endpoint = "vader-non-english/" + "spanish/english/" + data
    url = f"http://{ip}:{port}/" + endpoint
    
    print( f"\n\nSending request to url {url} for testing API\n\n\n" )
    r = requests.post(url)
    json_data = r.json()
    return json_data




def test_translator():

    """
    test case for testing out lyric translator
    and vader sentiment analysis
    """

    # Taking spanish song and translating to english
    resp_json = lyric_translation()
    print(f"\n\n\n\n\n Lyric Translation JSON: \n{resp_json}")
    data = resp_json['data']
    print(resp_json)

    # Sending Vader a request to analyze translation
    vader_resp = vader_response( data )
    print(f"\n\n\n\n\nRESP: \n{vader_resp}")
    vader_resp = vader_resp['data']

    # print(vader_resp)
    for i in vader_resp:
        print( i )



def test_non_english():

    song = file_data( f"{script_dir}/data/song_lyrics" )
    non_english_data = vader_non_english_response(song)

    a = "----------------NON ENGLISH RESPONSE-------------------"
    print( f"\n\n{a}\n{non_english_data}\n{a}\n\n" )



def custom_message():
    
    """
        Function sends custom messages to vader
    """

    ip = sys.argv[1]
    port = sys.argv[2]
    custom_message = sys.argv[3]
    print("\n\nInside custom function")
    json_data = None


    endpoint = "vader/"
    url = f"http://{ip}:{port}/"
    print( f"\n\nSending request to url {url} for testing API\n\n\n" )
    
    if custom_message != "":
        

        endpoint = endpoint + custom_message
        print( f"\n\n ------URL: {url + endpoint}\n\n")
        r = requests.post( url  + endpoint )
        json_data = r.json()
        print( f"\n\n ------{json_data}\n\n")
        data = json_data['data'][0]
        a = f"\n\nText: {data['line']}\n"
        a += f"Negative: {data['neg']}\n"
        a += f"Neutral: {data['neu']}\n"
        a += f"Positive: {data['pos']}\n"
        a += f"Compound: {data['compound']}\n\n"
        print( f"\n{a}\n")
        return json_data
    
    alt_message = "The product really sucked!"
    endpoint = endpoint + alt_message
    print( f"\n\n ------URL: {url + endpoint}\n\n")

    r = requests.post( url  + endpoint )
    json_data = r.json()
    print( f"\n\n ------{json_data}\n\n")
    data = json_data['data'][0]
    a = f"\n\nText: {data['line']}\n"
    a += f"Negative: {data['neg']}\n"
    a += f"Neutral: {data['neu']}\n"
    a += f"Positive: {data['pos']}\n"
    a += f"Compound: {data['compound']}\n\n"
    print( f"\n{a}\n")
    
    print("Custom request is not working.")
    return json_data




def main():

    """
        Main function runs an initial test to see if API Is alive and working.
        Then sends send API song lyrics to translate. 
        Then uses the song translated to english which is processed through vader
        which returns polarity scores. 
    """
    test()
    test_translator()
    test_non_english()
    
    custom_message()

if __name__ == "__main__":
	main()
