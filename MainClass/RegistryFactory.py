# -*- coding: utf-8 -*-
'''
Created on 22/07/2015

@author: dq21989
'''
from _winreg import *
from MainClass.LayoutData import LayoutData
from PyQt4.Qt import QFont

class RegistryFactory(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__registryMasterKey = r'Software\QgsLayoutWizard\LayouData'
    def doesMasterKeyExists(self):
        exists = False
        try:
            OpenKey(HKEY_LOCAL_MACHINE, self.__registryMasterKey, 0, KEY_ALL_ACCESS)
            exists = True
        except EnvironmentError:
            pass
        return exists
    def handleRegistry(self):
        exists = self.doesMasterKeyExists()
        if not exists:
            self.createLayoutKey()
    def createLayoutKey(self):
        CreateKey(HKEY_LOCAL_MACHINE,r'Software\QgsLayoutWizard\LayouData')
    def writeLayoutData(self,data):
        print 'writeLayoutData kaldt'
        self.handleRegistry()
        registry_key = OpenKey(HKEY_LOCAL_MACHINE, self.__registryMasterKey, 0,KEY_WRITE)
        SetValueEx(registry_key, 'firmanavn', 0, REG_SZ, data.firmName)
        SetValueEx(registry_key, 'firmaafdeling', 0, REG_SZ, data.firmDepartment)
        SetValueEx(registry_key, 'firmaadresse', 0, REG_SZ, data.firmAddress)
        print 'Skriver postnr:' + data.firmPostCode
        SetValueEx(registry_key, 'firmapostnr', 0, REG_SZ, data.firmPostCode)
        print 'Skriver by:' + data.firmCity
        SetValueEx(registry_key, 'firmaby', 0, REG_SZ, data.firmCity)
        SetValueEx(registry_key, 'firmatlf', 0, REG_SZ, data.firmPhone)
        SetValueEx(registry_key, 'firmawebside', 0, REG_SZ, data.firmWebPage)
        SetValueEx(registry_key, 'firmamail', 0, REG_SZ, data.firmMail)
        SetValueEx(registry_key, 'firmalogo', 0, REG_SZ, data.firmLogo)
        SetValueEx(registry_key, 'overskriftsfont', 0, REG_SZ, data.headerFont.family())
        SetValueEx(registry_key, 'overskriftsfontstr', 0, REG_SZ, str(data.headerFontSize))
        SetValueEx(registry_key, 'tekstfont', 0, REG_SZ, data.textFont.family())
        SetValueEx(registry_key, 'tekstfontstr', 0, REG_SZ, str(data.textFontSize))
        
        CloseKey(registry_key)
    def readLayoutData(self):
        data = LayoutData()
        try:
            self.handleRegistry()
            registry_key = OpenKey(HKEY_LOCAL_MACHINE, self.__registryMasterKey, 0, KEY_READ)
            
            data.firmName = QueryValueEx(registry_key, 'firmanavn')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            data.firmDepartment = QueryValueEx(registry_key, 'firmaafdeling')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            data.firmAddress = QueryValueEx(registry_key, 'firmaadresse')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            data.firmPostCode = QueryValueEx(registry_key, 'firmapostnr')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            data.firmCity = QueryValueEx(registry_key, 'firmaby')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            data.firmPhone = QueryValueEx(registry_key, 'firmatlf')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            data.firmWebPage = QueryValueEx(registry_key, 'firmawebside')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            data.firmMail = QueryValueEx(registry_key, 'firmamail')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            data.firmLogo = QueryValueEx(registry_key, 'firmalogo')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]

            data.headerFontSize = int(QueryValueEx(registry_key, 'overskriftsfontstr')[0]) #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            if data.headerFontSize is None:
                data.headerFontSize = 9

            data.textFontSize = int(QueryValueEx(registry_key, 'tekstfontstr')[0]) #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            if data.textFontSize is None:
                data.textFontSize = 12
            
            tmpHeaderFont = QueryValueEx(registry_key, 'overskriftsfont')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1]
            if not tmpHeaderFont is None:
                print 'opretter overskriftsfont: %s - str: %i'% (tmpHeaderFont,data.headerFontSize) 
                data.headerFont = QFont(tmpHeaderFont,data.headerFontSize)
            
            
            tmpTextFont = QueryValueEx(registry_key, 'tekstfont')[0] #QueryValueEx returns a tuple with the value as [0] and the type as [1] 
            if not tmpTextFont is None:
                print 'opretter tekstfont:' + tmpTextFont
                data.textFont = QFont(tmpTextFont,data.textFontSize)
        except EnvironmentError:
            pass
        
        CloseKey(registry_key)
        return data
        
