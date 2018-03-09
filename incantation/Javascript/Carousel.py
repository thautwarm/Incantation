from ..abst import traits_class, Tag, ITraitsAttribute, ITraitsTag, Attribute as Attr, Component
from ..utils import default_initializer
from ..Frequently import *
from ..CSS.Media import Img, IsResponsiveImg
from ..base import Script
from typing import Union
from functools import update_wrapper


@traits_class('class', 'carousel-item', inherit_from=Attribute)
class IsCarouselItem(ITraitsAttribute):
    pass


@traits_class('class', 'carousel caption', inherit_from=Attribute)
class IsCarousel(ITraitsAttribute):
    pass


@traits_class('class', 'carousel-slider', inherit_from=Attribute)
class WithCarouselSlider(ITraitsAttribute):
    pass


class CarouselItem(Tag):

    @default_initializer
    def __init__(self, src: str, href: str, *components):
        Tag.__init__(self, 'a', IsCarouselItem(), Href(href), Img(IsResponsiveImg(), src=src, alt=''), *components)


class Carouse(Tag):

    @default_initializer
    def __init__(self, *components: 'Union[CarouselItem, Component]'):
        Tag.__init__(self, 'div', IsCarousel(), *components)


def render_dict(kwargs: dict):
    return '{{{}}}'.format(', '.join(f'{k}: {v}' for k, v in kwargs.items() if v))


class IsCarouseActivated:
    def __new__(cls, *args, **kwargs):
        return Script(
            f"""
            $(document).ready(function(){{
              $('.carousel').carousel({render_dict(kwargs)});
            }});
            """)


def arg_inpect(full_width: 'true', interval: '2000', transition: '1000', height: '500', indicators: 'true'):
    pass


class Slider(Tag):
    @default_initializer
    def __init__(self, *components: 'Union[Slide, Component]'):
        Tag.__init__(self,
                     'div',
                     Attr('class', 'slider'),
                     Tag('ul',
                         Attr('class', 'slides'),
                         *components))


class Slide(Tag):
    @default_initializer
    def __init__(self, img: str, big_text: str, tiny_text: str, align: str, *components):
        Tag.__init__(self, 'li',
                     Img(src=img, alt=''),
                     Tag('div',
                         Attr('class', f'caption {align}-align'),
                         Tag('h3', big_text),
                         Tag('h5', tiny_text, Attr('light grey-text text-lighten-3'))),
                     *components)


def _DoSliderActivate(**kwargs):
    return Script(f"""
      $(document).ready(function(){{
      $('.slider').slider({render_dict(kwargs)});
    }});
    """)


def DoSliderActivate(full_width='true', interval=2000, transition=1000, height=500, indicators='true'):
    return _DoSliderActivate(full_width=full_width, interval=interval, transition=transition, height=height,
                             indicators=indicators)
