from ..abst import Attribute
from ..utils import default_initializer


class _Depth:
    def __init__(self, depth: int):
        self.depth = depth

    def __str__(self):
        return f'z-depth-{self.depth}'


class ZDepth(Attribute):

    @default_initializer
    def __init__(self, depth: int):
        Attribute.__init__(self, 'class', _Depth(depth))

    def rise(self, z=1):
        new = self.empty

        new.name = self.name
        new.components = self.check_componnets(
            _Depth(comp.depth + z) if isinstance(comp, _Depth) else comp for comp in self.components)

        return new

    def fall(self, z=1):
        new = self.empty

        new.name = self.name
        new.components = self.check_componnets(
            _Depth(comp.depth - z) if isinstance(comp, _Depth) else comp for comp in self.components)

        return new


DoZDepth = ZDepth
