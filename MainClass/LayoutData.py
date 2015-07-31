# -*- coding: utf-8 -*-
'''
Created on 11/07/2015

@author: DQ21989
'''


class LayoutData(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #Firm box definition
        self.__firmDataBoundingBoxX = 0
        self.__firmDataBoundingBoxY = 0
        self.__firmDataBoundingBoxW = 50
        self.__firmDataBoundingBoxH = 50
        self.__firmDataBoundingBoxDeltaX = 0
        self.__firmDataBoundingBoxDeltaY = 0
        
        #Firm data definitions
        self.__firmName = ''
        self.__firmNameDeltaX = 0
        self.__firmNameDeltaY = 5
        self.__firmNameX = 0
        self.__firmNameY = 0

        self.__firmDepartment = ''
        self.__firmDepartmentDeltaX = 0
        self.__firmDepartmentDeltaY = 10
        self.__firmDepartmentX = 0
        self.__firmDepartmentY = 0
        
        self.__firmAddress = ''
        self.__firmAddressDeltaX = 0
        self.__firmAddressDeltaY = 15
        self.__firmAddressX = 0
        self.__firmAddressY = 0
                
        self.__firmPostCode = ''
        self.__firmPostCodeDeltaX = 0
        self.__firmPostCodeDeltaY = 20
        self.__firmPostCodeX = 0
        self.__firmPostCodeY = 0
        
        self.__firmCity = ''
        self.__firmCityDeltaX = 10
        self.__firmCityDeltaY = 20
        self.__firmCityX = 0
        self.__firmCityY = 0
        
        self.__firmPhone = ''
        self.__firmPhoneDeltaX = 0
        self.__firmPhoneDeltaY = 25
        self.__firmPhoneX = 0
        self.__firmPhoneY = 0

        self.__firmMail = ''
        self.__firmMailDeltaX = 0
        self.__firmMailDeltaY = 30
        self.__firmMailX = 0
        self.__firmMailY = 0

        self.__firmWebpage = ''
        self.__firmWebpageDeltaX = 0
        self.__firmWebpageDeltaY = 35
        self.__firmWebpageX = 0
        self.__firmWebpageY = 0

        self.__firmLogo = ''
        self.__firmLogoDeltaX = 0
        self.__firmLogoDeltaY = 0
        self.__firmLogoX = 0
        self.__firmLogoY = 0

        #Username bounding box
        self.__userDataBoundingBoxX = 0
        self.__userDataBoundingBoxY = 0
        self.__userDataBoundingBoxW = 50
        self.__userDataBoundingBoxH = 20
        self.__userDataBoundingBoxDeltaX = 50
        self.__userDataBoundingBoxDeltaY = 10

        self.__userName = ''
        self.__userNameDeltaX = 0
        self.__userNameDeltaY = 0
        self.__userNameX = 0
        self.__userNameY = 0

        self.__userMail = ''
        self.__userMailDeltaX = 0
        self.__userMailDeltaY = 0
        self.__userMailX = 0
        self.__userMailY = 0

        #Other setup stuff
        self.__layoutName = ''
        self.__logoPath = ''
        
        self.__layoutPaperType = ''
        self.__layoutPaperOrientation = ''
        self.__paperX = 0
        self.__paperY = 0

        self.__layoutHeaderFont = None
        self.__layoutHeaderFontSize = 9
        self.__layoutTextFont = None
        self.__layoutTextFontSize = 12
        
    '''
    Firm textbox
    '''

    @property
    def firmDataBoundingBoxX(self):
        return self.__firmDataBoundingBoxX
    @property
    def firmDataBoundingBoxY(self):
        return self.__firmDataBoundingBoxY
    @property
    def firmDataBoundingBoxW(self):
        return self.__firmDataBoundingBoxW
    @property
    def firmDataBoundingBoxH(self):
        return self.__firmDataBoundingBoxH
    
    @property
    def firmNameX(self):
        return self.__firmNameX
    @property
    def firmNameY(self):
        return self.__firmNameY
    @property
    def firmName(self):
        return self.__firmName
    @firmName.setter
    def firmName(self,val):
        self.__firmName = val
        
    @property
    def firmDepartmentX(self):
        return self.__firmDepartmentX
    @property
    def firmDepartmentY(self):
        return self.__firmDepartmentY
    @property
    def firmDepartment(self):
        return self.__firmDepartment
    @firmDepartment.setter
    def firmDepartment(self,val):
        self.__firmDepartment = val
    
    @property
    def firmAddressX(self):
        return self.__firmAddressX
    @property
    def firmAddressY(self):
        return self.__firmAddressY
    @property
    def firmAddress(self):
        return self.__firmAddress
    @firmAddress.setter
    def firmAddress(self,val):
        self.__firmAddress = val

    @property
    def firmPostCodeX(self):
        return self.__firmPostCodeX
    @property
    def firmPostCodeY(self):
        return self.__firmPostCodeY
    @property
    def firmPostCode(self):
        return self.__firmPostCode
    @firmPostCode.setter
    def firmPostCode(self,val):
        self.__firmPostCode = val

    @property
    def firmCityX(self):
        return self.__firmCityX
    @property
    def firmCityY(self):
        return self.__firmCityY
    @property
    def firmCity(self):
        return self.__firmCity
    @firmCity.setter
    def firmCity(self,val):
        self.__firmCity = val

    @property
    def firmPhoneX(self):
        return self.__firmPhoneX
    @property
    def firmPhoneY(self):
        return self.__firmPhoneY
    @property
    def firmPhone(self):
        return self.__firmPhone
    @firmPhone.setter
    def firmPhone(self,val):
        self.__firmPhone = val

    @property
    def firmWebPageX(self):
        return self.__firmWebpageX
    @property
    def firmWebPageY(self):
        return self.__firmWebpageY
    @property
    def firmWebPage(self):
        return self.__firmWebpage
    @firmWebPage.setter
    def firmWebPage(self,val):
        self.__firmWebpage = val

    @property
    def firmMailX(self):
        return self.__firmMailX
    @property
    def firmMailY(self):
        return self.__firmMailY
    @property
    def firmMail(self):
        return self.__firmMail
    @firmMail.setter
    def firmMail(self,val):
        self.__firmMail = val

    @property
    def firmLogoX(self):
        return self.__firmLogoX
    @property
    def firmLogoY(self):
        return self.__firmLogoY
    @property
    def firmLogo(self):
        return self.__firmLogo
    @firmLogo.setter
    def firmLogo(self,val):
        self.__firmLogo = val
        
    '''
    User textbox
    '''
    @property
    def userDataBoundingBoxX(self):
        return self.__userDataBoundingBoxX
    @property
    def userDataBoundingBoxY(self):
        return self.__userDataBoundingBoxY
    @property
    def userDataBoundingBoxW(self):
        return self.__userDataBoundingBoxW
    @property
    def userDataBoundingBoxH(self):
        return self.__userDataBoundingBoxH

    
    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self,val):
        self.__userName = val
    
    @property
    def userMail(self):
        return self.__userMail
    @userMail.setter
    def userMail(self,val):
        self.__userMail = val
    
    @property
    def headerFont(self):
        return self.__layoutHeaderFont
    @headerFont.setter
    def headerFont(self,val):
        self.__layoutHeaderFont = val
    @property
    def headerFontSize(self):
        return self.__layoutHeaderFontSize
    @headerFontSize.setter
    def headerFontSize(self,val):
        self.__layoutHeaderFontSize = val

    @property
    def textFont(self):
        return self.__layoutTextFont
    @textFont.setter
    def textFont(self,val):
        self.__layoutTextFont = val
    @property
    def textFontSize(self):
        return self.__layoutTextFontSize
    @textFontSize.setter
    def textFontSize(self,val):
        self.__layoutTextFontSize = val
    
        
    
    @property
    def layoutName(self):
        return self.__layoutName
    @layoutName.setter
    def layoutName(self,val):
        self.__layoutName = val

    @property
    def logoPath(self):
        return self.__logoPath
    @logoPath.setter
    def logoPath(self,val):
        self.__logoPath = val
    
    @property
    def paperW(self):
        return self.__paperX
    @property
    def paperH(self):
        return self.__paperY
    
    def setPaperData(self,papertype,orientation):
        self.__layoutPaperType = papertype
        self.__layoutPaperOrientation = orientation
        self.calcLayoutProperties()
    
    def calcLayoutProperties(self):
        if self.__layoutPaperType == 'A4':
            if self.__layoutPaperOrientation == 'Portrait':
                self.__paperX = 210
                self.__paperY = 297
            else:
                self.__paperX = 297
                self.__paperY = 210
        elif self.__layoutPaperType == 'A3':
            if self.__layoutPaperOrientation == 'Portrait':
                self.__paperX = 297
                self.__paperY = 420
            else:
                self.__paperX = 420
                self.__paperY = 297
        elif self.__layoutPaperType == 'A2':
            if self.__layoutPaperOrientation == 'Portrait':
                self.__paperX = 420
                self.__paperY = 594
            else:
                self.__paperX = 594
                self.__paperY = 420
        elif self.__layoutPaperType == 'A1':
            if self.__layoutPaperOrientation == 'Portrait':
                self.__paperX = 594
                self.__paperY = 841
            else:
                self.__paperX = 841
                self.__paperY = 594
        elif self.__layoutPaperType == 'A0':
            if self.__layoutPaperOrientation == 'Portrait':
                self.__paperX = 841
                self.__paperY = 1189
            else:
                self.__paperX = 1189
                self.__paperY = 841
        #Calc firm box and data
        self.__firmDataBoundingBoxX = self.__paperX - self.__firmDataBoundingBoxDeltaX - self.__firmDataBoundingBoxW
        self.__firmDataBoundingBoxY = self.__paperY - self.__firmDataBoundingBoxDeltaY - self.__firmDataBoundingBoxH
        self.__firmNameX = self.__firmNameDeltaX + self.__firmDataBoundingBoxX
        self.__firmNameY = self.__firmNameDeltaY + self.__firmDataBoundingBoxY
        self.__firmDepartmentX = self.__firmDepartmentDeltaX + self.__firmDataBoundingBoxX
        self.__firmDepartmentY = self.__firmDepartmentDeltaY + self.__firmDataBoundingBoxY
        self.__firmAddressX = self.__firmAddressDeltaX + self.__firmDataBoundingBoxX
        self.__firmAddressY = self.__firmAddressDeltaY + self.__firmDataBoundingBoxY
        self.__firmPostCodeX = self.__firmPostCodeDeltaX + self.__firmDataBoundingBoxX
        self.__firmPostCodeY = self.__firmPostCodeDeltaY + self.__firmDataBoundingBoxY
        self.__firmCityX = self.__firmCityDeltaX + self.__firmDataBoundingBoxX
        self.__firmCityY = self.__firmCityDeltaY + self.__firmDataBoundingBoxY
        self.__firmPhoneX = self.__firmPhoneDeltaX + self.__firmDataBoundingBoxX
        self.__firmPhoneY = self.__firmPhoneDeltaY + self.__firmDataBoundingBoxY
        self.__firmWebpageX = self.__firmWebpageDeltaX + self.__firmDataBoundingBoxX
        self.__firmWebpageY = self.__firmWebpageDeltaY + self.__firmDataBoundingBoxY
        self.__firmMailX = self.__firmMailDeltaX + self.__firmDataBoundingBoxX
        self.__firmMailY = self.__firmMailDeltaY + self.__firmDataBoundingBoxY
        
        
        #calc userbox and data
        self.__userDataBoundingBoxX = self.__paperX - self.__userDataBoundingBoxDeltaX - self.__userDataBoundingBoxW
        self.__userDataBoundingBoxY = self.__paperY - self.__userDataBoundingBoxDeltaY - self.__userDataBoundingBoxH
        self.__userNameX = self.__userNameDeltaX + self.__userDataBoundingBoxX
        self.__userNameY = self.__userNameDeltaY + self.__userDataBoundingBoxY
        
        print 'Papir sat til:' + self.__layoutPaperType
        print 'Papir X/Y:' + str(self.__paperX) + '/' + str(self.__paperY)
        print 'firmabox X/Y:' + str(self.__firmDataBoundingBoxX) + '/' + str(self.__firmDataBoundingBoxY)
    
    