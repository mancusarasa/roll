from beam import Beam


class BeamCollection(object):
    '''
    The collection of beams.
    '''
    def __init__(self, beams_count=3):
        '''
        Constructor
        '''
        super(BeamCollection, self).__init__()
        for i in range(beams_count):
            b = Beam(60, 20, i*100 + 100, i*100 +100)
        
