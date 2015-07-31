# -*- coding: Latin-1 -*-
'''
Created on 11/07/2015

@author: DQ21989
'''
from MainClass.LayoutItem import LayoutItem
class LayoutFactory(object):
    '''
    classdocs
    '''


    def __init__(self,iface):
        '''
        Constructor
        '''
        
        self.__iFace = iface
        self.__headerFont = "Helvetica"
        self.__headerSize = 8
        self.__textFont = "Helvetica"
        self.__textSize = 12
        self.__paperWidth = 290
        self.__paperHeight = 210
        #self.__orientation = 'Portrait'
    def setLayoutData(self,data):
        self.__layoutData = data
    def createLayout(self):
        if not self.__layoutData.layoutName is None and len(self.__layoutData.layoutName) > 0:
            self.__compositionView = self.__iFace.createNewComposer(self.__layoutData.layoutName)
        else:
            tmpCompName = LayoutItem().idGenerator()
            self.__compositionView = self.__iFace.createNewComposer(tmpCompName)
        self.composition = self.__compositionView.composition() 
        self.composition.setPaperSize(self.__layoutData.paperW,self.__layoutData.paperH)        
        self.createTextBoxes()
        self.createHeaderTexts()
        self.createLayoutTexts()
        #self.createImage()
        return self.composition
    def createMap(self):
        pass
        
    def createTextBoxes(self):
        self.createFirmTextBox()
        self.createUserTextBox()
    def createFirmTextBox(self):
        cmdText = u'ny tekstbox tilføjet'
        txtBxFirm = LayoutItem(self.composition)
        txtBxFirm.setPosition(self.__layoutData.firmDataBoundingBoxX ,self.__layoutData.firmDataBoundingBoxY)
        txtBxFirm.setWidthHeight(self.__layoutData.firmDataBoundingBoxW,self.__layoutData.firmDataBoundingBoxH)
        txtBxFirmRect = txtBxFirm.createRectangle()
        self.composition.addItem(txtBxFirmRect)
        self.composition.sendItemAddedSignal(txtBxFirmRect)
        self.composition.pushAddRemoveCommand(txtBxFirmRect,cmdText)
    def createUserTextBox(self):
        cmdText = u'ny tekstbox tilføjet'
        txtBxUser = LayoutItem(self.composition)
        txtBxUser.setPosition(self.__layoutData.userDataBoundingBoxX ,self.__layoutData.userDataBoundingBoxY)
        txtBxUser.setWidthHeight(self.__layoutData.userDataBoundingBoxW,self.__layoutData.userDataBoundingBoxH)
        txtBxUserRect = txtBxUser.createRectangle()
        self.composition.addItem(txtBxUserRect)
        self.composition.sendItemAddedSignal(txtBxUserRect)
        self.composition.pushAddRemoveCommand(txtBxUserRect,cmdText)
        
    def createHeaderTexts(self):
        self.createFirmHeaderText()
        self.createUserHeaderText()
    
    def createFirmHeaderText(self):
        cmdText = u'ny overskrift tilføjet'
        txtHeaderFirm = LayoutItem(self.composition)
        #txtHeaderFirm.setFont('Courier', 8)
        txtHeaderFirm.setFont(self.__layoutData.headerFont)
        txtHeaderFirm.setPosition(self.__layoutData.firmDataBoundingBoxX, self.__layoutData.firmDataBoundingBoxY)
        txtHeaderFirmLbl = txtHeaderFirm.createLabel('Firma')
        self.composition.addItem(txtHeaderFirmLbl)
        self.composition.sendItemAddedSignal(txtHeaderFirmLbl)
        self.composition.pushAddRemoveCommand(txtHeaderFirmLbl,cmdText)

    def createUserHeaderText(self):
        cmdText = u'ny overskrift tilføjet'
        txtHeaderUser = LayoutItem(self.composition)
        txtHeaderUser.setFont(self.__layoutData.headerFont)
        txtHeaderUser.setPosition(self.__layoutData.userDataBoundingBoxX, self.__layoutData.userDataBoundingBoxY)
        txtHeaderUserLbl = txtHeaderUser.createLabel('Bruger')
        self.composition.addItem(txtHeaderUserLbl)
        self.composition.sendItemAddedSignal(txtHeaderUserLbl)
        self.composition.pushAddRemoveCommand(txtHeaderUserLbl,cmdText)

    def createLayoutTexts(self):
        self.createLayoutTxt(self.__layoutData.firmNameX,self.__layoutData.firmNameY,self.__layoutData.firmName)
        self.createLayoutTxt(self.__layoutData.firmDepartmentX,self.__layoutData.firmDepartmentY,self.__layoutData.firmDepartment)
        self.createLayoutTxt(self.__layoutData.firmAddressX,self.__layoutData.firmAddressY,self.__layoutData.firmAddress)
        self.createLayoutTxt(self.__layoutData.firmPostCodeX,self.__layoutData.firmPostCodeY,self.__layoutData.firmPostCode)
        self.createLayoutTxt(self.__layoutData.firmCityX,self.__layoutData.firmCityY,self.__layoutData.firmCity)
        self.createLayoutTxt(self.__layoutData.firmPhoneX,self.__layoutData.firmPhoneY,self.__layoutData.firmPhone)
        self.createLayoutTxt(self.__layoutData.firmWebPageX,self.__layoutData.firmWebPageY,self.__layoutData.firmWebPage)
        self.createLayoutTxt(self.__layoutData.firmMailX,self.__layoutData.firmMailY,self.__layoutData.firmMail)
        
    def createLayoutTxt(self,x,y,curText):
        cmdText = u'ny tekst tilføjet'
        txt = LayoutItem(self.composition)
        txt.setFont(self.__layoutData.textFont)
        txt.setPosition(x, y)
        txtFin = txt.createLabel(curText)
        self.composition.addItem(txtFin)
        self.composition.sendItemAddedSignal(txtFin)
        self.composition.pushAddRemoveCommand(txtFin,cmdText)      
        
    def createImage(self):
        cmdText = u'nyt billede tilføjet'
        pic = LayoutItem(self.composition)
        pic.setPosition(200, 200)
        curPic = pic.createPicture(self.__layoutData.logoPath)
        self.composition.addItem(curPic)
        self.composition.sendItemAddedSignal(curPic)
        self.composition.pushAddRemoveCommand(curPic,cmdText)      
        
        

        
         
        
        