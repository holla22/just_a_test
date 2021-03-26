from interview_mz import __version__
import json
from calc import Calculation
import pandas as pd
import numpy as np


def test_version():
    assert __version__ == '0.1.0'

def user_value_pass():
    json_array = '{ "0": "0.1", "1":"0.9", "2":"0.123", "3":"0.99" , "4":"0.5" , "5":"1.0" , "6":"0" }'

    return json_array

# check if string is passed
def test_user_value_string():

    value = user_value_pass()

    assert type(value) == str

# check if converstion to dict is dict
def test_user_value_dict():

    value = user_value_pass()

    v = json.loads(value)

    assert type(v) == dict

# check that we have 7 values in our dictionary
def test_user_value_lenght():

    value = user_value_pass()

    v = json.loads(value)

    assert len(v) == 7

# functional test of final calculation output
def test_user_value_cacl_function():

    value = user_value_pass()

    c = Calculation(value)

    final_output_cal = c.calculate_message()

    assert type(final_output_cal) == str

# test if data out put contiains 1,1,1,1,1,1,1
def test_user_value_cacl_function_contains_one():

    value = user_value_pass()

    c = Calculation(value)

    final_output_cal = c.calculate_message()

    substring = '1,1,1,1,1,1,1'

    try:
        final_output_cal.index(substring)
    except ValueError:
        isTrue = False
    else:
        isTrue = True

    assert isTrue == True

# test if data out put contiains 2,2,2,2,2,2,2
def test_user_value_cacl_function_contains_two():

    value = user_value_pass()

    c = Calculation(value)

    final_output_cal = c.calculate_message()

    substring = '2,2,2,2,2,2,2'

    try:
        final_output_cal.index(substring)
    except ValueError:
        isTrue = False
    else:
        isTrue = True

    assert isTrue == True


# test if data out put contiains 3,3,3,3,3,3,3
def test_user_value_cacl_function_contains_three():

    value = user_value_pass()

    c = Calculation(value)

    final_output_cal = c.calculate_message()

    substring = '3,3,3,3,3,3,3'

    try:
        final_output_cal.index(substring)
    except ValueError:
        isTrue = False
    else:
        isTrue = True

    assert isTrue == True

# test if data out put contiains user input 0.1,0.9,0.123,0.99,0.5,1.0,0
def test_user_value_cacl_function_contains_same_user_value():

    value = user_value_pass()

    c = Calculation(value)

    final_output_cal = c.calculate_message()

    substring = '0.1,0.9,0.123,0.99,0.5,1.0,0'

    try:
        final_output_cal.index(substring)
    except ValueError:
        isTrue = False
    else:
        isTrue = True

    assert isTrue == True


def pandas_calculation_from_user_import_two(user_input):

    # original value
    df_o = pd.Series([2,2,2,2,2,2,2], dtype=object)
    # user value
    df_u = pd.Series(user_input, dtype=object)

    final_df_calc = df_u * df_o

    return final_df_calc

def test_calculation_two():

    user_input = [0.1,0.9,0.123,0.99,0.5,1.0,0]
    expected_value = [0.2,1.8,0.246,1.98,1.0,2.0,0]

    calc = pandas_calculation_from_user_import_two(user_input)

    assert calc.tolist() == expected_value

def pandas_calculation_from_user_import_three(user_input):

    # original value
    df_o = pd.DataFrame([3,3,3,3,3,3,3])
    # user value
    df_u = pd.DataFrame(user_input)

    final_df_calc = df_u * df_o

    return final_df_calc

def test_calculation_three():

    user_input = [0.1,0.9,0.123,0.99,0.5,1.0,0]
    expected_value = [0.3,2.7,0.369,2.97,1.5,3.0,0]

    calc = pandas_calculation_from_user_import_three(user_input)

    #calc = calc.round(decimals=0).astype(object)
    print(type(calc))
    print(calc[0].tolist())

    assert calc[0].tolist() == expected_value