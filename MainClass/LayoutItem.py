# -*- coding: utf-8 -*-
'''
Created on 12/07/2015

@author: DQ21989
'''
from qgis._core import QgsComposerLabel,QgsComposerShape,QgsFillSymbolV2,QgsComposerPicture
from PyQt4.Qt import QFont,QPointF
import string
import random
class LayoutItem(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.__fontName = "Courier"
        self.__fontSize = 12
        self.__positionX = 0
        self.__positionY = 0
        self.__positionW = 0
        self.__positionH = 0
        self.__composition = params
        self.__symbolProperties = {'color':'255,255,255,255','color_border':'0,0,0,255','style_border':'solid','width_border':'0.5'}
        self.__font = None
    def setFont(self,font):
        self.__font = font
    def setPosition(self,x,y):
        self.__positionX = x
        self.__positionY = y
    def setWidthHeight(self,w,h):
        self.__positionW = w
        self.__positionH = h
    def updateProp(self,curKey,curVal):
        self.__symbolProperties[curKey] = curVal
    def createLabel(self,labelText):
        label = QgsComposerLabel(self.__composition)
        #labelFont = QFont(self.__la)
        label.setFont(self.__font)
        label.setText(labelText)
        label.setId(self.idGenerator())
        label.adjustSizeToText()
        label.setItemPosition(self.__positionX,self.__positionY)
        return label
    def createRectangle(self):
        rectangle = QgsComposerShape(self.__positionX,self.__positionY,self.__positionW,self.__positionH, self.__composition)
        self.__masterSym = QgsFillSymbolV2()
        curSym = self.__masterSym.createSimple(self.__symbolProperties)
        rectangle.setShapeType(QgsComposerShape.Rectangle)
        rectangle.setUseSymbolV2(True)
        rectangle.setShapeStyleSymbol(curSym)
        rectangle.setId(self.idGenerator())
        return rectangle
    def createPicture(self,path):
        curPictur = QgsComposerPicture(self.__composition)
        curPictur.setPos(QPointF(self.__positionX,self.__positionY))
        curPictur.setPictureFile(path)
        curPictur.setResizeMode(QgsComposerPicture.FrameToImageSize)
        curPictur.setId(self.idGenerator())
        return curPictur
    def idGenerator(self,size=8, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
            