import numpy as np
class Map:
    def __init__(self, name="untitled map", size=(200,64), wiew=(50,28), position = (0,0), backcolor = (0,0,0)):
        self.name = name
        self.size = size
        self.wiew = wiew
        self.position = position
        self.backcolor = backcolor
        self.layerBackground = np.ndarray(self.size)

t = Map()
print(t.layerBackground)
