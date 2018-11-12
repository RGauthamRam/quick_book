#imports
import os
from twilio.rest import Client
import time
from bs4 import BeautifulSoup
import requests

# my Twilio phone number
TWILIO_PHONE_NUMBER = ""

# list of phone numbers to dial
DIAL_NUMBERS = ["",]

#no idea what this does lol --- I guess instructions for when someone picks up the call
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

#get client from my auth token and password
key = ""
password = ""
client = Client(key, password)

def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER, url=TWIML_INSTRUCTIONS_URL, method="GET")

dial_numbers(DIAL_NUMBERS)

#loop infinitely and check every x seconds
while True:
    #url = url of webpage to be scraped (that the correct term ?)
    urlS = 'https://in.bookmyshow.com/buytickets/sarkar-chennai/movie-chen-ET00074493-MT/20181106'
    urlA = 'https://in.bookmyshow.com/buytickets/ags-cinemas-villivakkam/cinema-chen-ACVM-MT/20181104'
    #headers - request headers I think
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    #response of the url
    responseS = requests.get(urlS, headers=headers)
    responseA = requests.get(urlA, headers=headers)
    #beautiful soup module does it's magis, parse using basic html.parser because lxml was not working 
    soupS = BeautifulSoup(responseS.text, "html.parser")
    soupA = BeautifulSoup(responseA.text, "html.parser")
    #Check required conditions and call if true
    print(str(soupA).find("Tuesday, 6 Nov"))
    print(str(soupS.find(id="venuelist")).find('Villivakkam'))
    print(str(soupS.find(id="venuelist")).find('Vadapalani'))
    time.sleep(20)  #x=20 seconds
    continue


#The intent of this code is to call me when tickets are released in bookmyshow
#future improvements --- book tickets automatically based on my inputs
