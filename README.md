# mears-recipes
I had a problem: I wanted to plan meals for the week, then go shopping. But
working out what I needed to buy given a number of recipes with some overlap
was tedious.

This program tries to solve that problem by combining the ingredients of
selected recipes into a shopping list.

# installation

You could clone the repository and install that:
```
git clone https://github.com/rm646/mearecipes.git
cd mearecipes
pip install -e .
```
Or you could try the version published on [TestPyPI](https://test.pypi.org/project/mearecipes/):
```
pip install -i https://test.pypi.org/simple/ mearecipes
```

# usage

View the available recipes with
```bash
$ mearecipes list
```

See a particular recipe's details with
```bash
$ mearecipes show -i <recipe_index>
```
where <recipe_index> is the number from the list printed by the previous
command.

Select recipes and print the resulting shopping list with
```bash
$ mearecipes shop
```

Add your own recipes as .yaml files in the recipes folder.
