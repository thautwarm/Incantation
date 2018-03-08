from ..abst import Tag, Attribute
from ..utils import doc_printer, default_initializer


class CardPanel(Tag):
    @default_initializer
    def __init__(self, *components):
        Tag.__init__(self, 'div', Attribute('class', 'card-panel'), *components)

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> inc.CardPanel(inc.Hover())
        """
