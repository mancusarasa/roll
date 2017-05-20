from pygame.sprite import Group


class VisibleObjects(object):
    '''
    A Singleton that holds all the visible objects from the game.
    The objects are registered in a dictionary that maps
    group_name_string -> pygame.sprite.Group.
    '''
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        super(VisibleObjects, self).__init__()
        self.__groups = {
            'background': Group(),
            'floor': Group(),
            'balls': Group()
        }

    def register_object(self, group, visible_obj):
        '''
        Registers a new visible object in the indicated group.
        @param group string with the group where the object will be registered.
        @oaram visible_obj visible object to be registered.
        @return None.
        '''
        try:
            self.__groups[group].add(visible_obj)
            print 'Registered new {} object!'.format(group)
        except KeyError as e:
            raise RuntimeError('Group {} does not exist'.format(str(e)))

    def get_group(self, group):
        '''
        Gets the requested pygame.sprite.Group.
        @param group string with the requested group.
        @return pygame.sprite.Group instance.
        '''
        try:
            return self.__groups[group]
        except KeyError as e:
            raise RuntimeError('Group {} does not exist'.format(str(e)))
