from ..abst import Tag, Attribute, traits_class, ITraitsAttribute, ITraitsTag
from ..utils import default_initializer, ClassProperty, doc_printer
from typing import List, Optional
from enum import Enum as enum

"""
the inheritance here is redundant, but the type hinting of pycharm is not intelligent enough.
so I write it this way for auto-complement. 
"""


class TableDoc:

    @staticmethod
    @doc_printer
    def help(self):
        """
        See http://materializecss.com/table.html
        >>> import incantation as inc
        >>> table1 = inc.Table([[1, 2, 3], [2, 3, 4]], ['a', 'b', 'c'], index=[1, 2]).set_indent(1)
        >>> table2 = inc.Table(data_source=[[1, 2, 3], [2, 3, 4]], column=['a', 'b', 'c']).set_indent(1)
        >>> table3 : inc.Table = inc.Table.empty
        >>> columns = ['a', 'b', 'c']
        >>> data_source = [[1, 2, 3], [2, 3, 4]]
        >>> table3.append(Attribute('class', inc.Table.Enum.centered.value),
        >>>               inc.Thead(
        >>>                   inc.Tr(*(inc.Th(column) for column in columns))),
        >>>               inc.TBody(*(
        >>>                    inc.Tr(*(inc.Td(each_col) for each_col in data))
        >>>                    for data in data_source))))
        """


@traits_class('tr', inherit_from=Tag, help=TableDoc.help)
class Tr(ITraitsTag):
    pass


@traits_class('th', inherit_from=Tag, help=TableDoc.help)
class Th(ITraitsTag):
    pass


@traits_class('td', inherit_from=Tag, help=TableDoc.help)
class Td(ITraitsTag):
    pass


@traits_class('thead', inherit_from=Tag, help=TableDoc.help)
class Thead(ITraitsTag):
    pass


@traits_class('tbody', inherit_from=Tag, help=TableDoc.help)
class TBody(ITraitsTag):
    pass


class Table(Tag):
    help = TableDoc.help

    class Enum(enum):
        bordered = 'bordered'
        striped = 'striped'
        highlight = 'highlight'
        centered = 'centered'

    @default_initializer
    def __init__(self, data_source: 'List[List]',
                 columns: 'List',
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


@traits_class('class', "responsive-table", inherit_from=Attribute, help=TableDoc.help)
class IsResponsiveTable(ITraitsAttribute):
    pass
