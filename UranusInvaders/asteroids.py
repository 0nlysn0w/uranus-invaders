class Asteroids():
    def __init__(self, pyg, screen):
        print("init asteriods")
        self.pyg = pyg
        self.screen = screen
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.spaceship = pyg.image.load("Assets/spaceship-basic.png")
        self.width = pyg.display.Info().current_w
        self.height = pyg.display.Info().current_h
        self.spaceshipX = self.width/2
        self.spaceshipY = self.height/2
        self.spaceshipWidth = self.spaceship.get_rect().size[0]
        self.spaceshipHeight = self.spaceship.get_rect().size[1]


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
        

        #Makes sure the spaceship can't leave the screen
        self.SpaceShipInScreen()
            
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
