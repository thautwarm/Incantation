from ..utils import default_initializer
from ..abst import Tag, Attribute, traits_class


@traits_class('tr', Tag)
class Tr(Tag):
    pass

#
# class Tr(Tag):
#     @default_initializer
#     def __init__(self, *components):
#         Tag.__init__(self, 'tr', *components)


class Th(Tag):
    @default_initializer
    def __init__(self, column_name):
        Tag.__init__(self, 'th', column_name)


class Thead(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'thead', *components)


class Table(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'table', *components)
