from visible_objects import VisibleObjects

from pygame.sprite import spritecollideany


class CollisionManager(object):
    '''
    An object that handles all the collision in the game.
    '''
    def __init__(self):
        super(CollisionManager, self).__init__()
        self.__visible_objs = VisibleObjects()

    def handle_collisions(self):
        '''
        Handles the collisions between all the objects in the game.
        @return None
        '''
        players = self.__visible_objs.get_group('players')
        for player in players:
            collided = False
            # check for collision with floor
            collided = collided or self.__collide_with_floor(player)
            # check for collision with beams
            collided = collided or self.__collide_with_beams(player)
            if not collided:
                player.resume_drop()

    def __collide_with_floor(self, player):
        '''
        Solves the collisions between player and the floor.
        @param player.
        @return None.
        '''
        floor_group = self.__visible_objs.get_group('floor')
        floor = spritecollideany(player, floor_group)
        if floor is not None:
            player.on_collision_with_floor()
        return floor is not None

    def __collide_with_beams(self, player):
        '''
        Solves the collisions between player and the beams.
        @param player.
        @return None.
        '''
        beams = self.__visible_objs.get_group('beams')
        beam = spritecollideany(player, beams)
        if beam is not None:
            player.on_collision_with_beam(beam)
        return beam is not None
