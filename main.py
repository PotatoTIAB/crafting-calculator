from itemLib import *

class CraftingCalculator:
    def __init__(self):
        self.recipes = {
            ItemContainer(ItemStack("foo")): ItemContainer(ItemStack("bar")),
            ItemContainer(ItemStack("bar")): ItemContainer(ItemStack("foobar")),
        }

    def calculate(self, arr):
        _result = []
        if not isinstance(arr, list):
            arr = [arr]
        for item in self.substitute(arr):
            _result.append(item)
        return _result
    
    def substitute(self, arr):
        for item in arr:
            if item in self.recipes.keys():
                for res in self.substitute(self.recipes.get(item)[0]):
                    yield res
            else:
                yield item


calc = CraftingCalculator()
print(calc.calculate("foobar"))