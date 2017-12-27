import pygame, sys
from utils import MenuItemIndex
from BaseRenderer import BaseRenderer

class SpaceRace():
    def __init__(self, pyg, screen):
        #Hier kan je plaatjes inladen en in self.{NAAM} zetten en in de run functie dan weer gebruiken, dit zorgt ervoor dat je tijdens het spelen niets hoeft in te laden
        print("init SpaceRace")
        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen
        self.width = pyg.display.Info().current_w
        self.height = pyg.display.Info().current_h
        self.spaceship = pyg.image.load("Assets/spaceship-basic.png")
        self.track = pyg.image.load("Assets/track-1.png")
        self.spaceshipWidth = self.spaceship.get_rect().size[0]
        self.spaceshipHeight = self.spaceship.get_rect().size[1]
        self.trackWidth = self.track.get_rect().size[0]
        self.trackHeight = self.track.get_rect().size[1]
        self.spaceshipX = 0#(self.width - self.trackWidth)/2
        self.spaceshipY = 0#(self.height - self.trackHeight)/2
        self.rotation = 0
        self.speed = 10
        self.state = "menu"
        #self.menu_item = MenuItem("Continue", "game", None, 80)
        #self.menu_item.set_position((self.width/2)-(self.menu_item.width/2),(self.height/2))
        self.baseRenderer = BaseRenderer(pygame, screen)
        self.option_items = []
        self.test = ""

        options = ("Continue", "Option", "Exit")

        actions = ("game", "Options", "Exit")

        for index, option in enumerate(options):
            option_item = MenuItemIndex(str(option), actions[index], index, None, 80)

            t_h = len(options) * option_item.height
            pos_x = (self.width / 2) - (option_item.width / 2)
            pos_y = (self.height / 2) - (t_h / 2) + ((index * 2) + index * option_item.height)

            option_item.set_position(pos_x, pos_y)

            self.option_items.append(option_item)

    def background(self):

        if self.state ==  "menu":
            self.menu()
        elif self.state == "game":
            rotatedimg = self.pyg.transform.rotate(self.spaceship, self.rotation)

            #self.screen.blit(self.track, (self.spaceshipX, self.spaceshipY))
            self.screen.blit(self.track, (self.width/2 + self.spaceshipX, self.height/2 + self.spaceshipY))
            self.screen.blit(rotatedimg, ((self.width / 2) - (self.spaceshipWidth/2), (self.height / 2) - (self.spaceshipHeight/2)))

    def run(self, event):       
        if self.state == "menu":
            s = self.menu()
            return s
        elif self.state == "game":
            s = self.game(event)
            return s

    def menu(self):
        for option in self.option_items:
            mouseProperties = self.pyg.mouse.get_pos()
            if option.is_mouse_selection(mouseProperties[0], mouseProperties[1]):
                option.set_selected(True)
                if self.pyg.mouse.get_pressed()[0]:
                    self.state = option.redir
            else:
                option.set_selected(False)
            self.screen.blit(option.label, option.position)

    def can_move(self, x, y):
        print("x= ", x, ", y= ", y)
        
        if y > 0:
            return False
        return True

    def game(self, event):
        keys = self.pyg.key.get_pressed()

        # North
        if keys[self.pyg.K_UP] or keys[self.pyg.K_w]:
            if self.can_move(self.spaceshipX, self.spaceshipY + self.speed):
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


        #for event in self.pyg.event.get():
        #    if event.type == self.pyg.K_UP:
        #        self.test +=1
        #index %= len(self.option_items)