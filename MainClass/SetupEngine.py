from qgis.core import *
from qgis.gui import *
from PyQt4.Qt import QFont
class SetupEngine:
    def __init__(self,qgsIface):
        self.qgsIface = qgsIface
    def setQgsIface(self,qgsIface):
        self.qgsIface = qgsIface
    def setTextOne(self,txtOne):
        self.textOne = txtOne
    def setTextTwo(self,txtTwo):
        self.textTwo = txtTwo
    def createLayout(self):
        mapRenderer = self.qgsIface.mapCanvas().mapRenderer()
        self.composition = QgsComposition(mapRenderer)
        self.composition.setPlotStyle(QgsComposition.Print)
        x, y = 0, 0
        w, h = self.composition.paperWidth(), self.composition.paperHeight()
        print "W: %f - H: %f" % (w,h)
        composerMap = QgsComposerMap(self.composition, x,y,w,h)
        #self.composition.addItem(composerMap)
        #label
        composerLabel = QgsComposerLabel(self.composition)
        lblFont = QFont("Helvetica",12)
        composerLabel.font = lblFont
        composerLabel.setText("Hello world 20,20")
        composerLabel.setId("test1")
        composerLabel.adjustSizeToText()
        composerLabel.setItemPosition(20,20)
        
        self.composition.addItem(composerLabel)
        
        composerLabel2 = QgsComposerLabel(self.composition)
        lblFont2 = QFont("Helvetica",20)
        composerLabel2.font = lblFont2
        composerLabel2.setText("Hello world 75,75")
        composerLabel2.adjustSizeToText()
        composerLabel2.setItemPosition(75,75)
        
        self.composition.addItem(composerLabel2)


        #boks
        #composerBox = QgsComposerFrame(self.composition,0,0,10,10)

        #scalebar
        #item = QgsComposerScaleBar(c)
        #item.setStyle('Numeric') # optionally modify the style
        #item.setComposerMap(composerMap)
        #item.applyDefaultSize()
        #c.addItem(item)


        composerView = self.qgsIface.createNewComposer("min test")
        composerView.setComposition(self.composition)
        composer = composerView.composerWindow()
        composer.show()
        
        