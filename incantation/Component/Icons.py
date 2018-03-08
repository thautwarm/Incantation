from ..abst import traits_class, Attribute, Tag, ITraitsAttribute, ITraitsTag


@traits_class('i', Attribute('class', 'material-icons'), inherit_from=Tag)
class Icon(ITraitsTag):
    pass
