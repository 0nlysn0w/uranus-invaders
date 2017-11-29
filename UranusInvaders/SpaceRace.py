class SpaceRace():
    def __init__(self, pyg, screen):
        #Hier kan je plaatjes inladen en in self.{NAAM} zetten en in de run functie dan weer gebruiken, dit zorgt ervoor dat je tijdens het spelen niets hoeft in te laden
        print("init SpaceRace")
        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen


    def run(self):
        label = self.myfont.render("SpaceRace!", 1, (255,255,0))
        quit = self.myfont.render("press ESC to go back to the main menu", 1, (255,255,0))
        self.screen.blit(label, (100, 100))
        self.screen.blit(quit, (100, 500))