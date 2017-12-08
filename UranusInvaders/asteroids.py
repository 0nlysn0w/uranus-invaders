import random
from utils import utils
class Asteroids():
    def __init__(self, pyg, screen):
        print("init asteriods")

        spaceshipLoad = utils.loadObject("Spaceship")

        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.spaceship = pyg.image.load("Assets/" + spaceshipLoad + ".png")
        self.asteroidMedium = pyg.image.load("Assets/asteroid_1.png")
        self.asteroidSmall = pyg.image.load("Assets/asteroid_2.png")
        self.width = pyg.display.Info().current_w
        self.height = pyg.display.Info().current_h
        self.spaceshipWidth = self.spaceship.get_rect().size[0]
        self.spaceshipHeight = self.spaceship.get_rect().size[1]
        self.spaceshipX = (self.width - self.spaceshipWidth)/2
        self.spaceshipY = (self.height - self.spaceshipHeight)/2
        self.asteroids = []
        self.highscore = utils.loadObject("highscore", "asteroids")
        self.score = 0

        self.speed = 5


    def background(self):
        asteroid = AsteroidObject(self.pyg).newAsteroid()
        if asteroid != None:
            self.asteroids.append(asteroid);
        
        for x in self.asteroids:
            self.screen.blit(x.asteroid, (x.positionX, x.positionY))
            x.positionY += x.speed

        self.screen.blit(self.spaceship, (self.spaceshipX, self.spaceshipY))
        self.score += 1
        strscore = str(self.score)
        length = len(strscore);
        strzero = "000000000000"
        length = 5-length

        strscore = strzero[0:length] + strscore
        score = self.myfont.render("Score:" + strscore, 1, (255, 255, 0))

        highscore = self.myfont.render("highscore:" + str(self.highscore), 1, (32, 194, 14))
        self.screen.blit(score, (20, 20))
        self.screen.blit(highscore, (self.width - 300, 20))


    def run(self, event):
        self.spaceshipX, self.spaceshipY = utils.move(self.pyg, self.spaceshipX, self.spaceshipY, self.speed)

        #Makes sure the spaceship can't leave the screen

        self.spaceshipX, self.spaceshipY = utils.inScreen(self.pyg, self.spaceshipX, self.spaceshipY, self.spaceship)
        self.SpaceShipInScreen()
            
        self.pyg.event.pump()

    def SpaceShipInScreen(self):
        if self.spaceshipX < 0:
            self.spaceshipX = 0
        if self.spaceshipY < 0:
            self.spaceshipY = 0
        if self.spaceshipX > self.width - self.spaceshipWidth:
            self.spaceshipX = self.width - self.spaceshipWidth
        if self.spaceshipY > self.height - self.spaceshipHeight:
            self.spaceshipY = self.height - self.spaceshipHeight

    def quit(self):
        if self.highscore == None or (self.highscore != None and self.score > self.highscore):
            print("save highscore")
            utils.saveMinigame("highscore", self.score, "asteroids")

class AsteroidObject():
    def __init__(self, pyg):
        self.pyg = pyg
        self._asteroidMedium = pyg.image.load("Assets/asteroid_1.png")
        self._asteroidSmall = pyg.image.load("Assets/asteroid_2.png")
        self.asteroidChance = 20
        self.speed = 5
        self.positionX = 0
        self.positionY = 0
        self.asteroid = ""

    def newAsteroid(self):
        chance = random.randint(0, 500)

        if chance > self.asteroidChance:
            return


        i = random.randint(0, 1)
        self.asteroid = self._asteroidSmall
        if i == 1:
            self.asteroid = self._asteroidMedium

        self.positionX = random.randint(0, self.pyg.display.Info().current_w - self.asteroid.get_rect().size[0])
        self.positionY -= self.asteroid.get_rect().size[1]
        return self