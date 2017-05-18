import pygame
from pygame import locals

from controller import FirstPlayerController


class EventHandler(object):
    '''
    Handles all the events of the game.
    '''
    def __init__(self, screen, player_one):
        '''
        Class constructor.
        @param screen.
        @param player_one first player.
        '''
        super(EventHandler, self).__init__()
        self.__clock = pygame.time.Clock()
        self.__screen = screen
        self.__screen.register_visible_object(player_one.ball)
        self.__controllers = [FirstPlayerController(player_one)]

    def main_loop(self):
        '''
        Handles the new events until the game is quit, updating
        the changes in the screen.
        @param screen where the changes will be rendered.
        @return None.
        '''
        while True:
            time = self.__clock.tick()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    return
            for controller in self.__controllers:
                controller.take_action(keys)

            # Clear the screen
            self.__screen.clear()
            # Update the objects
            self.__screen.update_objects()
            # Show the updated objects
            self.__screen.flip()
