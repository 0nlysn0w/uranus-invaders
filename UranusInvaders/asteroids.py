from BaseRenderer import baseRenderer

class Asteroids(baseRenderer):
    def run(pyg, screen):


        base = baseRenderer(pyg, screen).run()
        if base == "quit":
            return base
        print("test");
