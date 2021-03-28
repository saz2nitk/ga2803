# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:44:27 2021

@author: saz2n
"""
import re
from loadData import ReadArticles

class PreprocessText:
    
    def __init__(self):
        
        self.specialChars = [',',';','#','$']
        readObj = ReadArticles()
        self.articleText = readObj.loadArticlesFromFile()
        self.stopWords = readObj.stopWordsFromFile()
        
    def sentTokenize(self,text):
        """Tokenize sentences from article.
        
        Input:
            text: string
        Output:
            sentArray: a list of strings
        """
        sentArray = text.split('.')
        return sentArray
    
    def wordTokenize(self,text):
        
        return re.split(' |,|;|-',text)
    
    def removeStopWords(self,text):
        
        wordList = self.wordTokenize(text)
        filteredWordList = [word for word in wordList if word not in self.stopWords]
        sentence = ' '.join(filteredWordList)
        return sentence
    
    def removeSpecialChar(self,text):
        
        sentence = ''.join([char for char in text if char not in self.specialChars])
        return  sentence
    
    def convertToLC(self,text):
        
        return text.lower()
    
    def preprocess(self):
        text = self.articleText
        sentences = self.sentTokenize(text)
        processedSentList = []
        for sentence in sentences:
            text = self.convertToLC(sentence)
            text = self.removeSpecialChar(text)
            text = self.removeStopWords(text)
            processedSentList.append(text)
        return processedSentList
    
#processObj = PreprocessText()
#processedSentList = processObj.preprocess()
#print('List of processed sentences: \n\n{}'.format(processedSentList))
#    
    