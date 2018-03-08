from ..utils import default_initializer
from ..abst import Attribute


class Pulse(Attribute):

    @default_initializer
    def __init__(self):
        Attribute.__init__(self, 'class', 'pulse')


IsPulse = Pulse
