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