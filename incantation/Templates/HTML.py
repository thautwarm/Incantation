from ..abst import traits_class, Tag, ITraitsTag, ITraitsAttribute, Attribute


@traits_class('html', inherit_from=Tag)
class Html(ITraitsTag):
    pass


@traits_class('head', inherit_from=Tag)
class Head(ITraitsTag):
    pass


@traits_class('meta', inherit_from=Tag)
class Meta(ITraitsTag):
    pass


@traits_class('body', inherit_from=Tag)
class Body(ITraitsTag):
    pass


@traits_class('script', Attribute('type', 'text/javascript'), inherit_from=Tag)
class Script(ITraitsTag):
    pass


@traits_class('link', inherit_from=Tag)
class Link(ITraitsTag):
    pass


@traits_class('a', inherit_from=Tag)
class A(ITraitsTag):
    pass


@traits_class('ul', inherit_from=Tag)
class Ul(ITraitsTag):
    pass


@traits_class('li', inherit_from=Tag)
class Li(ITraitsTag):
    pass


@traits_class('Span', inherit_from=Tag)
class Span(ITraitsTag):
    pass
