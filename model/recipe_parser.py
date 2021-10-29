from os import listdir
from os.path import isdir, lexists
import json


def get_recipes(recipepath):
    files = listdir(recipepath)
    recipes = []

    for file in files:
        fullpath = recipepath + file
        if isdir(fullpath):
            if lexists(fullpath + "/recipe.json"):
                recipes.append(fullpath + "/recipe.json")
    return recipes


def read_recipe(recipe_path):
    f = open(recipe_path, "r")
    lines = f.readlines()
    recipe_dict = json.loads(lines[0])
    return recipe_dict


def get_name(recipe):
    return recipe['name']


def get_servings(recipe):
    return recipe['recipeYield']


def get_ingredients(recipe):
    return recipe['recipeIngredient']


def get_instructions(recipe):
    return recipe['recipeInstructions']


def get_keywords(recipe):
    return recipe['keywords']
