# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:45:57 2018

@author: annaw
"""

import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import *
from DirectionsDisplay import *
from recipereader import *
from recipewriter import *

#filepath
filepath = os.path.dirname(os.path.realpath(__file__))
# Ui file
file = str(filepath)+"\\layout\\Recipe_Submitter_v3.ui"

# Graphical Interface particles -----------------------------------------------
w_icon = str(filepath)+"\\layout\\leek-icon.jpg"
background = str(filepath)+"\\layout\\submit_mainScreen.jpg"
pugFace = str(filepath)+"\\layout\\placeholderPug-Submit.jpg"

b_submit = str(filepath)+"\\layout\\button-submit.jpg"
b_add = str(filepath)+"\\layout\\button-add.jpg"
b_undo = str(filepath)+"\\layout\\button-undo.jpg"
b_file = str(filepath)+"\\layout\\button-file.jpg"
b_save = str(filepath)+"\\layout\\button-save.jpg"
b_reset = str(filepath)+"\\layout\\button-reset-lrg.jpg"
#b_close = str(filepath)+"\\layout\\button-close.jpg"
#b_close_grey = str(filepath)+"\\layout\\button-close-g.jpg"

#------------------------------------------------------------------------------

Ui_MainWindow, QtBaseClass = uic.loadUiType(file)
q = RecipeReader()
p = recipeWriter()
user_pic = QPixmap
name = ''
ingr = ''
directions = ''
ingr_list = list()

#user image size
recipe_w = 361
recipe_h = 241

# formatted or not
formatted = False

#------------------------------------------------------------------------------
###############################################################################
#  SubmitUI class handles the UI if the 'Submit your recipe' window, and it's #
#  fuctionality. Is called by the main window, defined in GuImple class, and  #
#  utilizes recipewriter class to ass user-submitted files to the database    #
###############################################################################
#------------------------------------------------------------------------------
class SubmitUI(QMainWindow):
    def __init__(self):
        super(SubmitUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(w_icon))################################@@@
        
        # button functionality + graphics -------------------------------------
        # toolbar - help
        self.ui.helpInstr.triggered.connect(self.hb)
        
        # button - add name
        self.ui.recName_submit.clicked.connect(self.userName)
        self.ui.recName_submit.setIcon(QtGui.QIcon(b_submit))
        self.ui.recName_submit.setIconSize(QtCore.QSize(97,31))
        
        # button - add ingredient
        self.ui.recIngr_Add.clicked.connect(self.userIngredients)
        self.ui.recIngr_Add.setIcon(QtGui.QIcon(b_add))
        self.ui.recIngr_Add.setIconSize(QtCore.QSize(97,31))
        
        # button - undo ingredient add
        self.ui.recIngr_undo.clicked.connect(self.undoIngr)
        self.ui.recIngr_undo.setIcon(QtGui.QIcon(b_undo))
        self.ui.recIngr_undo.setIconSize(QtCore.QSize(97,31))
        
        # button - select image file 
        self.ui.file_select.clicked.connect(self.openFileNameDialog) #Functionality added 5/28!
        self.ui.file_select.setIcon(QtGui.QIcon(b_file))
        self.ui.file_select.setIconSize(QtCore.QSize(97,31))
        
        # button - reset
        self.ui.submitRec_Reset.clicked.connect(self.subReset) 
        self.ui.submitRec_Reset.setIcon(QtGui.QIcon(b_reset))
        self.ui.submitRec_Reset.setIconSize(QtCore.QSize(249,39))
        
        # button format
        # ---
        # this button should initiate the transition of user input in the 
        # window to files in the database.
        # ---
        self.ui.submitRec_Format.clicked.connect(self.writeOut)
        self.ui.submitRec_Format.clicked.connect(self.inputDone)
        self.ui.submitRec_Format.setIcon(QtGui.QIcon(b_save))
        self.ui.submitRec_Format.setIconSize(QtCore.QSize(249,39))
    
        # user_image pug placeholder
        pic = QPixmap(pugFace)
        self.ui.selected_pic.setPixmap(pic.scaled(recipe_w,recipe_h))
        
        # background
        bg = QPixmap(background)
        self.ui.backG.setPixmap(bg)
        
        # hover-over status message
        self.statusBar().showMessage('RecipeSuggestor v 0.2 May 2018: A.Bobcova, J.Witt - Submit a Recipe')
        self.show()
        #This will the the help-box pop-up dialog
        
    def hb(self):
        #QMessageBox.about(self, "How to Use Recipe Submission Form", "Click and type stuff, and you'll get a recipe.")
        self.dialog = RecipeDirections()
        self.dialog.displaySubmitHelp()
        self.dialog.show()
    
    #Gets a name from input, and displays it back to the user
    def userName(self):
        global name
        enteredName = str(self.ui.recName_input.toPlainText())
        self.ui.recName_input.setText('')
        if len(enteredName) > 0:
            self.ui.recName_displayName.setText(enteredName)
            name = enteredName
        else:
            QMessageBox.about(self, "Error", "Please enter a name for your recipe.")
    
    #Takes care of user-entered ingredients
    def userIngredients(self):
        global ingr
        global ingr_list
        #
        user_ingr = str(self.ui.recIngr_input.toPlainText())
        user_ingr = user_ingr.lower()
        self.ui.recIngr_input.setText('')
        if len(user_ingr) > 0:
            ingr_list.append(user_ingr)
            text = '\n'.join(ingr_list)
            self.ui.ingrList.setText(text)
            self.ui.directionsEdit.setText(text)#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
        else:
            QMessageBox.about(self, "Error", "Please enter an ingredient for your recipe.")
    
    #deletes ingredient from list of ingredients, if for example an ingredient is entered in misspelled        
    def undoIngr(self):
        global ingr_list
        if len(ingr_list)>0:
            del ingr_list[-1]
            text = '\n'.join(ingr_list)
            self.ui.ingrList.setText(text)
        else:
            QMessageBox.about(self, "Error", "No ingredients found.")

    #opens file dialog, prompting user to load in an image for their recipe
    def openFileNameDialog(self):
        global user_pic
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            self.ui.user_imageDirPath.setText(fileName)
            user_pic = QPixmap(fileName)
            self.ui.selected_pic.setPixmap(user_pic.scaled(recipe_w,recipe_h))
            
    ###########################################################################
    # used to reset the form in case of error or to submit a new recipe without
    # restarting the window. Without this, only one recipe could be entered in 
    # a program instance without re-populating ingredients of the first recipe
    # submitted in the instance
    def subReset(self):
        global user_pic
        global name
        global ingr
        global ingr_list
        global formatted
        
        user_pic = QPixmap(pugFace)
        name = ''
        ingr = ''
        ingr_list = list()
        formatted = False
        
        #clears out all textboxes
        self.ui.recName_displayName.clear()
        self.ui.ingrList.clear()
        self.ui.directionsEdit.clear()
        self.ui.user_imageDirPath.clear()
    # did I miss anything?
    #Needs further testing
    ###########################################################################    

    # evaluates whether or not the inputs have been formatted and saved to the
    # database, using the global boolean 'formatted'. if formatted == True, 
    # closes the window. Clicking before formatting will prompt the user with
    # a dialog box that asks user to verify the inputs and format before saving
    def inputDone(self):
        global formatted
        if formatted == False:
            QMessageBox.about(self, "Save Your Submission", "Please ensure all fields are filled out appropriately, and save your recipe before closing the window.")
        else:
            QMessageBox.about(self, "Recipe Saved!", "You can now close the window.")

    def writeOut(self):
        global name
        global ingr_list
        global directions
        global user_pic
        global formatted
        global fileName
        directions = str(self.ui.directionsEdit.toPlainText())####
        if len(name) < 1:
            QMessageBox.about(self, "Name", "Name your recipe!")
        if len(ingr_list) < 1:
            QMessageBox.about(self, "Ingredients", "Enter some ingredients!")
        if len(directions) < 1:
            QMessageBox.about(self, "Directions", "Enter some directions!")
        if len(fileName) < 1:
            QMessageBox.about(self, "Image", "Include an image with your recipe!")
        p.writeRec(name, ingr_list, directions, user_pic)
        formatted = True
        #self.ui.submitRec_Done.setIcon(QtGui.QIcon(b_close))
        #self.ui.submitRec_Done.setIconSize(QtCore.QSize(249,39))
            
def main():
    app = QApplication(sys.argv)
    window = SubmitUI()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
