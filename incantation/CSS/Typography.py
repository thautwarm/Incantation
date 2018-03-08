from ..abst import traits_class, Tag, Attribute, ITraitsTag, ITraitsAttribute


@traits_class('blockquote', inherit_from=Tag)
class Blockquote(ITraitsTag):
    pass


@traits_class('class', 'flow-text', inherit_from=Attribute)
class IsFlowText(ITraitsAttribute):
    pass
