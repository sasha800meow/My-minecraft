from random import *
class MapManager():
    def __init__(self):
        self.model = "block.egg"
        self.Stonetexture = "stone.jpg"
        self.Woodtexture = "wood.jpg"
        self.Bricktexture = "brick.jpg"
        self.Leavestexture = "leaves.jpg"
        self.Treetexture = "treetexture.mtl"
        self.tree = "tree.obj"
        self.color = (1,1,1,1)
        self.startNew()

    def addStoneBlock(self,pos):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.Stonetexture))
        self.block.setColor(self.color)
        self.block.setPos(pos)
        self.block.reparentTo(self.land)

    def addWoodBlock(self,pos):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.Woodtexture))
        self.block.setColor(self.color)
        self.block.setPos(pos)
        self.block.reparentTo(self.land)

    def addBrickBlock(self,pos):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.Bricktexture))
        self.block.setColor(self.color)
        self.block.setPos(pos)
        self.block.reparentTo(self.land)

    def addLeavesBlock(self,pos):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.Leavestexture))
        self.block.setColor(self.color)
        self.block.setPos(pos)
        self.block.reparentTo(self.land)

    def addTree(self,pos):
        self.block = loader.loadModel(self.tree)
        self.block.setTexture(loader.loadTexture(self.Leavestexture))
        self.block.setColor(self.color)
        self.block.setPos(pos)
        self.block.reparentTo(self.land)

    def TreeGeneration(self):
        for x in range(15):
            self.Treepos = randint(-50,50)
            self.Treepos.addTree()


    def startNew(self):
        self.land = render.attachNewNode("Land")