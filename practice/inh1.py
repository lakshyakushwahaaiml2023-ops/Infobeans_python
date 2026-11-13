class Area:
    def __init__(self, l, w):
        self.__l = l
        self.__w = w

    def get_area(self):
        return self.__l * self.__w

    def get_l(self):
        return self.__l
    
    def get_w(self):
        return self.__w
    

class Volume(Area):
    def __init__(self, l, w, h):
        super().__init__(l, w)
        self.__h = h
    

    def get_volume(self):
        return self.__h * self.get_l() * self.get_w()


v = Volume(2,3,5)
print(v.get_volume())