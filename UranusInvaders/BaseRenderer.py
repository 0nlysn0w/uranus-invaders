import sys

class baseRenderer():
    def __init__(self, pyg, screen):
        print("base")
        self.clock = pyg.time.Clock()
        self.pyg = pyg
        self.screen = screen
    
    def run(self):
        running = True
        global state
        while running:
            
            for i in self.pyg.event.get():

                #this is where the code for pygame is supposed to run
                self.screen.fill((255, 255, 255))

                if i.type == self.pyg.QUIT or (hasattr(i, "key") and getattr(i, "key") == 27):
                    running = False
                    state = "quit"
                    return "quit";
                else:
                    #sets the fps and updates the game screen.
                    self.pyg.display.update()
                    self.clock.tick(30)


