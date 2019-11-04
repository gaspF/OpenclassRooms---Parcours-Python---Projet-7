import geocoder
from config import *
import re
import random
from requests import get

class Parser:
    def __init__(self, user_input):
        self.user_input = user_input

    def clean_input(self):
        stopwords = STOP_WORDS
        self.user_input = self.user_input.lower()
        self.user_input = re.sub(r"[.!,;?\']", " ", self.user_input).split()
        self.user_input = [w for w in self.user_input if w not in stopwords]
        self.user_input = " ".join(self.user_input)
        return self.user_input


class GoogleMaps:
    def __init__(self, query):
        self.query = query
        self.latitude = float
        self.longitude = float
        self.address = str

    def geoloc_coordinates(self):
        g = geocoder.google(self.query, key=GOOGLE_MAPS_API_KEY)
        data = g.json
        self.latitude = data["lat"]
        self.longitude = data["lng"]
        return self.latitude, self.longitude

    def get_geoloc_address(self, coordinates):
        g = geocoder.google(coordinates, method="reverse", key=GOOGLE_MAPS_API_KEY)
        data = g.json
        self.address = data["address"]
        return self.address


class WikiRequest:
    def __init__(self, lat, lng):
        pageid = self.get_pageid(lat, lng)
        if pageid:
            self.summary = self.get_summary(pageid)

    def get_pageid(self, lat, lng):
        lat_lng = "|".join([str(lat), str(lng)])
        parameters = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 10000,
            "gscoord": lat_lng,
            "format": "json",
        }
        response = get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()

        pageid = data["query"]["geosearch"][0]["pageid"]
        return pageid

    def get_summary(self, pageid):
        parameters = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "indexpageids": 1,
            "exsentences": "5",
            "pageids": pageid,
        }

        response = get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()
        summary = data["query"]["pages"][str(pageid)]["extract"]

        return summary


class PapyMessages:
    answers = ANSWERLIST
    end_quotes = ENDQUOTELIST

    @staticmethod
    def randomAnswer():
        quote_answer = random.choice(PapyMessages.answers)
        return quote_answer

    @staticmethod
    def randomEndQuote():
        random_quote_answer = random.choice(PapyMessages.end_quotes)
        return random_quote_answer
