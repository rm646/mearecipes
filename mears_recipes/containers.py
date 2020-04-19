class Recipe:
    def __init__(self, name, ingredients, method):
        self.name = name
        self.ingredients = ingredients
        self.method = method

    def __str__(self):
        title = '{:=^40}\n'.format(self.name)
        ingredients_str = 'INGREDIENTS:\n'
        for ingredient in self.ingredients:
            ingredients_str += f'\t- {str(ingredient)}\n'
        separator = '{:-^40}\n'.format('*')
        method_str = 'METHOD:\n'+str(self.method)+'\n'
        end = '{:=^40}'.format(self.name)
        return title + ingredients_str + separator + method_str + end


class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return str(self.quantity)+' '+str(self.name)

    def combine_two(self, other_ingredient):
        if (self.name != other_ingredient.name):
            raise ValueError("Tried to combine different kinds of ingredient")
        sum = self.quantity + other_ingredient.quantity
        return Ingredient(self.name, sum)

    def to_dict(self):
        return {'name': self.name, 'quantity': self.quantity}


class Method:
    def __init__(self, steps):
        self.steps = steps

    def __str__(self):
        method = ''
        step_list = [f'{step} {self.steps[step]}\n' for step in self.steps]
        print(method.join(step_list))
        method = method.join(step_list)
        return method
