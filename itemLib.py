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


class ItemContainer:
    pass

if __name__ == "__main__":
    pass