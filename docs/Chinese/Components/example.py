from incantation.Module.CSS.Grid import container, col, row, grid, section
from incantation.Module.CSS.Color import Indigo 
from incantation.Module.CSS.Helpers import align, left_align, right_align, center_align
from incantation.Module.CSS.Media import video_container
from incantation.Module import abst
from incantation.Module import blockquote
from incantation.Module.CSS.Table import table
from incantation.Module.abst import default_conf, gen_helper, Seq
from incantation.template import Page
from incantation.Module.Component.Badges import collections, dropdown, badge, collapsible
from incantation.Module.Component.Icons import icon
from incantation.Module.Component.Button import FAB, raised
from incantation.Module.Component.Form import form, input_field
from incantation.Module.Component.Navbar import navbar
from flask import Flask, g, request, render_template, url_for, redirect

class badges:
    @staticmethod
    def collections():
        c = collections([badge(new = False,href = '#!', num = 1, name = 'Alan'),
                  badge(new = True, href = '#!', num = 4, name = 'Alan'),
                  badge(href = '#!', name = 'Alan'),
                  badge(new = False,href = '#!', num = 14,name = 'Alan')
                                ])
        return Page(Seq('<br>'*3, c)).gen()
    
    def dropdown():
        main = container()
        
        c = globals()['dropdown']([badge(new = False,href = '#!', num = 1, name = 'Alan'),
                  badge(new = True, href = '#!', num = 4, name = 'Alan'),
                  badge(href = '#!', name = 'Alan'),
                  badge(new = False,href = '#!', num = 14,name = 'Alan')],
                  name = 'a dropdown list', id = 'someid')
        main.contains(c)
        return Page(Seq('<br>'*3, main)).gen()
    
    def collapsibles():
        main = container()
        collap = collapsible([
                (icon('filter_drama'),
                 badge(href = '#!', name = "First") ,
                 "<p>Lorem ipsum dolor sit amet.</p>"),
                
                (icon('place'),
                 badge(href = '#!', name = "Second"), 
                 "place")])
                 
        main.contains(collap)
        return Page(main).gen()

app = Flask(__name__)
app.debug = True

@app.route('/<concept_component>', methods=['GET'])
def index(concept_component):
    concept, component = concept_component.split('+')
    return getattr(eval(concept), component)()

app.run('localhost')