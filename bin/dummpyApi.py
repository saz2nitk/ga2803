# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:18:09 2021

@author: saz2n
"""

import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/home',methods=['GET'])
def printYay():
    return "Yay!! the api is fine !!!"

@app.route('/home/work',methods=['GET'])
def printWork():
    return "I am going to work"

app.run(host='127.0.0.1',port=8080, debug=True)
