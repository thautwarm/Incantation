from typing import Tuple, Optional, Union, Any
from abc import abstractmethod

from collections import defaultdict

from .utils import isa, is_unque
from linq import Flow
import copy as pycopy


class Format:
    Tag = ('{indent}<{name} {attributes}>\n'
           '{indent}{components}\n'
           '{indent}</{name}>\n')

    Attribute = '{name}{eq}"{content}"'
    Indent = ' '


class IIndent:
    indent: int

    @abstractmethod
    def set_indent(self, n: int):
        raise NotImplemented


class Component:
    name: str
    components: 'Optional[Tuple[Component]]'

    @property
    def empty(self):
        return type(self)(self.name)

    @abstractmethod
    def __str__(self):
        raise NotImplemented

    def __iter__(self):
        yield self.name
        yield from self.components

    def copy(self, deep=False):
        return pycopy.deepcopy(self) if deep else pycopy.copy(self)

    def append(self, *components: 'Component'):
        new = self.empty
        new.components = self.components + components
        return new


class IndentWrapper(IIndent):
    obj: 'Any'

    def __init__(self, obj, indent=1):
        self.obj = obj
        self.indent = indent

    def set_indent(self, n: int):
        self.indent = n

    def __str__(self):
        head = f'\n{Format.Indent * self.indent}'
        return head + str(self.obj).replace('\n', head)

    def copy(self, deep=False):
        return pycopy.deepcopy(self) if deep else pycopy.copy(self)


Object = Union[Component, str]


class Attribute(Component):

    def __init__(self, name, *components):
        self.components = components
        self.name = name

    def __str__(self):
        return Format.Attribute.format(name=self.name,
                                       eq='' if not self.components else '=',
                                       content='' if not self.components else ' '.join(map(str, self.components)))


class Tag(IIndent, Component):

    def __init__(self, name, *components, indent=1):
        self.name = name
        self.components = components
        self.indent = indent

    def set_indent(self, n: int):
        self.indent = n
        for each in self.components:
            if isinstance(each, IIndent):
                each.set_indent(n + 1)

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
                                 components=f'{" "*self.indent}\n'.join(map(str, others)),
                                 attributes=' '.join(map(str, attributes)))

# tag.make('1', '2', attr.make('class', 'true'))
# print(tag)
