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
        balls = objects.get_group('balls')
        floor = objects.get_group('floor')
        for ball in balls:
            collided = spritecollideany(ball, floor)
            if collided is not None:
                ball.rect.y -= 1
