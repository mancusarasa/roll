import pygame

from game_config import GameConfig


class Screen(object):
    '''
    The game's main screen.
    '''
    def __init__(self):
        '''
        Constructor.
        '''
        super(Screen, self).__init__()
        width, height, caption = self.__get_screen_config()
        # nota: self.__screen es una instancia de la clase pygame.Surface
        self.__screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.__visible_objs = []

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

    def __get_screen_config(self):
        '''
        Gets the screen configurable options.
        @return tuple with (width, height, caption).
        '''
        config = GameConfig()
        width = int(config.get('screen', 'width'))
        height = int(config.get('screen', 'height'))
        caption = config.get('screen', 'caption')
        return width, height, caption
