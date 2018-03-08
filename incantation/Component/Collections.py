from ..abst import traits_class, Tag, ITraitsAttribute, ITraitsTag, Attribute
from ..utils import default_initializer


@traits_class('class', 'collection', inherit_from=Attribute)
class IsCollection(ITraitsAttribute):
    pass


@traits_class('div', IsCollection(), inherit_from=Tag)
class Collection(ITraitsTag):
    pass


@traits_class('class', 'collection-item', inherit_from=Attribute)
class IsCollectionItem(ITraitsAttribute):
    pass


@traits_class('a', IsCollectionItem(), inherit_from=Tag)
class CollectionItemA(ITraitsTag):
    pass


@traits_class('li', IsCollectionItem(), inherit_from=Tag)
class CollectionItemLi(ITraitsTag):
    pass


@traits_class('class', 'collection-header', inherit_from=Attribute)
class IsCollectionHeader(ITraitsAttribute):
    pass


@traits_class('class', 'active', inherit_from=Attribute)
class ActivateCollectionItem(ITraitsAttribute):
    pass
