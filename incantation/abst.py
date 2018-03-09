import copy as pycopy
from abc import abstractmethod
from collections import defaultdict
from functools import update_wrapper
from typing import Tuple, Optional, Union, Any, Callable
from linq import Flow
from .utils import isa, is_unque, doc_printer, default_initializer, ClassProperty


class Format:
    Tag = ("{indent}<{name}{attributes}>\n"
           "{components}"
           "{indent}</{name}>\n")

    Attribute = '{name}{eq}"{content}"'
    Indent = ' ' * 4


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

        if hasattr(self, 'spec'):
            new.spec = self.spec

        if hasattr(self, 'indent'):
            new.indent = self.indent

        new.components = self.components + components
        return new

    def print_indent(self):
        if isinstance(self, IndentWrapper):
            return self.name
        return [(self.name, self.indent),
                [each.print_indent() for each in self.components if isinstance(each, Component)]]

    def set_indent(self, n):
        return self

    def __rrshift__(self, other):
        return self.append(other)

    def __lshift__(self, other):
        return self.append(other)

    def __rshift__(self, other):
        if callable(other):
            return other(self)
        elif isinstance(other, Component):
            return other.append(self)
        else:
            raise TypeError

    def __rlshift__(self, other):
        if callable(other):
            return other(self)
        elif isinstance(other, Component):
            return other.append(self)
        else:
            raise TypeError

    # noinspection PyCallingNonCallable
    @ClassProperty
    def empty(cls) -> 'Component':
        return cls(super)

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

        new.indent = n

        return new

    @abstractmethod
    def help(self):
        raise NotImplemented

    @abstractmethod
    def __str__(self):
        raise NotImplemented


class IndentWrapper(Component):
    __slots__ = ['components', 'indent']

    components: 'Any'

    name = 'wrapper'

    def __init__(self, obj, indent=1):
        self.components = obj
        self.indent = indent

    def set_indent(self, n: int):
        return IndentWrapper(self.components, n)

    def __str__(self):
        return f'{Format.Indent*self.indent}{self.components}\n'

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
                                 components='\n'.join(map(str, others)) if others else '\n' if self.indent <= 1 else '',
                                 attributes=f' {" ".join(map(str, attributes))}' if attributes else '')

    @doc_printer
    def help(self):
        """
        represent the the blocks in XML.
        """


def traits_class(*args, inherit_from: 'class' = Tag, help: 'Callable' = None):
    def wrap(cls):
        @default_initializer
        def __init__(self, *components):
            inherit_from.__init__(self, *args, *components)

        return type(cls.__name__, (inherit_from,), {'__init__': __init__, 'help': help})

    return wrap


def intelligence_traits_class(*args, inherit_from: 'class' = Tag, help: 'Callable' = None):
    def wrap(cls):
        @default_initializer
        def __init__(self, *components):
            inherit_from.__init__(self, *args, *components)

        update_wrapper(__init__, cls.__init__)
        return type(cls.__name__, (inherit_from,), {'__init__': __init__, 'help': help})

    return wrap


class ITraitsTag(Tag):
    # for auto-complement
    def __init__(self, *components):
        assert type(self) is Tag
        super().__init__(*components)
        raise NotImplemented


class ITraitsAttribute(Attribute):
    # for auto-complement
    def __init__(self, *components):
        assert type(self) is Tag
        super().__init__(*components)
        raise NotImplemented


def check_has_attributes(components, *attribute_names: str):
    for each in attribute_names:
        assert any(map(lambda x: x.name == each if isa(x, Attribute) else False, components))


def check_has_tags(components, *tag_names: str):
    for each in tag_names:
        assert any(map(lambda x: x.name == each if isa(x, Tag) else False, components))
