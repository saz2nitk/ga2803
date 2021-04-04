# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:18:09 2021

@author: saz2n
"""

import flask
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/home',methods=['GET'])
def printYay():
    return "Yay!! the api is fine !!!"

@app.route('/home/work',methods=['GET'])
def printWork():
    return "I am going to work"

@app.route('/home/custom',methods=['POST'])
def printCustomTextLower():
#    text = request.data
#    text = text.decode()
#    text = json.loads(text)
    text = json.loads(request.data.decode())['textData']
    #print(text)
    return text.lower()

app.run(host='127.0.0.1',port=8080)
