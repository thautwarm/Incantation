from ..abst import Attribute
from ..utils import BiMap, ClassProperty, doc_printer, default_initializer
from ..err import ArgumentError


class Color(Attribute):
    # TODO enum degree map

    degree_map = BiMap([
        *(('accent', i) for i in range(4)),
        *(('darken', i) for i in range(4)),
        (None, None),
        *(('lighten', i) for i in range(5))
    ],
        range(14))

    @default_initializer
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

    # TODO more default colors
    @ClassProperty
    def red(cls) -> 'Color':
        return Color('red')

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> print(inc.Color('red').darken_by(2))
        """
