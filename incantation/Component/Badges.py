from ..abst import Tag, Attribute, ITraitsAttribute, ITraitsTag, traits_class
from ..utils import default_initializer, doc_printer


class Collection(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'div', Attribute('class', 'collection'), *components)


class CollectionItem(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'a', Attribute('class', 'collection-item'), *components)


class Badge(Tag):
    @default_initializer
    def __init__(self, *components, new=False):
        if new:
            Tag.__init__(self, 'span', Attribute('class', 'badge', 'new'), *components)
        else:
            Tag.__init__(self, 'span', Attribute('class', 'badge'), *components)


class DropdownButton(Tag):

    @default_initializer
    def __init__(self, *components, id: str = 'dropdown2'):
        Tag.__init__(self, 'a',
                     Attribute('class', 'btn dropdown-button'),
                     Attribute('data-activates', id), *components)

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> body = inc.Dropdown(id='dropdown2')
        >>> link = body.link()
        >>> print(body)
        >>> print(link)
        <ul id="dropdown2" class="dropdown-content">

        </ul>

        <a class="btn dropdown-button" data-activates="dropdown2">

        </a>
        """


class Dropdown(Tag):
    help = DropdownButton.help

    @default_initializer
    def __init__(self, *components, id: str = 'dropdown2'):
        Tag.__init__(self, 'ul', Attribute('id', id), Attribute('class', 'dropdown-content'), *components)

    def link(self, *components):
        _, id = self.components[0]
        return DropdownButton(*components, id=id)


class NavBar(Tag):

    @default_initializer
    def __init__(self, *components):
        Tag.__init__()
