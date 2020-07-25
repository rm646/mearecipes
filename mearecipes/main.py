import click
import os

from mearecipes.functions import (
    load_recipe,
    store_recipe,
    simplify_ingredients,
    get_recipe_numbers_from_user,
    get_recipe_names_from_file,
)


@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option()
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('Welcome to Mears recipes.')

@cli.command()
def list():
    recipes = get_recipe_names_from_file()
    for i, recipe in enumerate(recipes):
        click.echo(f'{i}. {recipe.name}')

@cli.command()
@click.option('--index', '-i', required=True, type=int)
def show(index):
    recipe = get_recipe_names_from_file()[index]
    print(recipe)

@cli.command()
def shop():
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
    for ingredient in simplified_ingredients:
        ingredients_str += f'\t- {str(ingredient)}\n'
    click.echo(ingredients_str)
