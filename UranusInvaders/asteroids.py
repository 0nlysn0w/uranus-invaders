
class Asteroids():
    def __init__(self, pyg, screen):
        print("init asteriods")
        self.pyg = pyg
        self.screen = screen
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.wheatley = pyg.image.load("Assets/Wheatley.png")
        self.spaceship = pyg.image.load("Assets/spaceship-basic.png")
        self.width = pyg.display.Info().current_w
        self.height = pyg.display.Info().current_h
        self.spaceshipX = self.width/2
        self.spaceshipY = self.height/2



    def run(self, event):
        #self.pyg.draw.rect(self.screen, (255, 0, 0), [55,50,800,800], 0)
        label = self.myfont.render("Asteroids!", 1, (255,255,0))
        self.screen.blit(label, (100, 100))
        self.screen.blit(self.wheatley, (300, 100))
        keys = self.pyg.key.get_pressed()

        if keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]:
            self.spaceshipX -= 5

        if keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]:
            self.spaceshipX += 5

        if keys[self.pyg.K_UP] or keys[self.pyg.K_w]:
           self.spaceshipY -= 5

        if keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]:
           self.spaceshipY += 5
            
        print(self.spaceshipX, self.spaceshipY) 
        self.screen.blit(self.spaceship, (self.spaceshipX, self.spaceshipY))
        self.pyg.event.pump()
