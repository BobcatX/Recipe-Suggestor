# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:03:06 2018

@author: Jim Witt, Anna Bobcova


"""
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import *
from recipereader import *

# filepath - sets whatever folder this file is in as your working directory
# easier to edit files, or find files when the origram is run on a different
# computer, or moved to a different folderv 
filepath = os.path.dirname(os.path.realpath(__file__))

# Ui file
file = str(filepath)+"\\layout\\Directions.ui"

#------------------------------------------------------------------------------
Ui_MainWindow, QtBaseClass = uic.loadUiType(file)
q = RecipeReader()

w_icon = str(filepath)+"\\layout\\leek-icon.jpg"
background = str(filepath)+"\\layout\\DialogBox.jpg"
b_close = str(filepath)+"\\layout\\button-close.jpg"

#------------------------------------------------------------------------------
###############################################################################
#  RecipeDirections
###############################################################################
#------------------------------------------------------------------------------
class RecipeDirections(QMainWindow):
    def __init__(self):
        global window_title
        
        # Sets up the window itself
        super(RecipeDirections, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(w_icon))
        
        #bg image functionality
        bg = QPixmap(background)
        self.ui.bg_label.setPixmap(bg)
        
        #version+credit
        self.statusBar().showMessage('RecipeSuggestor v 0.2 May 2018: A.Bobcova, J.Witt')
        self.hide()
        
    def displayMainHelp(self):
        help_main = str(filepath)+"\\Help.txt"
        self.ui.win_title.setText('Help')
        text = open(help_main, 'r')
        self.ui.rec_directions.setText(text.read())
        
    def displayAbout(self):
        help_main = str(filepath)+"\\About.txt"
        self.ui.win_title.setText('About Recipe Suggestor')
        text = open(help_main, 'r')
        self.ui.rec_directions.setText(text.read())
    
    def displaySubmitHelp(self):
        help_submit = str(filepath)+"\\Help_Submit.txt"
        self.ui.win_title.setText('Help')
        text = open(help_submit, 'r')
        self.ui.rec_directions.setText(text.read())
        
    #def displayAbout(self):
    
    # Uses index to diplay proper ingredients.    
    def displayDirections(self, index):
        ingredientFile = open(str(filepath)+'\\recipes\\' + 'recipe' + str(index) + 'ingredients' + '.txt', 'r')
        name = ingredientFile.readline()
        self.ui.win_title.setText(name)
        
        directionFile = open(str(filepath)+'\\recipes\\' + 'recipe' + str(index) + '.txt', 'r')
        directions = directionFile.read()
        self.ui.rec_directions.setText(directions)
        
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------        
def main():
    app = QApplication(sys.argv)
    window = RecipeDirections()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
