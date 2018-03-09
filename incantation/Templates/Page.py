from ..Templates.HTML import Body

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
{}
</html>
"""

Include = """
<!-- Compiled and minified JavaScript -->
<script type="text/javascript" src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js"></script>
<script src="https://cdn.bootcss.com/materialize/0.100.2/js/materialize.js"></script>        
"""


class Page:
    def __init__(self, *component):
        self.component = Body(Include, *component)

    def append(self, *components):
        self.component = self.component.append(*components)

    def __str__(self):
        return InitSource.format(str(self.component.set_indent(1)))

    def write(self, to: str = './test.html'):
        with open(to, 'w') as f:
            f.write(str(self))
