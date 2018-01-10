import pygame

import constants
import platforms
import random
import math
from platforms import Enemy

enemies = []
x = y = 0

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))


        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Assets/background-space-0001.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 400, 550],
                  [platforms.GRASS_MIDDLE, 400, 518],
                  [platforms.GRASS_MIDDLE, 400, 486],
                  [platforms.GRASS_MIDDLE, 400, 454],
                  [platforms.GRASS_MIDDLE, 400, 422],
                  [platforms.GRASS_MIDDLE, 400, 390],
                  [platforms.GRASS_MIDDLE, 400, 358],
                  [platforms.GRASS_MIDDLE, 400, 326],
                  [platforms.GRASS_MIDDLE, 400, 294],
                  [platforms.GRASS_MIDDLE, 400, 262],
                  [platforms.GRASS_MIDDLE, 400, 230],
                  [platforms.GRASS_MIDDLE, 400, 198],
                  [platforms.GRASS_MIDDLE, 400, 166],
                  [platforms.GRASS_MIDDLE, 400, 134],
                  [platforms.GRASS_MIDDLE, 400, 102],
                  [platforms.GRASS_MIDDLE, 400, 70],
                  [platforms.GRASS_MIDDLE, 400, 38],
                  [platforms.GRASS_MIDDLE, 400, 6],
                  [platforms.GRASS_MIDDLE, 400, -26],
                  [platforms.GRASS_MIDDLE, 432, 550],
                  [platforms.GRASS_MIDDLE, 464, 550],
                  [platforms.GRASS_MIDDLE, 496, 550],
                  [platforms.GRASS_MIDDLE, 528, 550],
                  [platforms.GRASS_MIDDLE, 560, 550],
                  [platforms.GRASS_MIDDLE, 592, 550],
                  [platforms.GRASS_MIDDLE, 624, 550],
                  [platforms.GRASS_MIDDLE, 656, 550],
                  [platforms.GRASS_MIDDLE, 688, 550],
                  [platforms.GRASS_MIDDLE, 720, 550],
                  [platforms.GRASS_MIDDLE, 752, 550],
                  [platforms.GRASS_MIDDLE, 784, 550],
                  [platforms.GRASS_MIDDLE, 816, 550],
                  [platforms.GRASS_RIGHT, 848, 550],
                  [platforms.STONE_PLATFORM_LEFT, 1008, 486],
                  [platforms.STONE_PLATFORM_MIDDLE, 1040, 486],
                  [platforms.STONE_PLATFORM_RIGHT, 1072, 486],
                  [platforms.STONE_PLATFORM_LEFT, 1136, 380],
                  [platforms.STONE_PLATFORM_MIDDLE, 1168, 380],
                  [platforms.STONE_PLATFORM_RIGHT, 1200, 380],
                  [platforms.STONE_PLATFORM_LEFT, 1680, 348],
                  [platforms.STONE_PLATFORM_MIDDLE, 1712, 348],
                  [platforms.STONE_PLATFORM_RIGHT, 1744, 348],
                  [platforms.GRASS_LEFT, 1904, 550],
                  [platforms.GRASS_MIDDLE, 1904, 518],
                  [platforms.GRASS_MIDDLE, 1904, 486],
                  [platforms.GRASS_MIDDLE, 1936, 550],
                  [platforms.GRASS_MIDDLE, 1968, 550],
                  [platforms.GRASS_MIDDLE, 2000, 518],
                  [platforms.GRASS_MIDDLE, 2000, 486],
                  [platforms.GRASS_MIDDLE, 2000, 550],
                  [platforms.GRASS_MIDDLE, 2032, 550],
                  [platforms.GRASS_MIDDLE, 2064, 550],
                  [platforms.GRASS_MIDDLE, 2096, 550],
                  [platforms.GRASS_MIDDLE, 2096, 518],
                  [platforms.GRASS_MIDDLE, 2096, 486],
                  [platforms.GRASS_MIDDLE, 2128, 550],
                  [platforms.GRASS_MIDDLE, 2160, 550],
                  [platforms.GRASS_MIDDLE, 2192, 550],
                  [platforms.GRASS_MIDDLE, 2192, 518],
                  [platforms.GRASS_MIDDLE, 2192, 486],
                  [platforms.GRASS_MIDDLE, 2224, 550],
                  [platforms.GRASS_MIDDLE, 2256, 550],
                  [platforms.GRASS_MIDDLE, 2288, 550],
                  [platforms.GRASS_MIDDLE, 2288, 518],
                  [platforms.GRASS_MIDDLE, 2288, 486],
                  [platforms.GRASS_RIGHT, 2320, 550],
                  [platforms.GRASS_LEFT, 2400, 454],
                  [platforms.GRASS_MIDDLE, 2432, 454],
                  [platforms.GRASS_RIGHT, 2464, 454],
                  [platforms.GRASS_LEFT, 2600, 370],
                  [platforms.GRASS_MIDDLE, 2632, 370],
                  [platforms.GRASS_RIGHT, 2664, 370],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1250
        block.rect.y = 380
        block.boundary_left = 1250
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving Enemy
        block = platforms.MovingEnemy(Enemy)
        block.rect.x = 1250
        block.rect.y = 180
        block.boundary_left = 1250
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Assets/background-space-0001.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        self.surface = pygame.image.load("Assets/dirt-surface-0001.png").convert()

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 30, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 370, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 440, 550],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
