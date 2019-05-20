#Author: Carlos A. Cepeda

from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

import os
import sys
import json
from clickhouse_driver import Client
from timeit import default_timer as timer

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/userdata/")
def provider():
    start = timer()
    firstname = request.args.get('fn')
    lastname = request.args.get('ln')
    client = Client('clickhouse-service')

    checker = True
    if((firstname != None) and (lastname != None)):
        query = 'SELECT * FROM default.data WHERE (PVD_FIRST_NAME = \'' + firstname + '\') AND (PVD_LAST_NAME = \'' + lastname + '\') limit 50 FORMAT JSON'
    elif(firstname != None):
        query = 'SELECT * FROM default.data WHERE (PVD_FIRST_NAME = \'' + firstname + '\') limit 50 FORMAT JSON'
    elif(lastname != None):
        query = 'SELECT * FROM default.data WHERE (PVD_LAST_NAME = \'' + lastname + '\') limit 50 FORMAT JSON'
    else:
        checker = False

    if (checker):
        resultlist = client.execute(query)
        end = timer()
        print(end - start)
        return jsonify({'providers':resultlist})
        end2 = timer()
        print(end2 - start)


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
