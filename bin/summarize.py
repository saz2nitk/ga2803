# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:34:04 2021

@author: saz2n
"""
import numpy
from preProcessor import PreprocessText
import flask
from flask import Flask, request

summaryApp = Flask(__name__)

class SummarizeArticle:
    
    def __init__(self):
        processObj = PreprocessText()
        self.sentArray = processObj.preprocess()
    
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

@summaryApp.route('/home/summary',methods=['GET'])     
def summaryApi():
    summaryObj = SummarizeArticle()
    summary = summaryObj.summarize()
    return summary
    #print('The summary is:\n\n{}'.format(summary))

summaryApp.run('127.0.0.1','8000')
            
    
    
