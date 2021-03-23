# Assesment Project

Assessment:

Create a web app with the backend written in Python's Flask Framework. This backend only needs to expose an API (i.e. you don't have to build an accompanying front-end for it, we can just make use of curl commands for that).

As for Python make use of version 3.8 and select your build tool of choice (at Ramp we use 'poetry' so that's a preferable choice for us).

Requirements:
* The API should expose a RESTful endpoint that accepts a list of 7 comma-separated decimal values between and including 0 to1 (representing the 7 days of the week). E.g. 0.1,0.9,0.123,0.99,0.5,1.0,0
* Upon receiving a request the backend should respond with a calculated message like:

Your original weekly results for the next three weeks are:
1,1,1,1,1,1,1
2,2,2,2,2,2,2
3,3,3,3,3,3,3
Your modified weekly results for the next three weeks are:
0.1,0.9,0.123,0.99,0.5,1.0,0
0.2,1.8,0.246,1.98,1.0,2.0,0
0.3,2.7,0.369,2.97,1.5,3.0,0    

* In order to create this message, the backend should create a 3*7 Pandas dataframe (which contains the 'original' values as per above) and then copy and modify these values by multiplying them with the list of comma separated values to get the desired modified resultset (again, as per the example above).

Commit a git project to your repository of choice (include all your instructions, assumptions and judgement calls made in the project's README.md).

# Instructions

- git clone this repository
- cd into interview-mz directory
- run "poetry shell" to init virtual environment (assuming you have poetry installed)
- run "poetry install"
- run the bash script "get_up_and_running.sh", this will start flask in dev mode
- POST data to the following URL: http://127.0.0.1:5000/data

### Curl Commands

```
curl --location --request POST 'http://127.0.0.1:5000/data' \
--header 'Content-Type: application/json' \
--data-raw '{ "0": "0.1", "1":"0.9", "2":"0.123", "3":"0.99" , "4":"0.5" , "5":"1.0" , "6":"0" }'
```

## POST MAN

I have exported a POSTMAN json file which you can import and use for testing with the POSTMAN app to make life easier ;-)

## Assumptions

- I'm assuming that "original" values are based on 3 weeks and are currently fixed values used to do the culculation on the "Modified" values passed from the post request.

- I'm assuming you did not want me to print out the DataFrame, but return the values I have multiplied with the DataFrame. I did leave a print(df.T) in the calc.py file which you can uncomment to view the dataframe output

- I'm assuming you did not want me to return JSON but just the outputed format with data required

- the last set of numbers did not round as all the previews numbers, I'm assuming that this is ok.

- I'm assuming you want to change the numbers to see the calculations happen, go ahead and post a new set of numbers.

## Judment Calls
- I did NOT create authentication because this wasn't an ask, but I would surely do that if it was a live deployment
- I did not create any type of validation of data being passed, usually this would be done.