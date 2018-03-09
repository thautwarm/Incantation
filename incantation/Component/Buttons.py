from ..abst import Attribute, Tag, traits_class, ITraitsTag, ITraitsAttribute, Component
from ..utils import default_initializer

if False:
    import incantation as inc


@traits_class('class', 'disabled', inherit_from=Attribute)
class IsDisabledButton(ITraitsTag):
    pass


@traits_class('class', 'waves-effect waves-light', inherit_from=Attribute)
class IsRaised(ITraitsAttribute):
    pass


@traits_class('class', 'btn', inherit_from=Attribute)
class IsButton(ITraitsAttribute):
    pass


@traits_class('class', 'btn-large', inherit_from=Attribute)
class IsLargeButton(ITraitsAttribute):
    pass


@traits_class('class', 'btn-flat', inherit_from=Attribute)
class IsFlatButton(ITraitsAttribute):
    pass


@traits_class('class', 'horizontal', inherit_from=Attribute)
class Horizontal(ITraitsAttribute):
    pass


@traits_class('class', 'click-to-toggle', inherit_from=Attribute)
class IsButtonClickToToggle(ITraitsAttribute):
    pass


@traits_class('class', 'toolbar', inherit_from=Attribute)
class IsFABTooolbar(ITraitsAttribute):
    pass


@traits_class('class', 'btn-floating', inherit_from=Attribute)
class IsFloating(ITraitsAttribute):
    pass


class Submit(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'button',
                     Attribute('class', 'btn'),
                     Attribute('type', 'submit'),
                     Attribute('name', 'action'), *components)

    @property
    def to_large_btn(self):
        new: 'Component' = self.empty
        new.indent = self.indent
        new.name = self.name
        head, *tail = self.components
        new.components = Attribute('class', 'btn-large'), *tail

        return new


class Button(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'a',
                     Attribute('class', 'btn'),
                     *components)


class FixActionButton(Tag):
    @default_initializer
    def __init__(self, color: 'inc.Color', main_icon: 'inc.Icon', *components: 'the list of sub icons'):
        Tag.__init__(self, 'div', Attribute('class', 'fixed-action-btn'),
                     Tag('a', IsFloating(), IsLargeButton(), color),
                     main_icon,
                     Tag('ul', *components))

    def append_sub_icon(self, *btns: 'tag name should be a with an icon inside'):
        # TODO optimize use .empty
        new = self.copy()
        *neck, end = new.components
        end: 'Tag'
        new.components = neck, end.append(*(map(lambda x: Tag('li', x), btns)))
        return new
