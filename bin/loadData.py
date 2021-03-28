# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:09:04 2021

@author: saz2n
"""

class ReadArticles:
    
    def __init__(self):
        self.dataPath = './data/train/article1.txt'
        self.stopWordPath = './data/stopWords.txt'
            
    def loadArticlesFromFile(self):
        with open(self.dataPath,'r') as fl:
            text = fl.read()
        return text
    
    def stopWordsFromFile(self):
        with open(self.stopWordPath,'r') as fl:
            text = fl.read()
        return text.split('\n')
        
    def loadArticlesFromDb(self):
        pass
    
    def loadArticlesFromApi(self):
        pass
    
#readObj = ReadArticles()
#articleText = readObj.loadArticlesFromFile()
#print('The text is:\n\n{}'.format(articleText))