import pytest
from app.Class import Parser, PapyMessages, GoogleMaps, WikiRequest
from config import *
import urllib.request

class TestParser:

    def test_parsing_lowercase(self):
        quote_to_test = Parser("Rue Général Leclerc Paris France")
        assert quote_to_test.clean_input() == "rue général leclerc paris france"

    def test_parsing_stopwords(self):
        quote_to_test_2 = Parser("Salut Papy, parle moi sans attendre si tu le veux bien de la Tour Eiffel !")
        assert quote_to_test_2.clean_input() == "salut papy attendre veux tour eiffel"


class TestPapyMessages:

    answers = ANSWERLIST
    end_quotes = ENDQUOTELIST

    def test_random_answer(self):
        random_quote_test = PapyMessages.randomAnswer()
        assert random_quote_test in PapyMessages.answers

    def test_end_quotes(self):
        end_quote_test = PapyMessages.randomEndQuote()
        assert end_quote_test in PapyMessages.end_quotes


class TestGoogleMaps:

    def test_get_coordinates(self, monkeypatch):
        query_coordinates = GoogleMaps("Arc de Triomphe")
        data = {'accuracy': 'GEOMETRIC_CENTER', 'address': 'Place Charles de Gaulle, 75008 Paris, France', 'bbox': {'northeast': [48.8751406802915, 2.296376480291502], 'southwest': [48.8724427197085, 2.293678519708498]}, 'city': 'Paris', 'confidence': 9, 'country': 'FR', 'county': 'Arrondissement de Paris', 'lat': 48.8737917, 'lng': 2.2950275, 'ok': True, 'place': 'ChIJjx37cOxv5kcRPWQuEW5ntdk', 'postal': '75008', 'quality': 'establishment', 'raw': {'address_components': [{'long_name': 'Place Charles de Gaulle', 'short_name': 'Place Charles de Gaulle', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'Île-de-France', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75008', 'short_name': '75008', 'types': ['postal_code']}], 'formatted_address': 'Place Charles de Gaulle, 75008 Paris, France', 'geometry': {'location': {'lat': 48.8737917, 'lng': 2.2950275}, 'location_type': 'GEOMETRIC_CENTER', 'viewport': {'northeast': {'lat': 48.8751406802915, 'lng': 2.296376480291502}, 'southwest': {'lat': 48.8724427197085, 'lng': 2.293678519708498}}}, 'place_id': 'ChIJjx37cOxv5kcRPWQuEW5ntdk', 'plus_code': {'compound_code': 'V7FW+G2 Paris, France', 'global_code': '8FW4V7FW+G2'}, 'types': ['establishment', 'museum', 'point_of_interest', 'tourist_attraction'], 'route': {'long_name': 'Place Charles de Gaulle', 'short_name': 'Place Charles de Gaulle'}, 'locality': {'long_name': 'Paris', 'short_name': 'Paris'}, 'political': {'long_name': 'France', 'short_name': 'FR'}, 'administrative_area_level_2': {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris'}, 'administrative_area_level_1': {'long_name': 'Île-de-France', 'short_name': 'Île-de-France'}, 'country': {'long_name': 'France', 'short_name': 'FR'}, 'postal_code': {'long_name': '75008', 'short_name': '75008'}}, 'state': 'Île-de-France', 'status': 'OK', 'street': 'Place Charles de Gaulle'}
        def mockreturn():
            return data
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert query_coordinates.geoloc_coordinates() == (data['lat'], data['lng'])

    def test_get_address(self, monkeypatch):
        query_address = GoogleMaps("48.87183779999999, 2.3422204")
        data = {'accuracy': 'ROOFTOP', 'address': '10 Boulevard Montmartre, 75009 Paris, France', 'bbox': {'northeast': [48.8731867802915, 2.343569380291502], 'southwest': [48.8704888197085, 2.340871419708498]}, 'city': 'Paris', 'confidence': 9, 'country': 'FR', 'county': 'Arrondissement de Paris', 'housenumber': '10', 'lat': 48.87183779999999, 'lng': 2.3422204, 'ok': True, 'place': 'ChIJVUrgmz5u5kcRWPSN-T8a730', 'postal': '75009', 'quality': 'establishment', 'raw': {'address_components': [{'long_name': '10', 'short_name': '10', 'types': ['street_number']}, {'long_name': 'Boulevard Montmartre', 'short_name': 'Boulevard Montmartre', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'Île-de-France', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75009', 'short_name': '75009', 'types': ['postal_code']}], 'formatted_address': '10 Boulevard Montmartre, 75009 Paris, France', 'geometry': {'location': {'lat': 48.87183779999999, 'lng': 2.3422204}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 48.8731867802915, 'lng': 2.343569380291502}, 'southwest': {'lat': 48.8704888197085, 'lng': 2.340871419708498}}}, 'place_id': 'ChIJVUrgmz5u5kcRWPSN-T8a730', 'plus_code': {'compound_code': 'V8CR+PV Paris, France', 'global_code': '8FW4V8CR+PV'}, 'types': ['establishment', 'museum', 'point_of_interest', 'tourist_attraction'], 'street_number': {'long_name': '10', 'short_name': '10'}, 'route': {'long_name': 'Boulevard Montmartre', 'short_name': 'Boulevard Montmartre'}, 'locality': {'long_name': 'Paris', 'short_name': 'Paris'}, 'political': {'long_name': 'France', 'short_name': 'FR'}, 'administrative_area_level_2': {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris'}, 'administrative_area_level_1': {'long_name': 'Île-de-France', 'short_name': 'Île-de-France'}, 'country': {'long_name': 'France', 'short_name': 'FR'}, 'postal_code': {'long_name': '75009', 'short_name': '75009'}}, 'state': 'Île-de-France', 'status': 'OK', 'street': 'Boulevard Montmartre'}
        def mockreturn():
            return data
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert query_address.get_geoloc_address("48.87183779999999, 2.3422204") == (data['address'])


class TestWikiRequest:

    def test_wikirequest(self, monkeypatch):
        get_id_page = WikiRequest(48.86510080000001, 2.2936899)
        data = get_id_page.get_pageid
        def mockreturn():
            return data
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert get_id_page.get_pageid == data

    def test_get_summary(self, monkeypatch):
        data = WikiRequest.get_summary("48.86510080000001, 2.2936899", 285863)
        def mockreturn():
            return data
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert WikiRequest.get_summary("48.86510080000001, 2.2936899", 285863) == data


