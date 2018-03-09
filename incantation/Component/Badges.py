from ..abst import Tag, Attribute, ITraitsAttribute, ITraitsTag, traits_class
from ..utils import default_initializer, doc_printer, ArgumentError
import linq


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
                     Attribute('data-activates', id),
                     Attribute('class', 'btn dropdown-button'),
                     *components)

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
    def __init__(self, *components: 'requires an attribute id.'):
        Tag.__init__(self, 'ul', Attribute('class', 'dropdown-content'), *components)

    def link(self, *components):

        for each in self.components:
            if isinstance(each, Attribute) and each.name == 'id':
                id: str = each.components[0]
                return DropdownButton(*components, id=id)

        raise ArgumentError


class NavBar(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self,
                     'nav',
                     Tag('div', Attribute('class', 'nav-wrapper'), *components))


class BrandLogo(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'a', Attribute('class', 'brand-logo'), *components)

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> navbar_with_logo = inc.BrandLogo(inc.Attribute('href', 'https://github.com/thautwarm/Incantation'),
        >>>                                  inc.Attribute('logo_title', 'Incantation Project'))
        """


@traits_class('ul',
              Attribute('class', 'collapsible'),
              Attribute('data-collapsible', 'accordion'),
              inherit_from=Tag)
class Collapsible(ITraitsTag):
    pass


@traits_class('div', Attribute('class', 'collapsible-header'), inherit_from=Tag)
class CollapsibleHeader(ITraitsTag):
    pass


@traits_class('div', Attribute('class', 'collapsible-body'), inherit_from=Tag)
class CollapsibleBody(ITraitsTag):
    pass


class IsDataBadgeCaption(Attribute):

    @default_initializer
    def __init__(self, arg="custom caption", *components):
        Attribute.__init__(self, 'data-badge-caption', arg, *components)
