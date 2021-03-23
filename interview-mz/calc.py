import json
import sys
import pandas as pd

class Calculation:
    def __init__(self, json_array):
		
        self.json_array = json_array

    def calculate_message(self):

        jl = json.loads(self.json_array)
        #print(jl)
        aList = []
        for v in jl.values():
            #print(v)
            aList.append(float(v))

        # setup original values in a DataFrame
        # asuming that this is already a set of values and not given from the user
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
        #print(df.T)


        # lets build up the view format returned
        message_string1 = "Your original weekly results for the next three weeks are: \n "
        message_string1 += df_o[0].astype(str).to_string(index=False).replace('\n',',').replace(' ','') + " \n "
        message_string1 += df_o[1].astype(str).to_string(index=False).replace('\n',',').replace(' ','') + " \n"
        message_string1 += df_o[2].astype(str).to_string(index=False).replace('\n',',').replace(' ','') + " \n"
        message_string1 += "Your modified weekly results for the next three weeks are: \n "
        message_string1 += df[0].astype(str).to_string(index=False).replace('\n',',').replace(' ','')  + " \n "
        message_string1 += df[1].astype(str).to_string(index=False).replace('\n',',').replace(' ','')  + " \n"
        message_string1 += df[2].astype(str).to_string(index=False).replace('\n',',').replace(' ','')  + " \n"


        return message_string1