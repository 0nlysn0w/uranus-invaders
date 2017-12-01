
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



    def run(self, event):
        #self.pyg.draw.rect(self.screen, (255, 0, 0), [55,50,800,800], 0)
        label = self.myfont.render("Asteroids!", 1, (255,255,0))
        self.screen.blit(label, (100, 100))
        self.screen.blit(self.wheatley, (300, 100))

        self.screen.blit(self.spaceship, (self.height/2, self.width/2))

            
        
    def runextracode() :
        print("runextracode")
