from .Module.abst import abstract_object, gen_helper
from jinja2 import Template
Body=\
"""
  <!DOCTYPE html>
  <html>
    <head>
      <!--Import Google Icon Font-->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="static/materialize/css/materialize.min.css"  media="screen,projection"/>

      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <meta charset="utf-8">
    </head>

    <body>
      <!--Import jQuery before materialize.js-->
      <script type="text/javascript" src="static/jquery-3.2.1.min.js"></script>
      <script type="text/javascript" src="static/materialize/js/materialize.min.js"></script>
      {{body}}
    </body>
  </html>
"""

class Page:
    """  user help : >> help (Page.init)   
            Guide:
                page = Page( content )
                page.write('./test.html')
                
    """
    def __init__(self, body = ""):
        self.body = gen_helper(body) 
    def __str__(self):
        return Template(Body).render(body  = self.body)
    def write(self, to = './test.html'):
        with open(to, 'w', encoding = 'utf-8') as f:
            Template(Body).render(body  =  self.body) ->> f.write
    def gen(self):
        return Template(Body).render(body  = self.body)
        

        


