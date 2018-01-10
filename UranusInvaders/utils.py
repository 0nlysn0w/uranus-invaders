import json
import math
import pygame
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


    def movebugfixed(pyg, x, y, speed, keys):
        if keys[0]:
            x -= speed

        if keys[1]:
            x += speed

        if keys[2]:
           y -= speed

        if keys[3]:
           y += speed
        
        return x, y

    def collisionDetect(firstSprite, firstX, firstY, secondSprite, secondX, secondY):
        firstSpriteX = firstSprite.get_rect().size[0] + firstX
        firstSpriteY = firstSprite.get_rect().size[1] + firstY

        secondSpriteX = secondSprite.get_rect().size[0] + secondX
        secondSpriteY = secondSprite.get_rect().size[1] + secondY
        secondSpriteY = math.ceil(secondSpriteY)

        rX = range(firstX, firstSpriteX)
        rY = range(firstY, firstSpriteY)
        if (secondX in rX or secondSpriteX in rX) and (secondY in rY or secondSpriteY in rY):
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

class MenuItem(pygame.font.Font):
    def __init__(self, text, redir, font=None, font_size=30,
                 font_color=(255, 255, 255), pos_x = 0, pos_y = 0):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.redir = redir
        self.selected = False
 
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_selected(self, selected):
        self.selected = selected
        if selected:
            self.set_font_color((255, 0, 0))
            self.set_italic(True)
        elif not selected:
            self.set_font_color((255, 255, 255))
            self.set_italic(False)

 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
 
    def is_mouse_selection(self, posx, posy):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False

class MenuItemIndex(MenuItem):
    def __init__(self, text, redir, index, font=None, font_size=30,
                 font_color=(255, 255, 255), pos_x = 0, pos_y = 0):
        MenuItem.__init__(self, text, redir, font=None, font_size=30,
                 font_color=(255, 255, 255), pos_x = 0, pos_y = 0)
        self.index = index
