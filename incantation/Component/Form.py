from ..utils import default_initializer
from ..abst import Tag, ITraitsAttribute, ITraitsTag, Attribute, traits_class


class Label(Tag):
    @default_initializer
    def __init__(self, for_which: str):
        Tag.__init__(self, 'label', Attribute('for', for_which))


class InputField(Tag):
    @default_initializer
    def __init__(self, *components, id: str, type: str):
        pass
