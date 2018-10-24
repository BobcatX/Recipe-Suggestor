# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:24:59 2018

@author: Jim Witt, Anna Bobcova

Program to implement UI using PyQt5. Handles the main window UI, calls SubmitUI
(SubmitterWindow.py) class to open a recipe submit window. Searches a database 
for recipes containing ingredients entered by the user. Returns ingredients, 
directions, and an image of the final product.
"""
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import *
from DirectionsDisplay import *
from recipereader import *
from SubmitterWindow import *

#filepath
filepath = os.path.dirname(os.path.realpath(__file__))

# UI file
file = str(filepath)+"\\layout\\Recipe_Suggestor.ui"

#Graphical Interface particles ------------------------------------------------
w_icon = str(filepath)+"\\layout\\leek-icon.jpg"
background = str(filepath)+"\\layout\\MainScreen.jpg"
pugFace = str(filepath)+"\\layout\\placeholder.jpg"

b_add = str(filepath)+"\\layout\\button-add.jpg"
b_search = str(filepath)+"\\layout\\button-search.jpg"
b_reset = str(filepath)+"\\layout\\button-reset.jpg"
b_seeDir = str(filepath)+"\\layout\\button-seeDir.jpg"
b_seeOther = str(filepath)+"\\layout\\button-seeOther.jpg"

#------------------------------------------------------------------------------
Ui_MainWindow, QtBaseClass = uic.loadUiType(file)
q = RecipeReader()

index = 0 #Index variable
x=0
ingr1=''
ingr2=''
suggs=''

#recipe image Dimensions
recipe_w = 361
recipe_h = 241

#------------------------------------------------------------------------------
###############################################################################
#  MyApp class handles the UI if the main program window and functionality    #
#  it has the ability to call another window to submit own recipes from the   #
#  taskbar. Mainly utilizes 'recipereader' class to read recipe files from    #
#  the library/database.                                                      #
###############################################################################
#------------------------------------------------------------------------------
class MyApp(QMainWindow):
    def __init__(self):
        # sets up the window display
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(w_icon))################################@@@
        
        #recipe image functionality
        pixmap = QPixmap(pugFace)
        self.ui.picLabel.setPixmap(pixmap.scaled(recipe_w,recipe_h))
        
        #bg image functionality
        bg = QPixmap(background)
        self.ui.backG.setPixmap(bg)
        
        # button functionality ------------------------------------------------
        # button - add ingredient
        self.ui.addIngr.clicked.connect(self.add)
        self.ui.addIngr.setIcon(QtGui.QIcon(b_add))
        self.ui.addIngr.setIconSize(QtCore.QSize(97,31))
        
        # button - reset - NOT BUGGY (as of 5/31)
        self.ui.reset.clicked.connect(self.reset)
        self.ui.reset.setIcon(QtGui.QIcon(b_reset))
        self.ui.reset.setIconSize(QtCore.QSize(97,31))
        
        # button - search
        self.ui.Imdone.clicked.connect(self.search)
        self.ui.Imdone.setIcon(QtGui.QIcon(b_search))
        self.ui.Imdone.setIconSize(QtCore.QSize(97,31))
        
        # button - see directions for this recipe
        self.ui.Seedir.clicked.connect(self.direction)
        self.ui.Seedir.setIcon(QtGui.QIcon(b_seeDir))
        self.ui.Seedir.setIconSize(QtCore.QSize(309,29))
        
        #button - choose a different recipe
        self.ui.chooseDif.clicked.connect(self.tryDiff) #Still need to add this functionality.
        self.ui.chooseDif.setIcon(QtGui.QIcon(b_seeOther))
        self.ui.chooseDif.setIconSize(QtCore.QSize(309,29))
        
        # toolbar buttons
        self.ui.helpInstr.triggered.connect(self.hb)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.submitLibrary.triggered.connect(self.recSubmit)
        
        
        #hover-over status messages/version+credit
        self.statusBar().showMessage('RecipeSuggestor v 0.2 May 2018: A.Bobcova, J.Witt')
        #self.ui.helpInstr.setStatusTip('Get Help')
        self.show()
        
    # Help/Instructions window    
    def hb(self):
        #QMessageBox.about(self, "RST Instructions", "Click and type stuff, and you'll get a recipe.")
        self.dialog = RecipeDirections()
        self.dialog.displayMainHelp()
        self.dialog.show()
    
    def about(self):
        #QMessageBox.about(self, "RST Instructions", "Click and type stuff, and you'll get a recipe.")
        self.dialog = RecipeDirections()
        self.dialog.displayAbout()
        self.dialog.show()
    
    # Opens Submission UI -- see SubmitterWindow.py
    def recSubmit(self):
        #QMessageBox.about(self, "Submit", "Yay, I'm a placeholder!")
        self.dialog = SubmitUI()
        self.dialog.show()
        
    # handles takes user tngredient inputs, displays them in the UI. Trying 
    # to add an item without anything entered into the text input box results 
    # in an error dialog box
    def add(self):
        global x
        global ingr1
        global ingr2
        
        ingredient = str(self.ui.entry.toPlainText())
        self.ui.entry.setText('')
        if len(ingredient) > 0:
            if x == 0:
                self.ui.in1Found.setText(ingredient)
                ingr1 = ingredient
                x += 1
            else:
                self.ui.in2Found.setText(ingredient)
                ingr2 = ingredient
                x = 0
        else:
            QMessageBox.about(self, "Error", "Please enter an ingredient.")####@@@
    
    # resets recipe search ingredients -- just sets ingr1/ingr2 and where they
    # would display to blank
    def reset(self):
        global ingr1
        global ingr2
        global x
        x = 0
        ingr1 = ''
        ingr2 = ''
        self.ui.in1Found.setText('')
        self.ui.in2Found.setText('')
        self.ui.suggName.clear()
        self.ui.reciList.clear()
        pixmap = QPixmap(pugFace)
        self.ui.picLabel.setPixmap(pixmap.scaled(recipe_w,recipe_h))

    # Uses recipereader class methods to update name, ingredients list, and 
    # image. If no ingredients are entered, an error dialog pops up
    def search(self):
        global ingr1
        global ingr2
        global suggs
        global index
        if len(ingr2) > 2:
            suggs = q.recSearch(ingr1,ingr2)
        else:
            suggs = q.oneSearch(ingr1)
        self.ui.suggName.setText(suggs)
        index = q.getIndex(suggs) #name is used to find index
        if len(suggs)>-1:
            text = q.recIngr(index)
            self.ui.reciList.setText(text)
            pixmap = QPixmap(q.recImg(index))
            self.ui.picLabel.setPixmap(pixmap.scaled(recipe_w,recipe_h))
        else:
            QMessageBox.about(self, "Error", "No ingredients entered. Please enter at least one ingredient, and try again.")
            
    #Uses one recipereader method to get the directions and then opens them in a messagebox
    def direction(self):
        global index
        
        directions = q.recInst(index)
        self.dialog = RecipeDirections()
        self.dialog.displayDirections(index)
        self.dialog.show()
        #QMessageBox.about(self, "Directions", directions)

    def tryDiff(self):
        global ingr1
        global ingr2
        global suggs
        global index
        
        suggs = q.diffSearch(ingr1,ingr2,index)
        self.ui.suggName.setText(suggs)
        index = q.getIndex(suggs) #name is used to find index
        if len(suggs)>0:
            text = q.recIngr(index)
            self.ui.reciList.setText(text)
            pixmap = QPixmap(q.recImg(index))
            self.ui.picLabel.setPixmap(pixmap.scaled(recipe_w,recipe_h))
        else:
            QMessageBox.about(self, "Error", "No ingredients entered. Please enter at least one ingredient, and try again.")
        
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------        
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()