import random

class Asteroids():
    def __init__(self, pyg, screen):
        print("init asteriods")
        self.pyg = pyg
        self.screen = screen
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.spaceship = pyg.image.load("Assets/spaceship-basic.png")
        self.asteroidMedium = pyg.image.load("Assets/asteroid_1.png")
        self.asteroidSmall = pyg.image.load("Assets/asteroid_2.png")
        self.width = pyg.display.Info().current_w
        self.height = pyg.display.Info().current_h
        self.spaceshipWidth = self.spaceship.get_rect().size[0]
        self.spaceshipHeight = self.spaceship.get_rect().size[1]
        self.spaceshipX = (self.width - self.spaceshipWidth)/2
        self.spaceshipY = (self.height - self.spaceshipHeight)/2
        self.asteroids = []


    def run(self, event):
        keys = self.pyg.key.get_pressed()

        if keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]:
            self.spaceshipX -= 5

        if keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]:
            self.spaceshipX += 5

        if keys[self.pyg.K_UP] or keys[self.pyg.K_w]:
           self.spaceshipY -= 5

        if keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]:
           self.spaceshipY += 5
        
        asteroid = AsteroidObject(self.pyg).newAsteroid()
        if asteroid != None:
            self.asteroids.append(asteroid);
        

        for x in self.asteroids:
            self.screen.blit(x.asteroid, (x.positionX, x.positionY))
            x.positionY += x.speed

        #Makes sure the spaceship can't leave the screen
        self.SpaceShipInScreen()

        self.screen.blit(self.asteroidSmall, (300, 100))
        self.screen.blit(self.asteroidMedium, (500, 200))
            
        self.screen.blit(self.spaceship, (self.spaceshipX, self.spaceshipY))
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
        return self