from ..abst import traits_class, Tag, ITraitsTag


@traits_class('p', inherit_from=Tag)
class Paragraph(ITraitsTag):
    pass
