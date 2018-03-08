from ..abst import Component, Attribute, RecursiveIndent, Tag
from ..err import ArgumentError
from ..utils import doc_printer, default_initializer


class Container(Tag):
    @default_initializer
    def __init__(self, *components, indent=1):
        cls_attribute = Attribute('class', 'container')
        Tag.__init__(self, 'div', cls_attribute, *components, indent=indent)

    @doc_printer
    def help(self):
        """
        create a container for the page.
        >>> import incantation as inc
        >>> c1 = inc.Container(...)
        >>> c2 = inc.Container()

        """


class Div(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'div', *components)

    @doc_printer
    def help(self):
        """
        a single object which represents `div` in XML.
        """


C = Div


class Grid(Attribute):

    @default_initializer
    def __init__(self, s: int = None, m: int = None, l: int = None):
        if not s and not m and not l:
            raise ArgumentError('Require at least one keyword argumnet in (`s`, `m`, `l`).')
        param = ' '.join(f'{name}{length}' for name, length in dict(s=s, m=m, l=l).items() if length)
        Attribute.__init__(self, 'class', f'col {param}')

    @doc_printer
    def help(self):
        """
        the total count of columns of a page is 12.
        >>> import incantation as inc
        >>> container = inc.Container(inc.Grid(s=2))  # set the grid of container
        >>> container = inc.Container()
        >>> container.append(inc.Grid(s=2), inc.Color('red').darken_by(5))
        """


DoGrid = Grid


class Offset(Attribute):
    @default_initializer
    def __init__(self, s: int = None, m: int = None, l: int = None):
        if not s and not m and not l:
            raise ArgumentError('Require at least one keyword argumnet in (`s`, `m`, `l`).')
        param = ' '.join(f'{name}{length}' for name, length in dict(s=s, m=m, l=l).items() if length)
        Attribute.__init__(self, 'class', f'offset-{param}')

    @doc_printer
    def help(self):
        """
        `offset, push, pull`:
        >>> import incantation as inc
        >>> offset = inc.Offset(s=3)
        >>> pull = inc.Offset(m=3)
        >>> push = inc.Offset(l=3)
        >>> for each in (offset, pull, push):
        >>>     table = inc.Table(inc.Offset(s=3),
        >>>                       source=[[1, 2, 3, 4], [2, 3, 4, 5]], columns=range(4), index=range(2))
        >>>     print(table)
        """


DoOffset = Offset


class Push(Attribute):
    @default_initializer
    def __init__(self, s: int = None, m: int = None, l: int = None):
        if not s and not m and not l:
            raise ArgumentError('Require at least one keyword argumnet in (`s`, `m`, `l`).')
        param = ' '.join(f'{name}{length}' for name, length in dict(s=s, m=m, l=l).items() if length)
        Attribute.__init__(self, 'class', f'push-{param}')

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> inc.Form(inc.Push(10),
        >>>          inc.InputField(name='username', id='username', type='text'))
        """


DoPush = Push


class Pull(Attribute):
    help = Offset.help

    @default_initializer
    def __init__(self, s: int = None, m: int = None, l: int = None):
        if not s and not m and not l:
            raise ArgumentError('Require at least one keyword argumnet in (`s`, `m`, `l`).')
        param = ' '.join(f'{name}{length}' for name, length in dict(s=s, m=m, l=l).items() if length)
        Attribute.__init__(self, 'class', f'pull-{param}')


DoPull = Pull


class Row(Tag):
    @default_initializer
    def __init__(self, *columns: 'Component'):
        Tag.__init__(self, 'div', Attribute('class', 'row'), *columns)

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> inc.Row(inc.Div('here is a row'), inc.Color('red'))
        """


class Setion(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'div', Attribute('class', 'section'), *components)

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> inc.Container(inc.Setion('this is head of one section.', 'these are the tail.', '...'))
        """


class Divider(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'div', Attribute('class', 'divider'), *components)

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> inc.Container(inc.Setion('this is head of one section.',
        >>>                          inc.Divider(),
        >>>                          'these are the tail.', '...'))
        """
