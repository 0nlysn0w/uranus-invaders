class TrafficMadness():
    def __init__(self, pyg, screen):
        #Hier kan je plaatjes inladen en in self.{NAAM} zetten en in de run functie dan weer gebruiken, dit zorgt ervoor dat je tijdens het spelen niets hoeft in te laden
        print("init Traffic Madness on Uranus")
        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen
        self.wheatley = pyg.image.load("Assets/Wheatley.png")


    def run(self):
        label = self.myfont.render("Traffic Madness!", 1, (255,255,0))
        quit = self.myfont.render("press ESC to go back to the main menu", 1, (255,255,0))
        self.screen.blit(label, (100, 100))
        self.screen.blit(quit, (100, 500))
        self.screen.blit(self.wheatley, (300, 100))