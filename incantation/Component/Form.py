from ..utils import default_initializer
from ..abst import Tag, ITraitsAttribute, ITraitsTag, Attribute, traits_class
from enum import Enum as enum

class Label(Tag):
    @default_initializer
    def __init__(self, for_which: str, verbose_text: str, *components):
        Tag.__init__(self, 'label', Attribute('for', for_which), verbose_text, *components)


class Input(Tag):
    class Enum(enum):
        email = 'email'
        text = 'text'
        password = 'password'
        tel = 'tel'
        file = 'file'

    @default_initializer
    def __init__(self, *components, id: str, type: str):
        Tag.__init__(self, 'input',
                     Attribute('id', id),
                     Attribute('type', type))


class InputFiled(Tag):
    @default_initializer
    def __init__(self, input: 'Input', label: 'Label', *components):
        Tag.__init__(self, 'div', input, label, *components)
