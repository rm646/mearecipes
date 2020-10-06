import glob
from itertools import groupby
import os
import yaml

from astropy.units.core import UnitConversionError

from mearecipes.containers import Ingredient, Method, Recipe

RECIPES_FOLDER = f'{os.path.dirname(os.path.abspath(__file__))}/recipes'

def load_recipe(recipe_path):
    with open(recipe_path, 'r') as f:
        content = yaml.safe_load(f)

    name = content['name']
    ingredients = [
        Ingredient(x, content['ingredients'][x]) for x in content['ingredients']
    ]
    method = Method(content['method'])
    return Recipe(name, ingredients, method)


def store_recipe(recipe):
    with open(f'{RECIPES_FOLDER}/{recipe.name}.yaml', 'w') as f:
        store_dict = {
                'name': recipe.name,
                'ingredients': [x.to_dict() for x in recipe.ingredients],
                'method': recipe.method,
        }
        yaml.dump(store_dict, f, default_flow_style=False)


def simplify_ingredients(ingredients):
    get_name = lambda i : i.name
    get_unit = lambda i : i.unit
    ingredients = sorted(ingredients, key=get_name)
    simplified_ingredients = []
    for name, group in groupby(ingredients, key=get_name):
        quantities = [x.quantity for x in group]
        try:
            simplified_ingredient = Ingredient(name, sum(quantities))
            simplified_ingredients.append(simplified_ingredient)
        except UnitConversionError:
            for unit, unit_group in groupby(quantities, key=get_unit):
                simplified_ingredient = Ingredient(name, sum(unit_group))
                simplified_ingredients.append(simplified_ingredient)

    return simplified_ingredients


def get_recipe_numbers_from_user():
    all_numbers = []
    user_message = ("Enter recipe number, multiple comma-separated "
                    "numbers, or nothing if done. \n")
    input_str = input(user_message)
    numbers = input_str.split(',')
    try:
        all_numbers.extend([int(n) for n in numbers])
    except ValueError:
        print('Bad input.')
    return all_numbers


def get_recipe_names_from_file():
    recipes = []
    for rp in glob.glob(f'{RECIPES_FOLDER}/*.yaml'):
        try:
            recipes.append(load_recipe(rp))
        except Exception as e:
            print(f'Failed to load recipe from {rp}:', repr(e), '\n')
    get_name = lambda i : i.name
    recipes = sorted(recipes, key=get_name)
    return recipes
