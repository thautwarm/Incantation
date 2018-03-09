from ..abst import traits_class, Tag, Attribute, ITraitsTag, Component


@traits_class('html', inherit_from=Tag)
class HTML(ITraitsTag):
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


InitSource = """
<!DOCTYPE html>
<html>
<head>
  <!--Import Google Icon Font-->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <!--Import materialize.css-->
 <link rel="stylesheet" href="https://cdn.bootcss.com/materialize/0.100.2/css/materialize.css">


  <!--Let browser know website is optimized for mobile-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta charset="utf-8">
</head>

<body>
    

    <!-- Compiled and minified JavaScript -->
    <script type="text/javascript" src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/materialize/0.100.2/js/materialize.js"></script>
            
{}
</body>
</html>
"""


class Page:
    def __init__(self, component):
        self.component = component

    def append(self, *components):
        self.component = self.component.append(*components)

    def __str__(self):
        return InitSource.format(str(self.component.set_indent(1)))

    def write(self, to: str = './test.html'):
        with open(to, 'w') as f:
            f.write(str(self))
