
class Asteroids():
    def __init__(self, pyg, screen):
        print("init asteriods")
        self.pyg = pyg
        self.screen = screen


    def run(self):
        self.pyg.draw.rect(self.screen, (255, 0, 0), [55,50,800,800], 0)
        
    def runextracode() :
        print("runextracode")
