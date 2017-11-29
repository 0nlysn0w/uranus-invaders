
class Asteroids():
    def __init__(self, pyg, screen):
        print("init asteriods")
        self.pyg = pyg
        self.screen = screen
        self.myfont = self.pyg.font.SysFont("monospace", 30)


    def run(self):
        #self.pyg.draw.rect(self.screen, (255, 0, 0), [55,50,800,800], 0)
        label = self.myfont.render("Asteroids!", 1, (255,255,0))
        self.screen.blit(label, (100, 100))
        
    def runextracode() :
        print("runextracode")
