'''
Recipe reader: searches through txt files to find ingredients in a recipe.
Authors: James Witt and Anna Bobcova
Date: 4/17/2018
'''

import random
import os

#pathName = 'C:\\Users\\Excelsior\\Desktop\\Work\\CompMind\\Python\\Recipes\\'
path = os.path.dirname(os.path.realpath(__file__))
pathName = str(path) + '\\Recipes\\'
numRec = 0

class RecipeReader:

    def readRec(self):
        global numRec
        suggestions = list()
        suggestions2 = list()
        ingredient = (str(input("What is your main ingredient?"))).lower()
        for x in range(0,numRec):
            rec = list()
            instr = list()
            with open('recipe' + str(x) + 'ingredients' + '.txt', 'r') as f:
                for line in f:
                    line = line.rstrip()
                    rec.append(line)
            if ingredient in rec:
                infile = open('recipe' + str(x) + '.txt', 'r')
                instruct = infile.read()
                rec.append(instruct)
                suggestions.append(rec)
        if len(suggestions) == 0:
            print("Ingredient not found.")
        else:
            print("Would you like to add another ingredient? (yes/no)")
            ans1 = (str(input())).lower()
            if ans1 == 'yes':
                print("Enter another ingredient")
                ingredient2 = (str(input())).lower()
                for lst in suggestions:
                    if ingredient2 in lst:
                        suggestions2.append(lst)
                    else:
                        print("Ingredient not found")
                if len(suggestions2) != 0:
                    i = random.randint(0, len(suggestions2)-1)
                    print(suggestions2[i][0:-1])
                    print(suggestions2[i][-1])
            if ans1 == 'no':
                i = random.randint(0, len(suggestions)-1)
                print(suggestions[i][0:-1])
                print(suggestions[i][-1])
                
    def recSearch(self, ingr1, ingr2):
        global numRec #Call global numRec
        suggestions = list()
        ######get numRec from file ############
        number_rec = open(str(pathName) + 'NumberRecipes.txt', 'r')
        numRec = int(number_rec.read())
        number_rec.close()
        #########################################################3
        for x in range(0,numRec):
            rec = list()
            with open(str(pathName) + 'recipe' + str(x) + 'ingredients' + '.txt', 'r') as f:
                for line in f:
                    line = line.rstrip()
                    rec.append(line)
                if (ingr1 and ingr2) in rec:
                        suggestions.append(rec)
        i = random.randint(0, len(suggestions)-1)
        return(suggestions[i][0])

    def oneSearch(self, ingr1):
        global numRec #Call global numRec
        suggestions = list()
        ######get numRec from file ############
        number_rec = open(str(pathName) + 'NumberRecipes.txt', 'r')
        numRec = int(number_rec.read())
        number_rec.close()
        #########################################################3
        for x in range(0,numRec):
            rec = list()
            with open(str(pathName) + 'recipe' + str(x) + 'ingredients' + '.txt', 'r') as f:
                for line in f:
                    line = line.rstrip()
                    rec.append(line)
                if (ingr1) in rec:
                    suggestions.append(rec)
        i = random.randint(0, len(suggestions)-1)
        return(suggestions[i][0])

    def getIndex(self, suggs):
        global numRec #call global numRec
        for x in range(0,numRec):
            rec = list()
            with open(str(pathName) + 'recipe' + str(x) + 'ingredients' + '.txt', 'r') as f:
                for line in f:
                    line = line.rstrip()
                    rec.append(line)
            if suggs in rec:
                return x
            
    def diffSearch(self, ingr1, ingr2, index):
        global numRec #call global numRec
        suggestions = list()
        for x in range(0,numRec):
            rec = list()
            with open(str(pathName) + 'recipe' + str(x) + 'ingredients' + '.txt', 'r') as f:
                for line in f:
                    line = line.rstrip()
                    rec.append(line)
                if (ingr1 and ingr2) in rec:
                        suggestions.append(rec)
                elif (ingr1) in rec:
                        suggestions.append(rec)
        i = random.randint(0, len(suggestions)-1)
        while i == index:
            i = random.randint(0, len(suggestions)-1)
        return(suggestions[i][0])        

    def recInst(self, index):
        infile = open(str(pathName) + 'recipe' + str(index) + '.txt', 'r')
        instruct = infile.read()
        return instruct
    '''
        for x in range(0,5):
            rec = list()
            with open('recipe' + str(x) + 'ingredients' + '.txt', 'r') as f:
                for line in f:
                    line = line.rstrip()
                    rec.append(line)
            if suggs in rec:
                infile = open('recipe' + str(x) + '.txt', 'r')
                instruct = infile.read()
                return instruct
    '''
            
    def recIngr(self, index):
        infile = open(str(pathName) + 'recipe' + str(index) + 'ingredients' + '.txt', 'r')
        blah = infile.readline()
        ingree = infile.read()
        return ingree
    '''
        for x in range(0,5):
            rec = list()
            with open('recipe' + str(x) + 'ingredients' + '.txt', 'r') as f:
                for line in f:
                    line = line.rstrip()
                    rec.append(line)
            if suggs in rec:
                infile = open('recipe' + str(x) + 'ingredients' + '.txt', 'r')
                blah = infile.readline()
                ingree = infile.read()
                return ingree
    '''

    def recImg(self, index):
        img = str(pathName) + 'recipe' + str(index) + 'pic' + '.jpg'
        return img
    '''
        for x in range(0,5):
            rec = list()
            with open('recipe' + str(x) + 'ingredients' + '.txt', 'r') as f:
                for line in f:
                    line = line.rstrip()
                    rec.append(line)
            if suggs in rec:
                img = 'recipe' + str(x) + 'pic' + '.jpg'
                return img
    '''
