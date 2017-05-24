from visible_objects import VisibleObjects

from pygame.sprite import spritecollideany


class CollisionManager(object):
    '''
    An object that handles all the collision in the game.
    '''
    def __init__(self):
        super(CollisionManager, self).__init__()

    def handle_collisions(self):
        '''
        Handles the collisions between all the objects in the game.
        @return None
        '''
        objects = VisibleObjects()
        players = objects.get_group('players')
        floor = objects.get_group('floor')
        for player in players:
            collided = spritecollideany(player, floor)
            if collided is not None:
                player.rect.y -= 1
