import click
import glob
from itertools import groupby
import yaml
from containers import Ingredient, Method, Recipe


def load_recipe(recipe_path):
    with open(recipe_path, 'r') as f:
        try:
            content = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
    name = content['name']
    ingredients = [
        Ingredient(x, content['ingredients'][x]) for x in content['ingredients']
    ]
    method = Method(content['method'])
    return Recipe(name, ingredients, method)


def store_recipe(recipe):
    with open(f'recipes/{recipe.name}.yaml', 'w') as f:
        store_dict = {
                'name': recipe.name,
                'ingredients': [x.to_dict() for x in recipe.ingredients],
                'method': recipe.method,
        }
        yaml.dump(store_dict, f, default_flow_style=False)


def simplify_ingredients(ingredients):
    get_name = lambda i : i.name
    ingredients = sorted(ingredients, key=get_name)
    simplified_ingredients = []
    for name, group in groupby(ingredients, key=get_name):
        quantities = [x.quantity for x in group]
        simplified_ingredients.append(Ingredient(name, sum(quantities)))
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
    recipes = [load_recipe(recipe) for recipe in glob.glob('recipes/*.yaml')]
    get_name = lambda i : i.name
    recipes = sorted(recipes, key=get_name)
    return recipes


@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option()
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('Welcome to Mears recipes.')

@cli.command()
def list_recipes():
    recipes = get_recipe_names_from_file()
    for i, recipe in enumerate(recipes):
        click.echo(f'{i}. {recipe.name}')

@cli.command()
@click.option('--index', '-i', required=True, type=int)
def show_recipe(index):
    recipe = get_recipe_names_from_file()[index]
    print(recipe)

@cli.command()
def select_recipes():
    recipes = get_recipe_names_from_file()
    selected_recipe_numbers = get_recipe_numbers_from_user()
    selected_recipes = [
        recipes[i] for i in selected_recipe_numbers if i<len(recipes)
    ]
    if selected_recipes:
        click.echo('You have selected:')
    else:
        click.echo('No selections.')
    for i, recipe in zip(selected_recipe_numbers, selected_recipes):
        click.echo(f'{i}. {recipe.name}')

    ingredients = []
    _ = [ingredients.extend(recipe.ingredients) for recipe in selected_recipes]
    simplified_ingredients = simplify_ingredients(ingredients)
    ingredients_str = '{:=^40}\n'.format('ALL INGREDIENTS')
    for ingredient in ingredients:
        ingredients_str += f'\t- {str(ingredient)}\n'
    click.echo(ingredients_str)


if __name__ == '__main__':
    cli()
