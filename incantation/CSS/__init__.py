from ..abst import Component, Attribute, IIndent, Tag
from ..utils import BiMap
from ..err import ArgumentError


class Color(Attribute):
    degree_map = BiMap([
        *(('accent', i) for i in range(4)),
        *(('darken', i) for i in range(4)),
        (None, None),
        *(('lighten', i) for i in range(5))
    ],
        range(14))

    def __init__(self, color_name: str, degree: str = None, micro_degree: int = None):
        self.color_name = color_name
        self.degree = degree
        self.micro_degree = micro_degree

        types = tuple(map(type, [color_name, degree, micro_degree]))

        total_color_name_getter = {
            (str, str, int): lambda: f'{color_name} {degree}-{micro_degree}',
            (str, None.__class__, None.__class__): lambda: color_name
        }.get(types)

        if not total_color_name_getter:
            raise ArgumentError(
                f'requires arguments: (str, str, int) or (str, NoneType, NoneType), get ({", ".join(map(lambda x: x.__name__, types))}).')

        Attribute.__init__(self, 'class', total_color_name_getter())

    @property
    def lighten(self):
        if self.degree == 'lighten':
            return self
        else:
            return Color(self.color_name, 'lighten', self.micro_degree)

    @property
    def darken(self):
        if self.degree == 'darken':
            return self
        else:
            return Color(self.color_name, 'darken', self.micro_degree)

    @property
    def accent(self):
        if self.degree == 'accent':
            return self
        else:
            return Color(self.color_name, 'accent', self.micro_degree)

    def lighten_by(self, n: int):
        return Color(self.color_name, *(
            self.degree_map['<',
                            (self.degree_map['>',
                                             (self.degree, self.micro_degree)] + n)]))

    def darken_by(self, n: int):
        return Color(self.color_name, *(
            self.degree_map['<',
                            (self.degree_map['>',
                                             (self.degree, self.micro_degree)] - n)]))


class Container(Tag):
    def __init__(self, *components, indent=1):
        cls_attribute = Attribute('class', 'container')
        Tag.__init__(self, 'div', cls_attribute, *components, indent=indent)


class Grid(Attribute):
    """
    the total count of columns of a page is 12.
    """

    def __init__(self, s: int = None, m: int = None, l: int = None):
        param = ' '.join(f'{name}{length}' for name, length in dict(s=s, m=m, l=l).items() if length)
        Attribute.__init__(self, 'class', f'col {param}')


class Offset(Attribute):
    def __init__(self, s: int = None, m: int = None, l: int = None):
        param = ' '.join(f'{name}{length}' for name, length in dict(s=s, m=m, l=l).items() if length)
        Attribute.__init__(self, 'class', f'offset-{param}')


class Push(Attribute):
    def __init__(self, s: int = None, m: int = None, l: int = None):
        param = ' '.join(f'{name}{length}' for name, length in dict(s=s, m=m, l=l).items() if length)
        Attribute.__init__(self, 'class', f'push-{param}')


class Pull(Attribute):
    def __init__(self, s: int = None, m: int = None, l: int = None):
        param = ' '.join(f'{name}{length}' for name, length in dict(s=s, m=m, l=l).items() if length)
        Attribute.__init__(self, 'class', f'pull-{param}')
