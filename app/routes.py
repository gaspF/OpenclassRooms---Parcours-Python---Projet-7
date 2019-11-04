from app import app
from flask import render_template, request
from app.Class import Parser, GoogleMaps, PapyMessages, WikiRequest
import json


@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html', title='A propos')

@app.route('/_response', methods=['GET'])
def response():
    userText = request.args.get('text')
    sentence = Parser(userText)
    message_final = sentence.clean_input()
    print(message_final)

    query = GoogleMaps(message_final)
    coordinatesgps = query.geoloc_coordinates()
    lat = coordinatesgps[0]
    lng = coordinatesgps[1] #passer en float ou faire la conversion JS
    coordinates = str(lat) + ", " + str(lng)
    address = query.get_geoloc_address(coordinates)
    recherche = WikiRequest(lat, lng)
    message_wiki = recherche.summary
    open_quote = PapyMessages.randomAnswer()
    end_quote = PapyMessages.randomEndQuote()

    return json.dumps({'userText': userText, 'message_wiki': message_wiki, 'lat': lat, 'lng': lng, 'address': address, 'open_quote': open_quote, 'end_quote': end_quote})



