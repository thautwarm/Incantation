from .Buttons import Submit, IsButton
from ..utils import default_initializer, doc_printer
from ..abst import Tag, ITraitsAttribute, ITraitsTag, Attribute, traits_class, check_has_attributes, check_has_tags
from enum import Enum as enum

if False:
    import incantation as inc


class Label(Tag):
    @default_initializer
    def __init__(self, *components: 'requires atttribute: for, and a str for visibility'):
        Tag.__init__(self, 'label', *components)

    @doc_printer
    def help(self):
        """
        >>> Label("Input here", Attribute('id', 'xxx'))
        """


class Input(Tag):
    class Enum(enum):
        email = 'email'
        text = 'text'
        password = 'password'
        tel = 'tel'
        file = 'file'
        checkbox = 'checkbox'
        radio = 'radio'

    @default_initializer
    def __init__(self, type: 'Input.Enum', *components: 'optional attribute: id, name.'):
        # check_has_attributes(components, 'id', 'name')
        if id:
            Tag.__init__(self, 'input',
                         Attribute('type', type.value),
                         *components)
        else:
            Tag.__init__(self, 'input',
                         Attribute('type', type.value),
                         *components)


@traits_class('class', 'input-field', inherit_from=Attribute)
class IsInputField(ITraitsAttribute):
    pass


class InputField(Tag):
    @default_initializer
    def __init__(self, *components: 'requires tags of following types: Label, Input'):
        Tag.__init__(self, 'div', IsInputField(), *components)


@traits_class('class', 'multiple', inherit_from=Attribute)
class IsMultiFileInput(ITraitsAttribute):
    pass


@traits_class('class', 'file-field', inherit_from=Attribute)
class IsFileField(ITraitsAttribute):
    pass


@traits_class('class', 'file-path-wrapper', inherit_from=Attribute)
class IsFilePathWrapper(ITraitsAttribute):
    pass


@traits_class('div',
              IsFilePathWrapper(),
              Input(Input.Enum.text,
                    Attribute('class', 'file-path validate')),
              inherit_from=Tag)
class FilePathWrapper(ITraitsTag):
    pass


class PlaceHolder(Attribute):
    @default_initializer
    def __init__(self, name):
        Attribute.__init__(self, 'placeholder', name)


WithPlaceHolder = PlaceHolder


class Form(Tag):

    @default_initializer
    def __init__(self, *components: 'contains the input fields'):
        Tag.__init__(self, 'form', *components)

    @doc_printer
    def help(self):
        """
        >>> attr = inc.Attribute
        >>> tag = inc.Tag
        >>> inc.Form(
        >>>          inc.Row << inc.InputField(
        >>>                                 input=inc.Input(Input.Enum.text,
        >>>                                                 attr('id', 'xxx'),
        >>>                                                 inc.Label('input xxx', attr('for', 'xxx')))))
        >>>
        >>>
        """
