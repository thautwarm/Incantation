from ..abst import Attribute
from ..err import ArgumentError
from ..utils import ClassProperty, doc_printer, default_initializer
from enum import Enum as enum


class Align(Attribute):
    class Enum(enum):
        Vertical = 'valign-wrapper'
        Left = 'left-align'
        Right = 'right-align'
        Center = 'center-align'
        ForceLeft = 'left'
        ForceCenter = 'center'
        ForceRight = 'right'

    @default_initializer
    def __init__(self, style: 'Align.Enum'):
        assert isinstance(style, Align.Enum)
        Attribute.__init__(self, 'class', style.value)

    @ClassProperty
    def vertical(cls) -> 'Align':
        return Align(Align.Enum.Vertical)

    @ClassProperty
    def left(cls) -> 'Align':
        return Align(Align.Enum.Left)

    @ClassProperty
    def force_left(cls) -> 'Align':
        return Align(Align.Enum.ForceLeft)

    @ClassProperty
    def right(cls) -> 'Align':
        return Align(Align.Enum.Right)

    @ClassProperty
    def force_right(cls) -> 'Align':
        return Align(Align.Enum.ForceRight)

    @ClassProperty
    def center(cls) -> 'Align':
        return Align(Align.Enum.Center)

    @ClassProperty
    def force_center(cls) -> 'Align':
        return Align(Align.Enum.ForceCenter)

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> inc.Container(inc.Align.vertical)
        """


DoAlign = Align


class IsHide(Attribute):
    class Enum(enum):
        default = 'hide'
        small_only = 'hide-on-small-only'
        med_only = 'hide-on-med-only'
        large_only = 'hide-on-large-only'

    @default_initializer
    def __init__(self, style: 'IsHide.Enum'):
        assert isinstance(style, IsHide.Enum)
        Attribute.__init__(self, 'class', style.value)

    @ClassProperty
    def default(cls) -> 'IsHide':
        return IsHide(IsHide.Enum.default)

    @ClassProperty
    def small_only(cls) -> 'IsHide':
        return IsHide(IsHide.Enum.small_only)

    @ClassProperty
    def med_only(cls) -> 'IsHide':
        return IsHide(IsHide.Enum.med_only)

    @ClassProperty
    def large_only(cls) -> 'IsHide':
        return IsHide(IsHide.Enum.large_only)


class Truncate(Attribute):
    @default_initializer
    def __init__(self):
        Attribute.__init__(self, 'class', 'truncate')

    @doc_printer
    def help(self):
        """
        See `truncate` at http://materializecss.com/helpers.html.
        内容格式化
        >>> import incantation as inc
        >>> inc.Truncate()
        """


IsTruncate = Truncate


class Hover(Attribute):
    @default_initializer
    def __init__(self):
        Attribute.__init__(self, 'class', 'hoverable')


IsHover = Hover
