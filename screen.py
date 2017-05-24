import pygame

from game_config import GameConfig
from visible_objects import VisibleObjects
from background import Background
from floor import Floor


class Screen(object):
    '''
    The game's main screen.
    '''
    def __init__(self, width, height, caption):
        '''
        Constructor.
        @param width the screen's width.
        @param height the screen's height.
        @param caption the screen's caption.
        '''
        super(Screen, self).__init__()
        self.width = width
        self.height = height
        self.__screen = pygame.display.set_mode((width, height))
        self.__background = Background(width, height)
        self.__floor = Floor(width, height/4, x=0, y=height*3/4)
        pygame.display.set_caption(caption)

    def clear(self):
        '''
        Clears the screen.
        @return None.
        '''
        self.__screen.fill((0, 0, 0))

    def update_objects(self):
        '''
        Updates all the visible objects in the screen.
        @return None.
        '''
        # first, redraw the background
        self.__screen.blit(self.__background.image, self.__background.rect)
        # then, redraw the floor
        self.__screen.blit(self.__floor.image, self.__floor.rect)
        # finally, redraw the players
        visible_objs = VisibleObjects()
        players = visible_objs.get_group('players')
        for player in players:
            self.__screen.blit(player.image, player.rect)

    def flip(self):
        '''
        Redraws all the objects in the screen.
        @return None.
        '''
        pygame.display.flip()
