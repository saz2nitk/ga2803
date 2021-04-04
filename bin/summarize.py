# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:34:04 2021

@author: saz2n
"""
import numpy
from preProcessor import PreprocessText
import flask
from flask import Flask, request
import json
import tweepy

summaryApp = Flask(__name__)

class SummarizeArticle:
    
    def __init__(self,article):
        processObj = PreprocessText()
        self.sentArray = processObj.preprocess(article)
    
    def groupSentences(self,sentArray):
        
        firstSent = sentArray[0]
        restSents = sentArray[1:]
        return firstSent, restSents
    
    def sortSentences(self,restSents):
        sentLengths = [len(sent) for sent in restSents]
        sortedIdxs = numpy.argsort(sentLengths)
        sortedSentences = []
        for idx in sortedIdxs:
            sortedSentences.append(restSents[len(restSents)-idx-1])
        return sortedSentences
    
    def combineSentences(self,firstSent,sortedSentences):
        
        combinedSentences = [firstSent] + sortedSentences[:5]
        summary = ' '.join(combinedSentences)
        return summary
    
    def summarize(self):
        
        firstSent,restSents = self.groupSentences(self.sentArray)
        sortedSentences = self.sortSentences(restSents)
        summary = self.combineSentences(firstSent,sortedSentences)
        return summary

#@summaryApp.route('/home/summary/default',methods=['GET'])     
#def summaryApi():
#    summaryObj = SummarizeArticle()
#    summary = summaryObj.summarize()
#    return summary
#    #print('The summary is:\n\n{}'.format(summary))
        
@summaryApp.route('/home',methods=['GET'])
def printYay():
    return "Yay!! the api is fine !!!"

@summaryApp.route('/home/work',methods=['GET'])
def printWork():
    return "I am going to work"
    
@summaryApp.route('/home/summary/custom',methods=['POST'])     
def summaryApi():
    article = json.loads(request.data.decode())['articleText']
    summaryObj = SummarizeArticle(article)
    summary = summaryObj.summarize()
    return summary
    #print('The summary is:\n\n{}'.format(summary))

summaryApp.run('0.0.0.0','8000')
            
    
    
