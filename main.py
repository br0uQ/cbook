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


def get_values(recipe_path):
    f = open(recipe_path, "r")
    lines = f.readlines()
    recipe_dict = json.loads(lines[0])
    get_name(recipe_dict)
    get_servings(recipe_dict)
    get_ingredients(recipe_dict)
    get_instructions(recipe_dict)
    get_keywords(recipe_dict)


def get_name(recipe):
    print("Name: " + recipe['name'])


def get_servings(recipe):
    print("Servings: " + str(recipe['recipeYield']))


def get_ingredients(recipe):
    print("Ingredients: ")
    print(recipe['recipeIngredient'])


def get_instructions(recipe):
    print("Instructions: ")
    print(recipe['recipeInstructions'])


def get_keywords(recipe):
    print("Keywords: ")
    print(recipe['keywords'])


for r in recipes:
    print(r)
    get_values(r)
