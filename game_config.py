from ConfigParser import ConfigParser


class GameConfig(object):
    '''
    Encapsulates the config of the game.
    '''
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        '''
        Constructor.
        '''
        super(GameConfig, self).__init__()
        self.__config = ConfigParser()
        self.__config.read('config.ini')

    def get(self, section, option):
        '''
        Gets the indicated option from the indicated section.
        @return string with the indicated option from section.
        '''
        return self.__config.get(section, option)
