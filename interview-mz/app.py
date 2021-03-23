from flask import Flask, Response, request, jsonify
import json
import pandas as pd
import sys
from calc import Calculation
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Just a home page with nothing, ya nothing!'

@app.route('/data', methods=['POST'])
def data():

    # I'm asuming string values are being passed and not straight out float values
    #json_array = '{ "0": "0.1", "1":"0.9", "2":"0.123", "3":"0.99" , "4":"0.5" , "5":"1.0" , "6":"0" }'

    json_array =  str(request.json).replace("'",'"')
    
    # init class and pass json_string
    c = Calculation(json_array)
    message = c.calculate_message()

    return Response(message, 200)