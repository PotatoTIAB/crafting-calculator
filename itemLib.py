import math
from math import inf

class ItemStack:
    def __init__(self, ID="air", count=1):
        self.id = ID
        self.count = count
    

    def __add__(self, x):
        if isinstance(x, self.__class__):
            if self.id == x.id:
                return self.__class__(self.id, self.count + x.count)
            else:
                raise NotImplementedError("You can't add items of 2 different kinds yet.")
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



class ItemContainer:
    def __init__(self, size=inf):
        self.contents = []
        self.size = size
    
    def __add__(self, x):
        if isinstance(x, ItemStack):
            pass
        
    def index(self, x):
        if isinstance(x, ItemStack):
            x = x.id
        elif not isinstance(x, str):
            raise TypeError(f"Invalid type: {type(x)}")
        
        _i = 0
        for item in self.contents:
            if item.id == x:
                return _i
            _i += 1
        return -1

if __name__ == "__main__":
    pass