from astropy import units as u
u.imperial.enable()


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
    def __init__(self, name, quantity_str):
        self.name = name
        self.quantity = self._parse_quantity_str(quantity_str)

    def __str__(self):
        return str(self.quantity)+' '+str(self.name)

    def to_dict(self):
        return {self.name: self.quantity}

    def _convert_to_float(self, value_str):
        # handle fractions
        if '/' in value_str and len(value_str) > 1:
            fraction = value_str.split('/')
            numerator = fraction[0]
            denominator = fraction[1]
            return float(numerator)/float(denominator)
        else:
            return float(value_str)

    def _parse_quantity_str(self, quantity_str):
        quantity_str = str(quantity_str)
        try:
            split_index = quantity_str.index(' ')
            value = self._convert_to_float(quantity_str[:split_index])
            unit = u.Unit(quantity_str[split_index+1:])
        except ValueError:
            value = self._convert_to_float(quantity_str)
            unit = u.dimensionless_unscaled
        return value*unit


class Method:
    def __init__(self, steps):
        self.steps = steps

    def __str__(self):
        method = ''
        step_list = [f'{step} {self.steps[step]}\n' for step in self.steps]
        method = method.join(step_list)
        return method
