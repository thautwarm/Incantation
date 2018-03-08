from ..abst import traits_class, Attribute, ITraitsAttribute


@traits_class('class', 'breadcrumb', inherit_from=Attribute)
class Breadcrumb(ITraitsAttribute):
    pass
