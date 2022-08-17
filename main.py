class CraftingCalculator:
    def __init__(self):
        self.recipes = {
            "foo": [["bar"]]
        }
        self.items = ["foo", "bar"]

    def calculate(self, item):
        if item in self.recipes.keys():
            return self.calculate(self.recipes.get(item)[0])
        else:
            return item

calc = CraftingCalculator()
print(calc.calculate("foo"))