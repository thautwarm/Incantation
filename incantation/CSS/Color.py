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
        self.spec = (color_name, degree, micro_degree)

        types = tuple(map(type, self.spec))
        total_color_name_getter = {
            (str, str, int): lambda: f'{color_name} {degree}-{micro_degree}',
            (str, None.__class__, None.__class__): lambda: color_name
        }.get(types)

        if not total_color_name_getter:
            raise ArgumentError(
                f'requires arguments: (str, str, int) or (str, NoneType, NoneType), get ({", ".join(map(lambda x: x.__name__, types))}).')

        Attribute.__init__(self, 'class', total_color_name_getter())

    def switch(self, degree):
        new = self.empty

        new.name = self.name

        color_name, degree, micro_degree = self.spec

        _len = len(list(filter(lambda x: x is not None, self.spec)))

        if degree is None:
            new.spec = (color_name, None, None)
        else:
            new.spec = (color_name, degree, micro_degree if micro_degree else 1)

        # TODO Lazy reuse to optimize
        new.components = self.check_componnets((*filter(lambda x: x is not None, new.spec), *self.components[_len:]))

        return new

    @property
    def lighten(self) -> 'Color':
        return self.switch('lighten')

    @property
    def darken(self) -> 'Color':
        return self.switch('darken')

    @property
    def accent(self) -> 'Color':
        return self.switch('accent')

    def lighten_by(self, n: int) -> 'Color':
        new = self.empty
        new.name = self.name

        color_name, degree, micro_degree = self.spec

        _len = len(list(filter(lambda x: x is not None, self.spec)))

        degree, micro_degree = self.degree_map['<',
                                               self.degree_map['>', (degree, micro_degree)] + n]

        new.spec = (color_name, degree, micro_degree)

        # TODO Lazy reuse to optimize
        new.components = self.check_componnets((*filter(lambda x: x is not None, new.spec), *self.components[_len:]))

        return new

    def darken_by(self, n: int) -> 'Color':
        return self.lighten_by(-n)

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
