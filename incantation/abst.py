import copy as pycopy
from abc import abstractmethod
from collections import defaultdict
from typing import Tuple, Optional, Union, Any

from linq import Flow

from .utils import isa, is_unque, doc_printer, default_initializer


def traits_class(name, inherit_from: 'class'):
    # def wrap(cls: 'class'):
    #     class cls(inherit_from):
    #         @default_initializer
    #         def __init__(self, *components):
    #             inherit_from.__init__(self, name, *components)
    #
    #     return cls

    return wrap


class Format:
    Tag = ('{indent}<{name} {attributes}>\n'
           '{indent}{components}'
           '{indent}</{name}>')

    Attribute = '{name}{eq}"{content}"'
    Indent = ' '


class Component:
    name: str
    components: 'Optional[Tuple[Component]]'

    def __iter__(self):
        yield self.name
        yield from self.components

    def copy(self, deep=False):
        return pycopy.deepcopy(self) if deep else pycopy.copy(self)

    def append(self, *components: 'Component'):
        new = self.empty
        new.name = self.name

        if hasattr(self, 'indent'):
            new.indent = self.indent

        new.components = self.components + components
        return new

    def set_indent(self, n):
        return self

    @property
    def empty(self):
        return type(self)(super)

    @abstractmethod
    def help(self):
        raise NotImplemented

    @abstractmethod
    def __str__(self):
        raise NotImplemented


class RecursiveIndent(Component):
    indent: int

    def set_indent(self, n: int):
        new = self.empty

        new.name = self.name

        new.components = tuple(each.set_indent(n + 1) for each in self.components)

        new.indent = n + 1

        return new

    @abstractmethod
    def help(self):
        raise NotImplemented

    @abstractmethod
    def __str__(self):
        raise NotImplemented


class IndentWrapper(Component):
    __slots__ = ['components', 'name', 'indent']
    components: 'Any'

    def __init__(self, obj, indent=1):
        self.components = obj
        self.indent = indent

    def set_indent(self, n: int):
        return IndentWrapper(self.components, n)

    def __str__(self):
        head = f'\n{Format.Indent * self.indent}'
        return head + str(self.components).replace('\n', head)

    def copy(self, deep=False):
        return pycopy.deepcopy(self) if deep else pycopy.copy(self)

    @doc_printer
    def help(self):
        """
        the wrapper of the object which is not of incantation category.
        """


Object = Union[Component, str]


class Attribute(Component):

    def __init__(self, name: str, *components):
        if name is super:
            return

        self.components = components
        self.name = name

    def __str__(self):
        return Format.Attribute.format(name=self.name,
                                       eq='' if not self.components else '=',
                                       content='' if not self.components else ' '.join(map(str, self.components)))

    @classmethod
    def check_componnets(cls, components):
        return tuple(components)

    @doc_printer
    def help(self):
        """
        represent the the attributes of blocks in XML.
        """


class Tag(RecursiveIndent):
    def __init__(self, name: str, *components, indent=1):
        if name is super:
            return

        self.name = name
        self.components = self.check_componnets(components)
        self.indent = indent

    @classmethod
    def check_componnets(cls, components):
        return tuple(comp if isa(comp, Component) else IndentWrapper(comp) for comp in components)

    def __str__(self):
        grouped = Flow(self.components).GroupBy(isa(type=Attribute)).Unboxed()

        others = grouped.get(False)
        attributes = grouped.get(True)

        if not others:
            others = ()
        if not attributes:
            attributes = ()

        if not is_unque(map(lambda a: a.name, attributes)):
            render_attributes = defaultdict(list)

            for each in attributes:
                attribute = render_attributes[each.name]
                attribute.append(each.components)

            attributes = tuple(Attribute(name, *sum(configs, ())) for name, configs in render_attributes.items())

        return Format.Tag.format(name=self.name,
                                 indent=Format.Indent * self.indent,
                                 components='{}\n'
                                 .format(f'{" "*self.indent}\n'.join(
                                     map(str, others)))
                                 if others else '\n' if self.indent <= 1 else '',
                                 attributes=' '.join(map(str, attributes)))

    @doc_printer
    def help(self):
        """
        represent the the blocks in XML.
        """

# tag.make('1', '2', attr.make('class', 'true'))
# print(tag)
