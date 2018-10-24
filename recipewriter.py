'''
Recipe writer: writes recipes to .txt files for recipe suggestions program.
Date: 4/15/2018
'''

import os

path = os.path.dirname(os.path.realpath(__file__))
pathName = str(path) + '\\Recipes\\'
#pathName = 'C:\\Users\\Excelsior\\Desktop\\Work\\CompMind\\Python\\Recipes\\'

scrEggs = '''1. Scramble eggs with a fork in a small bowl adding salt and
pepper to taste. \n 2. Heat a tbsp of oil in a small skillet over low
heat. Once skillet is warm, pour egg mixture in, and mix eggs with a
spatula as they cook until the eggs are cooked. Enjoy!'''

hbEggs = '''1. Fill a pot with an inch of water, insert a steamer
basket. Boil the water on high. \n 2. Once water is boiling, place eggs
in the steamer basket and cover. Steam for 13 minutes. \n 3. Once cooked,
immediately place eggs under cold running water. Enjoy!'''

pbJ = '''1. Lightly toast two slices of bread. \n 2. Spread peanut butter
on one slice, jelly on the other, amounts to taste. \n 3. Put the
sandwich together, shmeared pars together. Enjoy!'''

summHash = '''1. Chop onions into 1/2 inch squares. \n 2. Chop bell
peppers into inch-long strips. \n 3. Cube potatoes into 1/2 inch squares.
\n 4. Whisk eggs in a separate bowl with 1 tbsp paprika, salt and pepper
to taste. Set eggs aside. \n 5. Warm oil in a skillet over medium-low
heat. Once warmed, add in onions, and cook until translucent, roughly
3-4 minutes. \n 6. Add in bellpeppers and cook stirring occasionally for
another 4 minutes. \n 7. Add in potatoes, and cook continuing to stir
until potatoes begin to soften. \n 8. Once potatoes are soft, pour in the
egg mixture and cook, stirring occasionally, until eggs are cooked.
Enjoy!'''

cSSU = '''1. Finely chop fresh dill and set aside. Allow two eggs to
come to room temperature on the counter. \n 2. Slice a tomato into 1/3
inch round, and allow to sit on a paper towel to absorb some of the
juice. \n 3. Warm enough oil to cover the bottom of the skillet over
medium-low heat. Closely place tomato rounds in heated oil, and sprinkle
with pepper to taste and 2/3 of the dill. Cook for 3-4 minutes. \n 4.
Turn the heat down to low and crack the eggs over cooked tomatos, cook
until whites are solid. \n 5. Sprinkle with salt to taste and the last of
dill. Enjoy!'''

r0 = ['Scrambled Eggs', 'eggs', 'salt', 'pepper', 'oil', scrEggs]
r1 = ['Hard Boiled Eggs', 'eggs', hbEggs]
r2 = ['Peanut Butter and Jelly Sandwich', 'bread', 'peanut butter', 'jelly', pbJ]
r3 = ['Summer Hash', 'oil', 'eggs', 'onions', 'bell peppers', 'potatoes', 'paprika', summHash]
r4 = ['Countryside Sunny Side Up', 'eggs', 'oil', 'dill', 'tomato', cSSU]


recipes = [r0, r1, r2, r3, r4]

x = 0
numRec = 0
'''
With the way the program is currently set up, numRec will be reset to 5
every time the program is run, we will have to find a way to work around that
maybe by using another variable.
'''
class recipeWriter:

    def firstRecs(self):
        for lst in recipes:
            outfile = open(str(pathName) + 'recipe' + str(x) + '.txt', 'w')
            outfile.write(lst[-1])
            outfile.close()
            outfile = open(str(pathName) + 'recipe' + str(x) + 'ingredients' + '.txt', 'w')
            x += 1
            for y in range(0, len(lst)-1):
                word = lst[y]
                outfile.write(word + '\n')
        outfile.close()

    def writeRec(self, name, ingr_list, directions, user_pic):
        global numRec
#####################################################################
        number_rec = open(str(pathName) + 'NumberRecipes.txt', 'r')
        numRec = int(number_rec.read())
        number_rec.close()
####################################################################
        outfile = open(str(pathName) + 'recipe' + str(numRec) + '.txt', 'w')
        outfile.write(directions)
        outfile.close()
        outfile = open(str(pathName) + 'recipe' + str(numRec) + 'ingredients' + '.txt', 'w')
        outfile.write(name + '\n')
        for y in range(0, len(ingr_list)):
            word = ingr_list[y]
            outfile.write(word + '\n')
        outfile.close
        pic = user_pic.save(str(pathName) + 'recipe' + str(numRec) + 'pic' + '.jpg', 'JPG')
######################################################################
        numRec += 1
        number_rec = open(str(pathName) + 'NumberRecipes.txt', 'w')
        number_rec.write(str(numRec))
        number_rec.close()
######################################################################
