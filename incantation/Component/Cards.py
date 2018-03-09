from ..abst import traits_class, Attribute, Tag, ITraitsAttribute, ITraitsTag
from ..utils import default_initializer, doc_printer
from .Buttons import Horizontal

if False:
    import incantation as inc


class CardModule:

    @staticmethod
    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> assert str(inc.C()) == str(inc.Tag('div'))
        >>> card = inc.C(inc.IsCard(),
        >>>
        >>>              inc.Color('blue-grey').darken,
        >>>
        >>>              inc.CardContent(
        >>>                             inc.CardTitle('Card Title'),
        >>>                             inc.Paragraph("I am a very simple card."),
        >>>                             text_color='white'),
        >>>
        >>>              inc.CardAction(inc.Tag('a', inc.Attribute('href', '#!'), 'this is a link'),
        >>>                             inc.Tag('a', inc.Attribute('href', '#!'), 'this is another link')))
        >>> print(card)
        <div class="card blue-grey">
            <div class="card-content white-text">
                <span class="card-title">
                    Card Title
                </span>

                <p>
                    I am a very simple card.
                </p>
            </div>

            <div class="card-action">
                <a href="#!">
                    this is a link
                </a>

                <a href="#!">
                    this is another link
                </a>
            </div>
        </div>
        """


@traits_class('class', 'card', inherit_from=Attribute)
class IsCard(ITraitsAttribute):
    pass


@traits_class('span', Attribute('class', 'card-title'), inherit_from=Tag)
class CardTitle(ITraitsTag):
    pass


@traits_class('div', Attribute('class', 'card-action'), inherit_from=Tag)
class CardAction(ITraitsTag):
    pass


class CardImg(Tag):

    @default_initializer
    def __init__(self, *components: 'requires an image and a str'):
        Tag.__init__(self, 'div',
                     Attribute('class', 'card-image'),
                     *components)

    @doc_printer
    def help(self):
        """
        >>>with open('xxx.html', 'w') as file:
        >>>     inc.C(inc.IsCard(),
        >>>       inc.Color('blue-grey').lighten,
        >>>       inc.CardImage(img=inc.Img(src='xxx.png')),
        >>>       inc.CardContent(inc.CardTitle('Title'),
        >>>                       inc.Paragraph('some text here'),
        >>>                       text_color='whilte')).set_indent(0) >> file.write
        """


@traits_class('div', Attribute('class', 'card-image'), inherit_from=Tag)
class CardImage(ITraitsTag):
    pass


class CardContent(Tag):
    @default_initializer
    def __init__(self, *components: 'requres a TextColor'):
        Tag.__init__(self, 'div',
                     Attribute('class', 'card-content'),
                     *components)
