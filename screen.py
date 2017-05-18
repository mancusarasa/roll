import pygame

from game_config import GameConfig
from background import Background


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
        # note: self.__screen is a pygame.Surface instance
        self.__screen = pygame.display.set_mode((width, height))
        self.__background = Background(width, height)
        pygame.display.set_caption(caption)
        self.__visible_objs = [self.__background]

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
        for obj in self.__visible_objs:
            self.__screen.blit(obj.image, obj.rect)

    def register_visible_object(self, obj):
        '''
        Registers a new visible object to be rendered.
        @param obj new visible object.
        '''
        self.__visible_objs.append(obj)

    def flip(self):
        '''
        Redraws all the objects in the screen.
        @return None.
        '''
        pygame.display.flip()
