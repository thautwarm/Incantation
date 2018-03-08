from ..abst import Tag, Attribute, traits_class, ITraitsAttribute, ITraitsTag
from ..utils import default_initializer, ClassProperty
from typing import List, Optional
from enum import Enum as enum

"""
the inheritance here is redundant, but the type hinting of pycharm is not intelligent enough.
so I write it this way for auto-complement. 
"""


@traits_class('tr', inherit_from=Tag)
class Tr(ITraitsTag):
    pass


@traits_class('th', inherit_from=Tag)
class Th(ITraitsTag):
    pass


@traits_class('td', inherit_from=Tag)
class Td(ITraitsTag):
    pass


@traits_class('thead', inherit_from=Tag)
class Thead(ITraitsTag):
    pass


@traits_class('tbody', inherit_from=Tag)
class TBody(ITraitsTag):
    pass


class Table(Tag):
    class Enum(enum):
        bordered = 'bordered'
        striped = 'striped'
        highlight = 'highlight'
        centered = 'centered'

    @default_initializer
    def __init__(self, data_source: 'List[List]', columns: 'List',
                 style: 'Table.Enum' = None,
                 index: 'Optional[List]' = None):

        if style is None:
            style = Table.Enum.striped

        if index is None:

            Tag.__init__(self, 'table',
                         Attribute('class', style.value),
                         Thead(
                             Tr(*(Th(column) for column in columns))),
                         TBody(*(
                             Tr(*(Td(each_col) for each_col in data))
                             for data in data_source)))
        else:

            Tag.__init__(self, 'table',
                         Attribute('class', style.value),
                         Thead(
                             Tr(Th(''), *(Th(column) for column in columns))),
                         TBody(*(
                             Tr(Td(index[row_idx]), *(Td(each_col) for each_col in data))
                             for row_idx, data in enumerate(data_source))))


@traits_class('class', "responsive-table", inherit_from=Attribute)
class ResponsiveTable(ITraitsAttribute):
    pass
