from itemLib import *

class CraftingCalculator:
    def __init__(self):
        self.recipes = {
            ItemContainer(ItemStack("foo")): ItemContainer(ItemStack("bar")),
            ItemContainer(ItemStack("bar")): ItemContainer(ItemStack("foobar")),
        }


    def calculate(self, cont):
        if not isinstance(cont, ItemContainer):
            _item, cont = cont, ItemContainer()
            if isinstance(_item, str):
                _item = ItemStack(_item)
            elif isinstance(_item, list):
                if len(_item) == 2:
                    _item = ItemStack(_item[0], _item[1])
                elif len(cont) == 1:
                    _item = ItemStack(_item[0])
                else:
                    raise ValueError(f"Expected a list with 1 or 2 elements, got {len(cont)} instead.")
            cont.add(_item)
        
        # for item in self.substitute(cont):
        #     _result.append(item)
        
        return cont


    def substitute(self, arr):
        for item in arr:
            if item in self.recipes.keys():
                for res in self.substitute(self.recipes.get(item)[0]):
                    yield res
            else:
                yield item


calc = CraftingCalculator()
print(calc.calculate("foo"))