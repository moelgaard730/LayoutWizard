# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MainClassDialog
                                 A QGIS plugin
 Første udkast
                             -------------------
        begin                : 2015-06-30
        git sha              : $Format:%H$
        copyright            : (C) 2015 by kmr
        email                : kmr@randers.dk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.Qt import QObject, SIGNAL, QFont
from PyQt4.QtGui import QFileDialog
from MainClass.LayoutData import LayoutData
from MainClass.RegistryFactory import RegistryFactory

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'MainModule_dialog_base.ui'))


class MainClassDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MainClassDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.__layoutData = LayoutData()
        QObject.connect(self.btnLogoFilepicker, SIGNAL("clicked()"),self.pickLogoFile)
        
    def handleData(self):
        
        self.__layoutData.firmName = self.txtBxFirmName.text()
        self.__layoutData.firmDepartment = self.txtBxFirmDepartment.text()
        self.__layoutData.firmAddress = self.txtBxFirmAddress.text()
        self.__layoutData.firmPostCode = self.txtBxFirmPostCode.text()
        self.__layoutData.firmCity = self.txtBxFirmCity.text()
        self.__layoutData.firmPhone = self.txtBxFirmPhone.text()
        
        self.__layoutData.firmWebPage = self.txtBxFirmWebpage.text()
        self.__layoutData.firmMail = self.txtBxFirmMail.text()
        self.__layoutData.firmLogo = self.txtBxFirmLogo.text()
        self.__layoutData.layoutName = self.txtBxLayoutName.text()
        self.txtBxLayoutName.setText('') #empty the textbox
        self.__layoutData.headerFont = self.fontCmbBxHeader.currentFont()
        self.__layoutData.headerFontSize = self.spinBoxHeaderFontSize.value()
        self.__layoutData.headerFont.setPointSize(int(self.__layoutData.headerFontSize))
        self.__layoutData.textFont = self.fontCmbBxText.currentFont()
        self.__layoutData.textFontSize = self.spinBoxTextFontSize.value()
        self.__layoutData.textFont.setPointSize(int(self.__layoutData.textFontSize))
        
        self.handleSelectedPaper()
        RegistryFactory().writeLayoutData(self.__layoutData)
    def handleSelectedPaper(self):
        paper = self.cmbBxPaper.currentText()
        if self.rdoBtnPortrait.isChecked():
            self.__layoutData.setPaperData(paper,'Portrait')
        else:
            self.__layoutData.setPaperData(paper,'Landscape')
        
    def getData(self):
        return self.__layoutData
    def fillGUI(self):
        self.fillPaperComboBox()
        self.rdoBtnPortrait.setChecked(True)
        self.__layoutData = RegistryFactory().readLayoutData()
        if not self.__layoutData.firmName is None:
            self.txtBxFirmName.setText(self.__layoutData.firmName)
        
        if not self.__layoutData.firmDepartment is None:
            self.txtBxFirmDepartment.setText(self.__layoutData.firmDepartment)
        
        if not self.__layoutData.firmAddress is None:
            self.txtBxFirmAddress.setText(self.__layoutData.firmAddress)
        
        if not self.__layoutData.firmPostCode is None:
            self.txtBxFirmPostCode.setText(self.__layoutData.firmPostCode)
        
        if not self.__layoutData.firmCity is None:
            self.txtBxFirmCity.setText(self.__layoutData.firmCity)
        
        if not self.__layoutData.firmPhone is None:
            self.txtBxFirmPhone.setText(self.__layoutData.firmPhone)
        
        if not self.__layoutData.firmWebPage is None:
            self.txtBxFirmWebpage.setText(self.__layoutData.firmWebPage)
        
        if not self.__layoutData.firmMail is None:
            self.txtBxFirmMail.setText(self.__layoutData.firmMail)
        
        if not self.__layoutData.firmLogo is None:
            self.txtBxFirmLogo.setText(self.__layoutData.firmLogo)
        
        if type(self.__layoutData.headerFont) is QFont:
            self.fontCmbBxHeader.setCurrentFont(self.__layoutData.headerFont)
        else:
            print 'overskriftsfont ikke legal'

        if type(self.__layoutData.textFont) is QFont:
            self.fontCmbBxText.setCurrentFont(self.__layoutData.textFont)
        else:
            print 'tekstfont ikke legal'
        
        if not self.__layoutData.headerFontSize is None:
            self.spinBoxHeaderFontSize.setValue(int(self.__layoutData.headerFontSize))
    
        if not self.__layoutData.textFontSize is None:
            self.spinBoxTextFontSize.setValue(int(self.__layoutData.textFontSize))

    def fillPaperComboBox(self):
        self.cmbBxPaper.addItem('A4')
        self.cmbBxPaper.addItem('A3')
        self.cmbBxPaper.addItem('A2')
        self.cmbBxPaper.addItem('A1')
        self.cmbBxPaper.addItem('A0')
    def pickLogoFile(self):
        self.__layoutData.logoPath = QFileDialog.getOpenFileName(self, u'Vælg en billedfil')
        self.txtBxFirmLogo.setText(self.__layoutData.logoPath)
        print u'Filen der blev valgt:' +  self.__layoutData.logoPath
