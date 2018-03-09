from typing import List, Iterable
from ..utils import default_initializer, ClassProperty, ArgumentError
from ..abst import Tag, Attribute as Attr, ITraitsAttribute, traits_class
from ..CSS.Grid import C
from ..CSS.Media import Img
from ..Templates import HTML


@traits_class('class', 'side-nav', inherit_from=Attr)
class IsSideNav(ITraitsAttribute):
    pass


class SideNav(Tag):
    @default_initializer
    def __init__(self, id: str, *componnets):
        Tag.__init__(self, 'ul', Attr('id', id), IsSideNav(), *componnets)

    @classmethod
    def new(cls,
            id: str,
            profile_background_img: str,
            user_info: 'List[ProfileItem]',
            items: 'Iterable' = ()
            ):
        return SideNav(
            id,
            HTML.Li(
                C(
                    Attr('class', 'user-view'),
                    C(
                        Attr('class', 'background'),
                        Img(src=profile_background_img, alt='background')
                    ),
                    *user_info,
                    *items
                )
            )
        )

    def active(self, *codes: str):
        return HTML.Script(
            *codes,
            ' $(".button-collapse").sideNav();'
        )

    def link(self, *components) -> 'SideNavLink':
        for each in self.components:
            if isinstance(each, Attr) and each.name == 'id':
                id: str = each.components[0]
                return SideNavLink(id, *components)

        raise ArgumentError


class SideNavLink(Tag):
    @default_initializer
    def __init__(self, id: str, *components):
        Tag.__init__(self, 'a',
                     Attr('data-activates', id),
                     Attr('class', 'button-collapse'),
                     *components)


class SideNavItem(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'a', *components)
