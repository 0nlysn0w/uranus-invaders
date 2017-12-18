import pygame, sys
from utils import MenuItem
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
        self.menu_item = MenuItem("Continue", "game", None, 80)
        self.menu_item.set_position((self.width/2)-(self.menu_item.width/2),(self.height/2))
        self.baseRenderer = BaseRenderer(pygame, screen)

    def background(self):

        if self.state ==  "menu":
            self.menu()
        elif self.state == "game":
            self.game(self.event)
            rotatedimg = self.pyg.transform.rotate(self.spaceship, self.rotation)

            self.screen.blit(self.track, (self.spaceshipX, self.spaceshipY))
            self.screen.blit(rotatedimg, ((self.width / 2) - (self.spaceshipWidth/2), (self.height / 2) - (self.spaceshipHeight/2)))

    def run(self, event):       

        mouseProperties = self.pyg.mouse.get_pos()
        if self.menu_item.is_mouse_selection(mouseProperties[0], mouseProperties[1]):
            self.menu_item.set_font_color((255, 0, 0))
            self.menu_item.set_italic(True)
            if self.pyg.mouse.get_pressed()[0]:
                print("left clicked")
                self.baseRenderer.run("SpaceRace", "SpaceRaceGame")
                #print("1. -->" + self.menu_item.redir)
                #self.state = self.menu_item.redir
                #print("2. -->" + self.state)
                #return "return=" + self.state
                #running = True

        else:
            self.menu_item.set_font_color((255, 255, 255))
            self.menu_item.set_italic(False)
    
    def menu(self):
        self.screen.blit(self.menu_item.label, self.menu_item.position)


        return

    def game(self, event):
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
