#!/bin/env python3

from os import listdir
from os.path import isdir, lexists
import json

mypath = "./data/test-recipes/"

def get_recipes(recipepath):
    files = listdir(recipepath)
    recipes = []

    for file in files:
        fullpath = mypath + file
        if isdir(fullpath):
            if lexists(fullpath + "/recipe.json"):
                recipes.append(fullpath + "/recipe.json")
    return recipes

recipes = get_recipes(mypath)

def get_name(recipe_path):
    f = open(recipe_path, "r")
    lines = f.readlines()
    print(lines)
    recipe_dict = json.loads(lines[0])
    print("Name: " + recipe_dict['name'])


for r in recipes:
    print(r)
    get_name(r)
