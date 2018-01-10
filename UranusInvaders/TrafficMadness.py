import Frogger
class TrafficMadness():
    def __init__(self, pyg, screen):
        #Hier kan je plaatjes inladen en in self.{NAAM} zetten en in de run functie dan weer gebruiken, dit zorgt ervoor dat je tijdens het spelen niets hoeft in te laden
        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen
        self.wheatley = pyg.image.load("Assets/Wheatley.png")
        self.m = Frogger.start()

    def background(self):
        if self.m == "return=main":
            return self.m

    def run(self, event):
        m = 0