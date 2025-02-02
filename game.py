from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        base.camLens.setFov(90)
        map = MapManager()
        for x in range(-50,50):
            for y in range(-50,50):
                map.addLeavesBlock((x,y,0))
base = Game()
base.run()