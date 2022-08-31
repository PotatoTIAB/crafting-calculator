import math
from math import inf
from typing import Any


class ItemStack:
    """
    Item class that supports math operators. Recommended to use with ItemContainer().
    """

    def __init__(self, ID="air", count=1):
        self.id = ID
        self.count = count
    

    def __add__(self, x):
        if isinstance(x, self.__class__):
            if self.id == x.id:
                return self.__class__(self.id, self.count + x.count)
            else:
                raise NotImplementedError("You can't add items of 2 different kinds.")
        
        elif isinstance(x, int) or isinstance(x, float):
            if x % 1 == 0:
                return self.__class__(self.id, self.count + x)
            else:
                raise ValueError(f"{x} is not a whole number.")
        
        else:
            raise TypeError("Invalid summation.")
    

    def __sub__(self, x):
        if isinstance(x, self.__class__):
            if self.id == x.id:
                if self.count <= x.count:
                    return None
                else:
                    return self.__class__(self.id, self.count - x.count)
            else:
                raise NotImplementedError("You can't subtract items of 2 different kinds.")
        
        elif isinstance(x, int) or isinstance(x, float):
            if x % 1 == 0:
                if self.count <= x:
                    return None
                else:
                    return self.__class__(self.id, self.count - x)
            else:
                raise ValueError(f"{x} is not a whole number.")
        
        else:
            raise TypeError("Invalid subtraction.")
        
    
    def __mul__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            _count = math.floor(self.count * x)
            if _count > 0:
                return self.__class__(self.id, _count)
            else:
                return None
        
        else:
            raise TypeError("Invalid multiplication.")
    
    
    def __truediv__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            _count = math.floor(self.count / x)
            if _count > 0:
                return self.__class__(self.id, _count)
            else:
                return None
        
        else:
            raise TypeError("Invalid division.")


    def __mod__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            return self.count % x
    

    def __str__(self):
        return f"{self.count}x {self.id.title()}"



class ItemContainer:
    """
    Container to store ItemStacks().
    """
    
    def __init__(self, *args, size=inf):
        self.contents = []
        self.size = size
        for _item in args:
            self.add(_item)
    

    def __iter__(self):
        for _item in self.contents:
            yield _item
    

    def __str__(self):
        _str = ""
        for _item in self:
            _str += str(_item) + '\n'
        return _str[:-1]


    def add(self, x: (Any | ItemStack), mult: int = 1) -> None:
        """
        Adds the given item or container items to container.
        """

        if isinstance(x, ItemStack):
            x *= mult
            _i = self.index(x)
            if _i < 0:
                self.contents.append(x)
            else:
                self.contents[_i] += x
        
        elif isinstance(x, self.__class__):
            for _item in x:
                self.add(_item, mult=mult)
        
        else:
            raise TypeError(f"You can only add items, not {type(x)}.")
    
    
    def remove(self, x: (Any | ItemStack), mult: int = 1) -> (list[ItemStack] | None):
        """
        Removes the given item or container items from container and return what has been removed.
        Can delete that slot if no items left to remove.
        """
        
        if isinstance(x, ItemStack):
            x *= mult
            _i = self.index(x)
            if _i < 0:
                return None
            else:
                if self.contents[_i].count > x.count:
                    self.contents[_i] -= x
                    return [x]
                else:
                    return [self.contents.pop(_i)]
        
        elif isinstance(x, self.__class__):
            _ret = []
            for _item in x:
                _ret.append(self.remove(_item, mult=mult))
            return _ret
        
        else:
            raise TypeError(f"You can only remove items, not {type(x)}.")


    def index(self, x: (ItemStack | str)) -> int:
        """
        Finds and returns the index number of given item.
        Returns -1 if not found.
        """

        if isinstance(x, ItemStack):
            x = x.id
        
        elif not isinstance(x, str):
            raise TypeError(f"Invalid type: {type(x)}")
        
        _i = 0
        for _item in self.contents:
            if _item.id == x:
                return _i
            _i += 1
        return -1
    
    
    def find(self, x: (ItemStack| str)) -> (ItemStack | None):
        """
        Finds and returns the item inside the container.
        Returns None if not found.
        """

        if isinstance(x, ItemStack):
            x = x.id
        
        elif not isinstance(x, str):
            raise TypeError(f"Invalid type: {type(x)}")
        
        for _item in self.contents:
            if _item.id == x:
                return _item


    def mult(self, mult: int) -> None:
        """
        Multiplies the items inside with the given mult.
        """

        for item in self.contents:
            item *= mult



if __name__ == "__main__":
    pass
