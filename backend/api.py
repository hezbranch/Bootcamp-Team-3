from flask import Flask
from flask import request
import pyodbc
import requests


import ast

app = Flask(__name__)





@app.route("/backend/time")
def getTime():
    import time

    ## No need to jsonify
    return {"time": time.time()}


@app.route("/backend/formAPI", methods=["GET", "POST"])
def formAPI():
    if request.method == "GET":
        print("request.args =", request.args)
        orgName = request.args.get("orgName")

        ## Implement backend logic here

        ## Implement SQL logic here

        ## No need to jsonify
        return {"orgName": orgName}

    elif request.method == "POST":
        dict_str = request.data.decode("UTF-8")
        postData = ast.literal_eval(dict_str)

        inputParams = postData.get("params")

        orgName = inputParams.get("orgName")

        ## Implement backend logic here

        ## Implement SQL logic here

        ## No need to jsonify
        return {"orgName": orgName}


@app.route("/backend/createAccount", methods=["GET", "POST"])
def userFormAPI():
    if request.method == "GET":
        return userInfoVerification(request.args)

    elif request.method == "POST":
        dict_str = request.data.decode("UTF-8")
        postData = ast.literal_eval(dict_str)

        inputParams = postData.get("params")

        return userInfoVerification(inputParams)


def userInfoVerification(inputParams):

    email = inputParams.get("email")
    username = inputParams.get("username")
    pasW = inputParams.get("pass")
    pasWConf = inputParams.get("passConf")

    if pasW != pasWConf:
        return {"error": "passConf"}
    if len(pasW) < 5:
        return {"error": "passIsShort"}
    if pasW.islower():
        return {"error": "passIsLower"}
    if pasW.isupper():
        return {"error": "passIsUpper"}

    ## We can put the username through the database here to check if this user already exists

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FFDB.dbo.Users WHERE username = ' + username + 'OR email = ' + email)

    if cursor == null:
        cursor.execute('INSERT INTO FFDB.dbo.Users (username, password, email) VALUES ('+username+', '+pasW+','+email+')')
    else:
        return {"error"} #Specify error that username or email are already in use


    ## At this point, the user information is valid

    ## We send this data to the database
    userInfo = {"email": email, "username": username, "pass": pasW, "verified": True}

    return userInfo


@app.route("/backend/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return loginVerification(request.args)

    elif request.method == "POST":
        dict_str = request.data.decode("UTF-8")
        postData = ast.literal_eval(dict_str)

        inputParams = postData.get("params")

        return loginVerification(inputParams)


def loginVerification(inputParams):

    username = inputParams.get("username")
    pasW = inputParams.get("pass")

    ## VERIFY W/ DATABASE HERE
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FFDB.dbo.Users WHERE username = {} AND password = {}').format(username, pasW)
    #cursor.execute('SELECT * FROM FFDB.Users WHERE username = ' + username + 'AND password = ' + pasW)


    if cursor != null:
        return {} # login successful
    else:
        return {"error"} #Specify error that username or password are not correct

    ## We can put the username through the database here to check if this user already exists
    ## At this point, the user information is valid



    ## We send this data to the database
    userInfo = {"username": username, "pass": pasW, "verified": True}

    return userInfo

@app.route('/backend/search', methods=['GET', 'POST'])
def search_data():

    # First clears out the old search items
    # 
    # Gets value of term user sent in
    if request.method == "POST":
        json_data = request.get_json()
        search_term = json_data["search_term"]


    # Just for testing purposes right now
    return true;
