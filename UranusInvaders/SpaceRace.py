import pygame, sys
from utils import MenuItemIndex
from BaseRenderer import BaseRenderer

class SpaceRaceGame():
    def __init__(self, pyg, screen):
        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen
        self.spaceship = pyg.image.load("Assets/spaceship-basic.png")
        self.track = pyg.image.load("Assets/track-1.png")
        self.width = pyg.display.Info().current_w
        self.height = pyg.display.Info().current_h
        self.spaceshipWidth = self.spaceship.get_rect().size[0]
        self.spaceshipHeight = self.spaceship.get_rect().size[1]
        self.spaceshipX = (self.width - self.spaceshipWidth)/2
        self.spaceshipY = (self.height - self.spaceshipHeight)/2
        self.rotation = 0
        self.speed = 10

    def background(self):

        rotatedimg = self.pyg.transform.rotate(self.spaceship, self.rotation)

        self.screen.blit(self.track, (self.spaceshipX, self.spaceshipY))
        self.screen.blit(rotatedimg, ((self.width / 2) - (self.spaceshipWidth/2), (self.height / 2) - (self.spaceshipHeight/2)))

    def run(self, event):
        keys = self.pyg.key.get_pressed()

        #print(keys)

        # North
        if keys[self.pyg.K_UP] or keys[self.pyg.K_w]:
           self.spaceshipY += self.speed
           self.rotation = 0

        # East
        if keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]:
            self.spaceshipX -= self.speed
            self.rotation = 270

        # South
        if keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]:
           self.spaceshipY -= self.speed
           self.rotation = 180

        # West
        if keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]:
            self.spaceshipX += self.speed
            self.rotation = 90

        # North East
        if (keys[self.pyg.K_UP] or keys[self.pyg.K_w]) and (keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]):
            self.rotation = 315

        # South East
        if (keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]) and (keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]):
           self.rotation = 225

        # South West
        if (keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]) and (keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]):
           self.rotation = 135  

        # North West
        if (keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]) and (keys[self.pyg.K_UP] or keys[self.pyg.K_w]):
           self.rotation = 45

class SpaceRace():
    def __init__(self, pyg, screen):
        #Hier kan je plaatjes inladen en in self.{NAAM} zetten en in de run functie dan weer gebruiken, dit zorgt ervoor dat je tijdens het spelen niets hoeft in te laden
        print("init SpaceRace")
        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen
        self.width = pyg.display.Info().current_w
        self.height = pyg.display.Info().current_h
        self.state = "menu"
        #self.menu_item = MenuItem("Continue", "game", None, 80)
        #self.menu_item.set_position((self.width/2)-(self.menu_item.width/2),(self.height/2))
        self.baseRenderer = BaseRenderer(pygame, screen)
        self.option_items = []
        self.test = ""

        options = ("Continue", "Option", "Exit")

        actions = ("StartGame", "Options", "Exit")

        for index, option in enumerate(options):
            option_item = MenuItemIndex(str(option), option, index, None, 80)

            t_h = len(options) * option_item.height
            pos_x = (self.width / 2) - (option_item.width / 2)
            pos_y = (self.height / 2) - (t_h / 2) + ((index * 2) + index * option_item.height)

            option_item.set_position(pos_x, pos_y)

            self.option_items.append(option_item)



    def run(self, event):       
        # laatst bezig geweest met het toevoegen van een index aan eenmenu item. dit om bij te houden welk item er geselecteerd is
        keyinput = self.pyg.key.get_pressed()
        mouseProperties = self.pyg.mouse.get_pos()
        self.screen.fill((0, 0, 0))
        for option in self.option_items:
            if option.is_mouse_selection(mouseProperties[0], mouseProperties[1]):
                option.set_selected(True)
                if self.pyg.mouse.get_pressed()[0]:
                    print("left clicked")
                    self.baseRenderer.run("SpaceRace", "SpaceRaceGame")
                    running = False
            else:
                option.set_selected(False)
            index = str(option.index)
            print(str(option.label) + index)
            print(self.test)
            #option.label += " " + index
            self.screen.blit(option.label, option.position)

        #for event in self.pyg.event.get():
        #    if event.type == self.pyg.K_UP:
        #        self.test +=1
        #index %= len(self.option_items)