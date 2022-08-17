class CraftingCalculator:
    def __init__(self):
        self.recipes = {
            "foo": [["bar"]]
        }
        self.items = ["foo", "bar"]

    def recipe(self, arr):
        _result = []
        if not isinstance(arr, list):
            arr = [arr]
        for item in arr:
            if item in self.recipes.keys():
                return self.calculate(self.recipes.get(item)[0])
            else:
                return item
    
    def recc(self, arr):
        pass

calc = CraftingCalculator()
print(calc.calculate("foo"))