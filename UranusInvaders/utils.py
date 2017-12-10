import json
class utils:
    def inScreen(pyg, x, y, sprite):
        width = pyg.display.Info().current_w
        height = pyg.display.Info().current_h

        spriteWidth = sprite.get_rect().size[0]
        spriteHeight = sprite.get_rect().size[1]

        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x > width - spriteWidth:
            x = width - spriteWidth
        if y > height - spriteHeight:
            y = height - spriteHeight
        return x, y
    #To call this function you need to call it like this: x, y = utils.move(self.pyg, x, y, self.imagename)

    def move(pyg, x, y, speed):
        #the speed is how many pixels it moves in 1 action
        keys = pyg.key.get_pressed()

        if keys[pyg.K_LEFT] or keys[pyg.K_a]:
            x -= speed

        if keys[pyg.K_RIGHT] or keys[pyg.K_d]:
            x += speed

        if keys[pyg.K_UP] or keys[pyg.K_w]:
           y -= speed

        if keys[pyg.K_DOWN] or keys[pyg.K_s]:
           y += speed
        
        return x, y
        #To call this function you need to call it like this: x, y = utils.move(self.pyg, x, y, self.speed)

    def collisionDetect(firstSprite, firstX, firstY, secondSprite, secondX, secondY):
        firstSpriteX = firstSprite.get_rect().size[0] + firstY
        firstSpriteY = firstSprite.get_rect().size[1] + firstY

        secondSpriteX = secondSprite.get_rect().size[0] + secondX
        secondspriteY = secondSprite.get_rect().size[1] + secondY

        rX = range(firstX, firstSpriteX)
        rY = range(firstY, firstSpriteY)
        if (secondX in rX or secondSpriteX in rX) and (secondY in rY or secondspriteY in rY):
            return True
        else:
            return False

    def load():
        openfile = open("Assets/save.json", "r")
        outfile = json.load(openfile)
        outfile["AmountStarted"] = outfile["AmountStarted"] + 1
        tmp = outfile

        openfile = open("Assets/save.json", "w")
        json.dump(tmp, openfile)
   
    def loadObject(name, minigame = "none"):
        openfile = open("Assets/save.json", "r")
        outfile = json.load(openfile)
        if minigame != "none" and minigame in outfile:
            if name in outfile[minigame]:
                return outfile[minigame][name];

        if name in outfile:
            return outfile[name];

    def saveMinigame(name, valuem, minigame = "none"):
        openfile = open("Assets/save.json", "r")
        outfile = json.load(openfile)
        if minigame != "none":
            if not(minigame in outfile):
                outfile[minigame] = {}
            outfile[minigame][name] = valuem
        else:
            outfile[name] = valuem

        tmp = outfile

        openfile = open("Assets/save.json", "w")
        json.dump(tmp, openfile)