class utils:
    def inScreen(pyg, x, y, sprite):
        width = pyg.display.Info().current_w
        height = pyg.display.Info().current_h

        spriteWidth = sprite.get_rect().size[0]
        spriteHeight = sprite.get_rect().size[1]

        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x > width - spriteWidth:
            x = width - spriteWidth
        if y > height - spriteHeight:
            y = height - spriteHeight
        return x, y
    #To call this function you need to call it like this: x, y = utils.move(self.pyg, x, y, self.imagename)

    def move(pyg, x, y, speed):
        #the speed is how many pixels it moves in 1 action
        keys = pyg.key.get_pressed()

        if keys[pyg.K_LEFT] or keys[pyg.K_a]:
            x -= speed

        if keys[pyg.K_RIGHT] or keys[pyg.K_d]:
            x += speed

        if keys[pyg.K_UP] or keys[pyg.K_w]:
           y -= speed

        if keys[pyg.K_DOWN] or keys[pyg.K_s]:
           y += speed
        
        return x, y
        #To call this function you need to call it like this: x, y = utils.move(self.pyg, x, y, self.speed)