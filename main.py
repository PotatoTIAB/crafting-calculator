from sys import exit
from itemLib import *
import math

class CraftingCalculator:
    def __init__(self):
        self.recipes = {
            ItemContainer(ItemStack("stick", 2)): ItemContainer(ItemStack("planks")),
            ItemContainer(ItemStack("planks", 2)): ItemContainer(ItemStack("wood")),
            ItemContainer(ItemStack("wooden_sword")): ItemContainer(ItemStack("planks", 2), ItemStack("stick")),
        }


    def calculate(self, cont: (ItemContainer | ItemStack | str | list[str, int | None]), steps: bool = False) -> ItemContainer:
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
        
        if steps:
            _arr = []
            while True:
                _res = self.substitute(cont)
                if _res:
                    _arr.append(_res)
                else:
                    break

            _arr.reverse()
            for _input, _output in _arr:
                print(f"{str(_input)} -> {str(_output)}")
        else:
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
                continue

            _multList = []
            for _recipeItem in _output:
                _foundItem = cont.find(_recipeItem)
                if _foundItem:
                    print(_foundItem.count, _recipeItem.count)
                    _multList.append(math.ceil(_foundItem.count / _recipeItem.count))
                    break
            else:
                continue
            
            _mult = max(i for i in _multList)
            print(f"current mult: {_multList}")
            _input.mult(_mult)
            _output.mult(_mult)
            cont.remove(_output)
            cont.add(_input)
            print(f"current state: {str(cont)}")
            return (_input, _output) 
        return False


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
print(f"Steps to craft {str(itemToCraft)}:")
res = calc.calculate(itemToCraft, True)
print(f"\nTotal raw items required to craft:\n{str(res)}")
