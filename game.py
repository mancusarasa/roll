import pygame

from screen import Screen
from game_config import GameConfig
from event_handler import EventHandler
from clock import Clock
from players import FirstPlayer
from controller import FirstPlayerController
from collision_manager import CollisionManager
from beam_collection import BeamCollection
from time import sleep


class Game(object):
    '''
    Main Game class.
    '''
    def __init__(self):
        super(Game, self).__init__()
        width, height, caption = self.__get_screen_config()
        self.__screen = Screen(width, height, caption)
        self.__players = [FirstPlayer(self)]
        self.__controllers = [FirstPlayerController(self.__players[0])]
        self.__handler = EventHandler()
        self.__beamCollection = BeamCollection()
        self.__clock = Clock()
        self.__game_over = False

    def Run(self):
        '''
        The game's main loop.
        @return None
        '''
        pygame.init()
        self.__main_loop()

    def end_game(self):
        '''
        Indicates the game ended
        @return None
        '''
        self.__game_over = True

    def __main_loop(self):
        '''
        The ACTUAL game's main loop.
        '''
        while not self.__game_over:
            elapsed_time = self.__clock.tick()
            self.__process_input()
            self.__update(elapsed_time)
            self.__render()
            # sleep a few miliseconds to slow down the game
            sleep(0.001)

    def __process_input(self):
        '''
        Processes the players' input.
        @return None.
        '''
        # events generated (such as pygame.quit)
        self.__handler.handle_events()
        # controllers' actions over the players
        for controller in self.__controllers:
            controller.handle_keys()

    def __update(self, time):
        '''
        Updates the game's state.
        @param time elapsed time.
        @return None.
        '''
        # periodic updates on the players
        for player in self.__players:
            player.update()

        # periodic updates on the beams
        self.__beamCollection.update()

        # collisions
        collision_manager = CollisionManager()
        collision_manager.handle_collisions()

    def __render(self):
        '''
        Renders the game's changes on the screen.
        @return None.
        '''
        # Clear the screen
        self.__screen.clear()
        # Update the objects
        self.__screen.update_objects()
        # Show the updated objects
        self.__screen.flip()

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
