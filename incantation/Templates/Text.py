from ..abst import traits_class, Tag, ITraitsTag, Attribute
from ..CSS.Media import Img
from ..utils import default_initializer

if False:
    import incantation as inc


@traits_class('p', inherit_from=Tag)
class Paragraph(ITraitsTag):
    pass


class IconTextBlock(Tag):
    @default_initializer
    def __init__(self, icon_color: str, title: str, text: str, icon: 'inc.Icon'):
        """
        <div class="icon-block">
            <h2 class="center light-blue-text"><i class="material-icons">flash_on</i></h2>
            <h5 class="center">Speeds up development</h5>

            <p class="light"></p>
          </div>
        :param components:
        """

        Tag.__init__(self, 'div',
                     Attribute('class', 'icon-block'),
                     Tag('h2', Attribute('class', f'center {icon_color}-text'), icon),
                     Tag('h5', Attribute('class', 'center'), title),
                     Tag('p', Attribute('class', 'light'), text))


class ImgTextBlock(Tag):
    @default_initializer
    def __init__(self, img: str, title: str, text: str):
        Tag.__init__(self, 'div',
                     Attribute('class', 'icon-block'),
                     Tag('h2', Img(src=img, alt='')),
                     Tag('h5', Attribute('class', 'center'), title),
                     Tag('p', Attribute('class', 'light'), text))


class TextColor(Attribute):
    @default_initializer
    def __init__(self, color: str):
        Attribute.__init__(self, 'class', f'{color}-text')
