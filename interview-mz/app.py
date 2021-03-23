from flask import Flask, Response, request, jsonify
import json
import pandas as pd
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Just a home page with nothing, ya nothing!'

@app.route('/data', methods=['POST'])
def data():

    # I'm asuming string values are being passed and not straight out float values
    #json_array = '{ "0": "0.1", "1":"0.9", "2":"0.123", "3":"0.99" , "4":"0.5" , "5":"1.0" , "6":"0" }'

    """ print(request.json)

    sys.exit(0) """
    json = request.json
    json_array = json.dumps(json)

    message = calculate_message(json_array)


    return message


def calculate_message(json_array):

    jl = json.loads(json_array)
    #print(jl)
    aList = []
    for v in jl.values():
        #print(v)
        aList.append(float(v))

    # setup original values in a DataFrame
    # asuming that this is already a set of values and not giving from the user
    df_o = pd.DataFrame([1,1,1,1,1,1,1])
    df_o[1] = [2,2,2,2,2,2,2]
    df_o[2] = [3,3,3,3,3,3,3]

    # given value from rest
    df = pd.DataFrame(aList)

    # lets multiple with original dataframe
    # asuming that I should multiply the the original values with the users given value to get the results
    df[0] = df[0] * df_o[0]
    df[1] = df[0] * df_o[1]
    df[2] = df[0] * df_o[2]

    # lets transpose to get/see 3x7 matrix
    df.T



    message_string1 = "Your original weekly results for the next three weeks are: <br> "
    message_string1 += df_o[0].astype(str).to_string(index=False).replace('\n',',').replace(' ','') + " <br> "
    message_string1 += df_o[1].astype(str).to_string(index=False).replace('\n',',').replace(' ','') + " <br>"
    message_string1 += df_o[2].astype(str).to_string(index=False).replace('\n',',').replace(' ','') + " <br>"
    message_string1 += "Your modified weekly results for the next three weeks are: <br> "
    message_string1 += df[0].astype(str).to_string(index=False).replace('\n',',').replace(' ','')  + " <br> "
    message_string1 += df[1].astype(str).to_string(index=False).replace('\n',',').replace(' ','')  + " <br>"
    message_string1 += df[2].astype(str).to_string(index=False).replace('\n',',').replace(' ','')  + " <br>"


    message_string1

    return message_string1