import pygame
from utils import utils
from GameMenu import MenuItem
import random

class Asteroids(pygame.font.Font):
    def __init__(self, pyg, screen):
        print("init asteriods")
        pygame.font.Font.__init__(self, None, 30)
        spaceshipLoad = utils.loadObject("Spaceship")

        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen
        self.image = pyg.image.load("Assets/" + spaceshipLoad + ".png")
        self.screenWidth = pyg.display.Info().current_w
        self.screenHeight = pyg.display.Info().current_h
        self.rect = self.image.get_rect()
        self.width = self.rect.size[0]
        self.height = self.rect.size[1]
        self.x = (self.screenWidth - self.width)/2
        self.y = (self.screenHeight - self.height)/2
        self.asteroids = []
        self.highscore = utils.loadObject("highscore", "asteroids")
        self.score = 0
        self.invinFrames = 20
        self.speed = 5
        self.lifes = 3
        self.updateHighscore = False
        self.state = "menu"
        self.items = []
        self.explosion = pyg.image.load("Assets/explosion.png")
        self.exploded = None
        self.keys = [False, False, False, False]

        items = ("Start", "How to play", "Quit")
        redir = ("game", "htp", "quit")
        for index, item in enumerate(items):
            menu_item = MenuItem(item, redir[index])
 
            t_h = len(items) * menu_item.height
            pos_x = (self.screenWidth / 2) - (menu_item.width / 2)
            pos_y = (self.screenHeight / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)


    def background(self):
        if self.state == "menu":
            m = self.menu()
            return m
        elif self.state == "game":
            m = self.gameBackground()
            return m
        elif self.state == "quit":
            return "return=main"

    def run(self, event):
        if self.state == "Menu":
            m = self.menu()
            return m
        else:
            #sets the keys so it won't bug out when you do a keyup event and it doesn't trigger any events anymore
            if event.type == self.pyg.KEYDOWN:
                if event.key == self.pyg.K_LEFT:
                    self.keys[0] = True
                elif event.key == self.pyg.K_RIGHT:
                    self.keys[1] = True
                elif event.key == self.pyg.K_UP:
                    self.keys[2] = True
                elif event.key == self.pyg.K_DOWN:
                    self.keys[3] = True

            if event.type == self.pyg.KEYUP:
                if event.key == self.pyg.K_LEFT:
                    self.keys[0] = False
                elif event.key == self.pyg.K_RIGHT:
                    self.keys[1] = False
                elif event.key == self.pyg.K_UP:
                    self.keys[2] = False
                elif event.key == self.pyg.K_DOWN:
                    self.keys[3] = False

            #Makes sure the spaceship can't leave the screen

            
            self.pyg.event.pump()
        
    def menu(self):
        for item in self.items:
            mouseProperties = self.pyg.mouse.get_pos()
            if item.is_mouse_selection(mouseProperties[0], mouseProperties[1]):
                item.set_font_color((255, 0, 0))
                item.set_italic(True)
                if self.pyg.mouse.get_pressed()[0]:
                    self.state = item.redir

            else:
                item.set_font_color((255, 255, 255))
                item.set_italic(False)
            self.screen.blit(item.label, item.position)


    def SpaceShipInScreen(self):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > self.screenWidth - self.width:
            self.x = self.screenWidth - self.width
        if self.y > self.screenHeight - self.height:
            self.y = self.screenHeight - self.height

    def gameBackground(self):
        self.x, self.y = utils.movebugfixed(self.pyg, self.x, self.y, self.speed, self.keys)
        self.x, self.y = utils.inScreen(self.pyg, self.x, self.y, self.image)

        if self.lifes == 0:
            m = self.gameover()
            if m == "tryagain":
                self.quit()
                self = self.__init__(self.pyg, self.screen)
            elif m == "quit":
                return "return=main"

            return

        asteroid = AsteroidObject(self.pyg, self.score).newAsteroid()
        if asteroid != None:
            self.asteroids.append(asteroid)
        
        removeAsteroids = []
        for x in self.asteroids:
            if x.y > self.screenHeight:
                removeAsteroids.append(x)
            else:
                if x.exploded:
                    x.image = self.pyg.transform.flip(x.image, True, False)
                x.y += x.speed
                self.screen.blit(x.image, (x.x, x.y))

        self.screen.blit(self.image, (self.x, self.y))
        #score
        self.score += 1
        strscore = str(self.score)
        length = len(strscore)
        strzero = "000000000000"
        length = 5-length

        strscore = strzero[0:length] + strscore
        score = self.myfont.render("Score:" + strscore, 1, (255, 255, 0))
        #if highscore is lower than score the highscore also updated
        if self.score > self.highscore:
            self.updateHighscore = True
            self.highscore = self.score

        highscore = self.myfont.render("highscore:" + str(self.highscore), 1, (32, 194, 14))
        self.screen.blit(score, (20, 20))
        self.screen.blit(highscore, (self.screenWidth - 300, 20))
        if self.invinFrames > 0:
            self.invinFrames = self.invinFrames - 1
        if self.exploded != None and self.invinFrames < 15:
            self.asteroids.remove(self.exploded)
            self.exploded = None

        for x in self.asteroids:
            hit = utils.collisionDetect(x.image, x.x, x.y, self.image, self.x, self.y)
            if hit == True and self.invinFrames == 0:
                x.exploded = True
                self.lifes -= 1
                self.invinFrames = 60
                self.explosion = self.pyg.transform.scale(self.explosion, (x.image.get_rect().size[0], x.image.get_rect().size[1]))
                x.image = self.explosion
                self.exploded = x

        for x in removeAsteroids:
            if x == self.exploded:
                self.exploded = None
            self.asteroids.remove(x)
        
        lifes = self.myfont.render("lifes:" + str(self.lifes), 1, (32, 194, 14))
        self.screen.blit(lifes, (self.screenWidth / 3, 20))

    def gameover(self):
            gameover = MenuItem("Game over!", "none", None, 80, (138, 7, 7))
            pos_x = (self.screenWidth / 2) - (gameover.width / 2)
            pos_y = (self.screenHeight / 2) - (gameover.height / 2)
            gameover.set_position(pos_x, pos_y)
            self.screen.blit(gameover.label, gameover.position)

            strscore = str(self.score)
            score = MenuItem("Score: " + strscore, "none", None, 30, (255, 255, 0))
            pos_x = (self.screenWidth / 2) - (score.width / 2)
            pos_y = (self.screenHeight / 4) - (score.height / 2)
            score.set_position(pos_x, pos_y)
            self.screen.blit(score.label, score.position)

            strhighscore = str(self.highscore)
            highscore = MenuItem("Highscore: " + strhighscore, "none", None, 30, (255, 255, 0))
            pos_x = (self.screenWidth / 2) - (highscore.width / 2)
            pos_y = (self.screenHeight / 8 * 3) - (highscore.height / 2)
            highscore.set_position(pos_x, pos_y)
            self.screen.blit(highscore.label, highscore.position)

            tryagain = MenuItem("Try again", "tryagain", None, 30, (255, 255, 255))
            pos_x = (self.screenWidth / 4 ) - (tryagain.width / 2)
            pos_y = (self.screenHeight / 8 * 6) - (tryagain.height / 2)
            tryagain.set_position(pos_x, pos_y)

            quit = MenuItem("Quit", "quit", None, 30, (255, 255, 255))
            pos_x = (self.screenWidth / 4 * 3) - (quit.width / 2)
            pos_y = (self.screenHeight / 8 * 6) - (quit.height / 2)
            quit.set_position(pos_x, pos_y)
            items = []
            items.append(tryagain)
            items.append(quit)
            for item in items:
                mouseProperties = self.pyg.mouse.get_pos()
                if item.is_mouse_selection(mouseProperties[0], mouseProperties[1]):
                    item.set_font_color((255, 0, 0))
                    item.set_italic(True)
                    if self.pyg.mouse.get_pressed()[0]:
                        print("left clicked")
                        print(item.redir)
                        if item.redir == "tryagain":
                            return "tryagain"
                        if item.redir == "quit":
                            return "quit"

                else:
                    item.set_font_color((255, 255, 255))
                    item.set_italic(False)
                self.screen.blit(item.label, item.position)
            


    def quit(self):
        if self.highscore == None or (self.highscore != None and self.updateHighscore == True):
            print("save highscore")
            utils.saveMinigame("highscore", self.score, "asteroids")

class AsteroidObject(pygame.sprite.Sprite):
    def __init__(self, pyg, score):
        speedIncrease = (score // 500)
        print(speedIncrease)
        pyg.sprite.Sprite.__init__(self)
        self.pyg = pyg
        self._asteroidMedium = pyg.image.load("Assets/asteroid_1.png")
        self._asteroidSmall = pyg.image.load("Assets/asteroid_2.png")
        self.asteroidChance = 20
        self.speed = 5 + speedIncrease
        self.x = 0
        self.y = 0
        self.image = ""
        self.rect = self.x, self.y
        self.exploded = False

    def newAsteroid(self):
        chance = random.randint(0, 500)

        if chance > self.asteroidChance:
            return


        i = random.randint(0, 1)
        self.image = self._asteroidSmall
        if i == 1:
            self.image = self._asteroidMedium

        self.x = random.randint(0, self.pyg.display.Info().current_w - self.image.get_rect().size[0])
        self.y -= self.image.get_rect().size[1]
        self.rect = self.image.get_rect()
        return self