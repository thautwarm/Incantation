from ..abst import traits_class, Tag, ITraitsTag, ITraitsAttribute, Attribute, IndentWrapper
from ..utils import call_func


@traits_class('href', inherit_from=Attribute)
class Href(ITraitsAttribute):
    pass


@traits_class('src', inherit_from=Attribute)
class Src(ITraitsAttribute):
    pass


def Br() -> IndentWrapper:
    return IndentWrapper('<br>')


NewLine = Br()
