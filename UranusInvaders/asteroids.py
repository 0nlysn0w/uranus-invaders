import random
import pygame
from utils import utils
from GameMenu import MenuItem

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
        self.lifes = 1
        self.updateHighscore = False


    def background(self):
        if self.lifes == 0:
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

            return;
        asteroid = AsteroidObject(self.pyg).newAsteroid()
        if asteroid != None:
            self.asteroids.append(asteroid);
        
        for x in self.asteroids:
            if x.y > self.screenHeight:
                self.asteroids.remove(x)
            self.screen.blit(x.image, (x.x, x.y))
            x.y += x.speed

        self.screen.blit(self.image, (self.x, self.y))
        #score
        self.score += 1
        strscore = str(self.score)
        length = len(strscore);
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

        for x in self.asteroids:
            hit = utils.collisionDetect(x.image, x.x, x.y, self.image, self.x, self.y)
            print(hit)
            if hit == True and self.invinFrames == 0:
                self.lifes -= 1
                self.invinFrames = 60
        
        lifes = self.myfont.render("lifes:" + str(self.lifes), 1, (32, 194, 14))
        self.screen.blit(lifes, (self.screenWidth / 3, 20))


    def run(self, event):
        self.x, self.y = utils.move(self.pyg, self.x, self.y, self.speed)

        #Makes sure the spaceship can't leave the screen

        self.x, self.y = utils.inScreen(self.pyg, self.x, self.y, self.image)
        self.SpaceShipInScreen()
            
        self.pyg.event.pump()

    def SpaceShipInScreen(self):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > self.screenWidth - self.width:
            self.x = self.screenWidth - self.width
        if self.y > self.screenHeight - self.height:
            self.y = self.screenHeight - self.height

    def quit(self):
        if self.highscore == None or (self.highscore != None and self.updateHighscore == True):
            print("save highscore")
            utils.saveMinigame("highscore", self.score, "asteroids")

class AsteroidObject(pygame.sprite.Sprite):
    def __init__(self, pyg):
        pyg.sprite.Sprite.__init__(self)
        self.pyg = pyg
        self._asteroidMedium = pyg.image.load("Assets/asteroid_1.png")
        self._asteroidSmall = pyg.image.load("Assets/asteroid_2.png")
        self.asteroidChance = 20
        self.speed = 5
        self.x = 0
        self.y = 0
        self.image = ""
        self.rect = self.x, self.y

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