# Game of Joost Stam
import pygame, sys, math, time
from utils import MenuItemIndex, utils, TimerObject
from BaseRenderer import BaseRenderer

class SpaceRace():
    def __init__(self, pyg, screen):
        # General settings
        print("init SpaceRace")
        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen
        self.width = pyg.display.Info().current_w
        self.height = pyg.display.Info().current_h
        self.state = "menu"

        # Loading the items on screen and do some calculations
        self.spaceship = pyg.image.load("Assets/spaceship-basic.png")
        self.track = pyg.image.load("Assets/track-2.png")
        self.track_mask = pyg.image.load("Assets/track-2.png")
        self.startfinish_checker = pyg.image.load("Assets/startfinish.png")
        self.can_lap_checker = pyg.image.load("Assets/startfinish.png")
        self.startfinish = pyg.image.load("Assets/chequered.png")
        self.spaceshipWidth = self.spaceship.get_rect().size[0]
        self.spaceshipHeight = self.spaceship.get_rect().size[1]
        self.trackWidth = self.track.get_rect().size[0]
        self.trackHeight = self.track.get_rect().size[1]

        # Space ship start location
        self.spaceshipX = -142
        self.spaceshipY = -487

        # Space ship starting variables
        self.rotation = 0
        self.speed = 0
        self.max_speed = 20
        self.acceleration = 0.3
        self.keys = [False, False, False, False]

        # Things with timers and laps
        self.start_time = 0
        self.laptime = TimerObject()
        self.bestlaptime = TimerObject("00:00:000", 0)
        self.laps = 0
        self.can_lap = False

        # Menu items
        self.option_items = []
        options = ("Continue", "Exit")
        actions = ("game", "quit")

        for index, option in enumerate(options):
            option_item = MenuItemIndex(str(option), actions[index], index, None, 80)

            t_h = len(options) * option_item.height
            pos_x = (self.width / 2) - (option_item.width / 2)
            pos_y = (self.height / 2) - (t_h / 2) + ((index * 2) + index * option_item.height)

            option_item.set_position(pos_x, pos_y)
            self.option_items.append(option_item)

    # 30FPS masterrace
    def background(self):
        if self.state ==  "menu":
            self.menu()
        elif self.state == "quit":
            return "return=main"
        elif self.state == "game":
            # Well, check every frame
            self.speed_controll()

            # React to button presses of the arrow keys and do something with it
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

            # Draw track
            self.rotatedimg = self.pyg.transform.rotate(self.spaceship, self.rotation)
            self.screen.blit(self.track, (self.width/2 + self.spaceshipX, self.height/2 + self.spaceshipY))

            # Track markers
            startfinishX = 454 + self.spaceshipX
            startfinishY = 787 + self.spaceshipY

            can_lap_checkerX = 2221 + self.spaceshipX
            can_lap_checkerY = 787 + self.spaceshipY

            # Draw track markers
            # The checkers are invisible
            self.screen.blit(self.startfinish_checker, (startfinishX, startfinishY))
            self.screen.blit(self.can_lap_checker, (can_lap_checkerX, can_lap_checkerY))
            # This one is chequered xD
            self.screen.blit(self.startfinish, (startfinishX, startfinishY))

            # Draw rotated space ship on top of everything
            self.screen.blit(self.rotatedimg, ((self.width / 2) - (self.spaceshipWidth/2), (self.height / 2) - (self.spaceshipHeight/2)))
            
            # Check if markers have been hit
            startfinish_hit = utils.collisionDetect(self.startfinish_checker, startfinishX, startfinishY, self.rotatedimg, (self.width / 2) - (self.spaceshipWidth/2), (self.height / 2) - (self.spaceshipHeight/2), self.speed)
            can_lap_checker_hit = utils.collisionDetect(self.can_lap_checker, can_lap_checkerX, can_lap_checkerY, self.rotatedimg, (self.width / 2) - (self.spaceshipWidth/2), (self.height / 2) - (self.spaceshipHeight/2), self.speed)
            
            # Check if space ship passed the lap marker halfway the lap
            if can_lap_checker_hit == True:
                self.can_lap = True

            # Calculate the lap time
            self.laptime = utils.get_elapsed_time(self.start_time)

            # Check if space ship passed start finish and do stuf like reset the laptime an add one lap to the counter
            if startfinish_hit == True and self.can_lap == True:
                if self.laptime.millis < self.bestlaptime.millis or self.bestlaptime.millis == 0:
                    self.bestlaptime.millis = self.laptime.millis
                    self.bestlaptime.disp_time = self.laptime.disp_time
                self.start_time = 0
                self.laps += 1
                self.can_lap = False

            # Draw lap information
            self.disp_laptime = self.myfont.render("Time: " + self.laptime.disp_time, 1, (255, 255, 0))
            self.disp_bestlaptime = self.myfont.render("Highscore: " + self.bestlaptime.disp_time, 1, (225, 225, 0))
            self.disp_laps = self.myfont.render("Laps: " + str(self.laps), 1, (225, 225, 0))

            self.screen.blit(self.disp_laptime, (20, 20))
            self.screen.blit(self.disp_bestlaptime, (20, 60))
            self.screen.blit(self.disp_laps, (20, 100))

    def run(self, event):       
        if self.state == "menu":
            s = self.menu()
            return s
        elif self.state == "game":
            i = event
            # Detect if and which button(s) is/are pressed
            if i.type == self.pyg.KEYDOWN:
                if self.start_time == 0:
                    # Start the timer when you start moving
                    self.start_time = utils.start_timer()

                if i.key == self.pyg.K_LEFT:
                    self.keys[0] = True
                if i.key == self.pyg.K_RIGHT:
                    self.keys[1] = True
                if i.key == self.pyg.K_UP:
                    self.keys[2] = True
                if i.key == self.pyg.K_DOWN:
                    self.keys[3] = True

            if i.type == self.pyg.KEYUP:
                if i.key == self.pyg.K_LEFT:
                    self.keys[0] = False
                if i.key == self.pyg.K_RIGHT:
                    self.keys[1] = False
                if i.key == self.pyg.K_UP:
                    self.keys[2] = False
                if i.key == self.pyg.K_DOWN:
                    self.keys[3] = False
    
    # Manage the speed of the space ship
    def speed_controll(self):
        drag = 0.5

        # Prevents the speed from dipping below 0
        if self.speed < 0:
            self.speed = 1

        # Prevents the speed from exceeding the speed limit
        if self.speed > self.max_speed:
            self.speed = self.max_speed

        # If there is movement in any direction
        if any(k == True for k in self.keys):
            self.speed += self.acceleration

        # If there is no movement at all
        if all(k == False for k in self.keys) and self.speed > 0:
            self.speed -= drag

        if self.speed > 1:

            if self.keys[2] and self.keys[0] == True:   #Up Left
                self.speed -= drag

            if self.keys[2] and self.keys[1] == True:   #Up Right
                self.speed -= drag

            if self.keys[3] and self.keys[0] == True:   #Down Left
                self.speed -= drag

            if self.keys[3] and self.keys[1] == True:   #Down Right
                self.speed -= drag
    
    # Manage the menu clicks
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

    # Decides if the character is allowed to move
    def can_move(self, min_x, min_y):
        x = math.floor(0 - min_x)
        y = math.floor(0 - min_y)

        #x and y not outside track.width and height
        if (x < 0 or x > self.trackWidth - 1 - self.speed):
            return False

        if (y < 0 or y > self.trackHeight - 1 - self.speed):
            return False

        # Don't move if transparent
        if (self.color_code(x, y).a) > 0:
            return True
        else:
            self.speed -= 10
            return False

    # Return the RGBA value of a pixel at a given location
    def color_code(self, x, y):
        if str(x)[0] == "-":
            x = math.floor(0 - x)
            y = math.floor(0 - y)
        color_code = self.track_mask.get_at((x,y))
        return color_code
