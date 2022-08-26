from sys import exit
from itemLib import *

class CraftingCalculator:
    def __init__(self):
        self.recipes = {
            ItemContainer(ItemStack("stick", 2)): ItemContainer(ItemStack("planks")),
            ItemContainer(ItemStack("planks", 2)): ItemContainer(ItemStack("wood")),
        }


    def calculate(self, cont: (ItemContainer | ItemStack | str | list[str, int | None])) -> ItemContainer:
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
        
        while self.substitute(cont):
            pass
        
        return cont


    def recipeSearch(self, itemid: str) -> (tuple[ItemContainer, ItemContainer] | tuple[None, None]):
        for _cont in self.recipes.keys():
            for _item in _cont:
                if _item.id == itemid:
                    return (_cont, self.recipes[_cont])
        return (None, None)


    def substitute(self, cont: ItemContainer):
        for _item in cont:
            _output, _input = self.recipeSearch(_item.id)
            if not _input:
                return False

            _multList = []
            for _recipeItem in _output:
                _foundItem = cont.find(_recipeItem)
                if _foundItem:
                    _multList.append(_foundItem.count / _recipeItem.count)
            
            _mult = max(i for i in _multList)
            print(_mult)

            cont.remove(_output, _mult)
            cont.add(_input, _mult)
            return True


calc = CraftingCalculator()
itemid = input("Enter item you want to craft: ")
itemcount = None
while True:
    try:
        itemcount = int(input("Enter how many items you want to craft: "))
    except ValueError:
        print("Invalid input.")
        continue
    break
itemToCraft = ItemStack(itemid, itemcount)
print(f"Items required to craft {str(itemToCraft)}:")
print(calc.calculate(itemToCraft))
