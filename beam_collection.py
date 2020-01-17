from beam import Beam
from game_config import GameConfig
from random import randint


class BeamCollection(object):
    '''
    The collection of beams.
    '''
    def __init__(self, beams_count=10):
        '''
        Constructor
        '''
        super(BeamCollection, self).__init__()
        self.beams = []
        config = GameConfig()
        width = int(config.get('beams', 'width'))
        height = int(config.get('beams', 'height'))
        screen_width = int(config.get('screen', 'width'))
        screen_height = int(config.get('screen', 'height'))

        for i in range(beams_count):
            x_offset = randint(0, screen_width)
            y_offset = i*(screen_height/beams_count)
            self.beams.append(Beam(width, height, x_offset, y_offset))

    def update(self):
        for beam in self.beams:
            beam.update()
