import pygame, sys, math
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
        self.track = pyg.image.load("Assets/track-2.png")
        self.track_mask = pyg.image.load("Assets/track-mask-2.png")
        self.spaceshipWidth = self.spaceship.get_rect().size[0]
        self.spaceshipHeight = self.spaceship.get_rect().size[1]
        self.trackWidth = self.track.get_rect().size[0]
        self.trackHeight = self.track.get_rect().size[1]
        #TODO: from config: start position x and y
        self.spaceshipX = -142
        self.spaceshipY = -487
        self.rotation = 0
        self.speed = 0
        self.max_speed = 20
        self.acceleration = 0.3
        self.state = "menu"
        self.baseRenderer = BaseRenderer(pygame, screen)
        self.option_items = []
        self.test = ""
        self.keys = [False, False, False, False]

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
        #print("")
        if self.state ==  "menu":
            self.menu()
        elif self.state == "game":

            self.speed_controll()

            if self.keys[0] == True:    #Left
                if self.can_move(self.spaceshipX + self.speed, self.spaceshipY):
                    self.spaceshipX += self.speed
                self.rotation = 90
            if self.keys[1] == True:    #Right
                if self.can_move(self.spaceshipX - self.speed, self.spaceshipY):
                    self.spaceshipX -= self.speed
                self.rotation = 270
            if self.keys[2] == True:    #Up
                if self.can_move(self.spaceshipX, self.spaceshipY + self.speed):
                    self.spaceshipY += self.speed
                self.rotation = 0
            if self.keys[3] == True:    #Down
                if self.can_move(self.spaceshipX, self.spaceshipY - self.speed):
                    self.spaceshipY -= self.speed
                self.rotation = 180

            if self.keys[2] and self.keys[0] == True:   #Up Left
                self.rotation = 45

            if self.keys[2] and self.keys[1] == True:   #Up Right
                self.rotation = 315

            if self.keys[3] and self.keys[0] == True:   #Down Left
                self.rotation = 135

            if self.keys[3] and self.keys[1] == True:   #Down Right
                self.rotation = 225

            self.rotatedimg = self.pyg.transform.rotate(self.spaceship, self.rotation)
            self.screen.blit(self.track, (self.width/2 + self.spaceshipX, self.height/2 + self.spaceshipY))
            self.screen.blit(self.rotatedimg, ((self.width / 2) - (self.spaceshipWidth/2), (self.height / 2) - (self.spaceshipHeight/2)))

    def run(self, event):       
        if self.state == "menu":
            s = self.menu()
            return s
        elif self.state == "game":
            i = event
            if i.type == self.pyg.KEYDOWN:
                if i.key == self.pyg.K_LEFT:
                    self.keys[0] = True
                if i.key == self.pyg.K_RIGHT:
                    self.keys[1] = True
                if i.key == self.pyg.K_UP:
                    self.keys[2] = True
                if i.key == self.pyg.K_DOWN:
                    self.keys[3] = True
                if i.key == self.pyg.K_q:
                    print("DEBUG")

            if i.type == self.pyg.KEYUP:
                if i.key == self.pyg.K_LEFT:
                    self.keys[0] = False
                if i.key == self.pyg.K_RIGHT:
                    self.keys[1] = False
                if i.key == self.pyg.K_UP:
                    self.keys[2] = False
                if i.key == self.pyg.K_DOWN:
                    self.keys[3] = False

    def speed_controll(self):
        #print(self.speed)
        if self.speed < 0:
            self.speed = 1

        if self.speed > self.max_speed:
            self.speed = 15

        if any(k == True for k in self.keys):
            self.speed += self.acceleration

        if all(k == False for k in self.keys) and self.speed > 0:
            self.speed -= 0.6

        drag = 0.4
        if self.speed > 1:

            if self.keys[2] and self.keys[0] == True:   #Up Left
                self.speed -= drag

            if self.keys[2] and self.keys[1] == True:   #Up Right
                self.speed -= drag

            if self.keys[3] and self.keys[0] == True:   #Down Left
                self.speed -= drag

            if self.keys[3] and self.keys[1] == True:   #Down Right
                self.speed -= drag

        
        #return

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

    def can_move(self, min_x, min_y):
        #TODO: invert X and Y from start, for now just invert here
        x = math.floor(0 - min_x)
        y = math.floor(0 - min_y)

        #print("x= ", x, ", y= ", y)

        #x and y not outside track.width and height
        if (x < 0 or x > self.trackWidth - 1):
            return False

        if (y < 0 or y > self.trackHeight - 1):
            return False

        #print(self.track_mask.get_at((x, y)))

        if (self.track_mask.get_at((x, y)).a) > 0:
            return True
        else:
            self.speed -= 10
            return False

    def game(self, event):
        keys = self.pyg.key.get_pressed()



        ## North
        #if keys[self.pyg.K_UP] or keys[self.pyg.K_w]:
        #    if self.can_move(self.spaceshipX, self.spaceshipY + self.speed):
        #        self.spaceshipY += self.speed
        #    self.rotation = 0

        ## East
        #if keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]:
        #    if self.can_move(self.spaceshipX - self.speed, self.spaceshipY):
        #        self.spaceshipX -= self.speed
        #    self.rotation = 270

        ## South
        #if keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]:
        #    if self.can_move(self.spaceshipX, self.spaceshipY - self.speed):
        #        self.spaceshipY -= self.speed
        #    self.rotation = 180

        ## West
        #if keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]:
        #    if self.can_move(self.spaceshipX + self.speed, self.spaceshipY):
        #        self.spaceshipX += self.speed
        #    self.rotation = 90

        ## North East
        #if (keys[self.pyg.K_UP] or keys[self.pyg.K_w]) and (keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]):
        #    self.rotation = 315

        ## South East
        #if (keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]) and (keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]):
        #    self.rotation = 225

        ## South West
        #if (keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]) and (keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]):
        #    self.rotation = 135  

        ## North West
        #if (keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]) and (keys[self.pyg.K_UP] or keys[self.pyg.K_w]):
        #    self.rotation = 45


        #for event in self.pyg.event.get():
        #    if event.type == self.pyg.K_UP:
        #        self.test +=1
        #index %= len(self.option_items)