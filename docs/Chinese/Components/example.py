from incantation.Module.CSS.Grid import container, col, row, grid, section, divider
from incantation.Module.CSS.Color import Indigo, color
from incantation.Module.CSS.Helpers import align, left_align, right_align, center_align
from incantation.Module.CSS.Media import video_container
from incantation.Module import abst
from incantation.Module import blockquote
from incantation.Module.CSS.Table import table
from incantation.Module.abst import default_conf, gen_helper, Seq, abstract_object,indent_setter, default_attr, attrset_sugar
from incantation.template import Page
from incantation.Module.Component.Badges import collections, dropdown, badge, collapsible
from incantation.Module.Component.Icons import icon
from incantation.Module.Component.Button import FAB, raised
from incantation.Module.Component.Form import form, input_field
from incantation.Module.Component.Navbar import navbar
from flask import Flask, g, request, render_template, url_for, redirect

import incantation.Module.Component.Icons as Icons


class badges:
    @staticmethod
    def collections():
        c = collections([badge(new=False, href='#!', num=1, name='Alan'),
                         badge(new=True, href='#!', num=4, name='Alan'),
                         badge(href='#!', name='Alan'),
                         badge(new=False, href='#!', num=14, name='Alan')
                         ])
        return Page(Seq('<br>' * 3, c)).gen()

    @staticmethod
    def dropdown():
        main = container()

        c = globals()['dropdown']([badge(new=False, href='#!', num=1, name='Alan'),
                                   badge(new=True, href='#!', num=4, name='Alan'),
                                   badge(href='#!', name='Alan'),
                                   badge(new=False, href='#!', num=14, name='Alan')],
                                  name='a dropdown list', id='someid')
        main.contains(c)
        return Page(Seq('<br>' * 3, main)).gen()

    @staticmethod
    def collapsibles():
        main = container()
        collap = collapsible([
            (icon('filter_drama'),
             badge(href='#!', name="First"),
             "<p>Lorem ipsum dolor sit amet.</p>"),

            (icon('place'),
             badge(href='#!', name="Second"),
             "place")])

        main.contains(collap)
        return Page(main).gen()


class forms:
    @staticmethod
    def normal():
        main = container()
        a_form = form(
            Seq("<br>" * 2,
                divider(),
                input_field(grid(l=10),
                            field_name='username',
                            type='text',
                            icon=Icons.account_circle,
                            id='username'),

                input_field(grid(l=10),
                            field_name='password',
                            type='password',
                            icon=icon('exposure_plus_1'),
                            id='password'
                            )
                )
        )
        main.contains(a_form)
        return Page(main).gen()

    @staticmethod
    def multifields():
        main = container()
        username = input_field(grid(l=5),
                               field_name='username',
                               type='text',
                               icon=Icons.account_circle,
                               id='username')
        password = input_field(grid(l=5),
                               field_name='password',
                               type='password',
                               icon=icon('exposure_plus_1'),
                               id='password')
        a_row = row(Seq(username, password))
        a_form = form(
            Seq("<br>" * 2,
                divider(),
                a_row
                )
        )
        main.contains(a_form)
        return Page(main).gen()
    
class button:
    @staticmethod
    def raised():
        raised = globals()['raised']
        more   = raised(icon = icon('cloud'), name = "  More", href = 'https://www.zhihu.com') 
        a_row  = row(more)
        right_align(a_row)

        more.cons_class(color('green').gen())

        collection=\
        collections([badge(new=True, href='#!', num=1, name='今日新闻'),
                     badge(new=True, href='#!', num=4, name='鬼畜专区'),
                     badge(href='#!', name='哲学论坛'),
                     badge(new=False, href='#!', num=14, name='血条众筹'),
                     
                    ])
        
        main = container()
        main.contains(Seq(collection,a_row))
        return Page(main).gen()

    def fab():
        fab = FAB([dict(color = 'red',  icon = icon("insert_chart"),  href = "#"),
                   dict(color = 'blue', icon = icon("publish"),       href = "#"),
                  ], 
                 color='red', horizon=True)
        return Page(fab).gen()

class sidenav(indent_setter, abstract_object):

    @default_attr('class', 'side-nav fixed') 
    # attributes有默认属性 class = "side-nav fixed"
    # 可使用 obj.append_class(arg:str)和obj.cons_class(arg:str)添加class的值。
    def init(self, content, **attributes):
        sugar = attrset_sugar(self.conf, attributes)

        # self.conf 是用来渲染Jinja2模板的参数字典。
        
        sugar('id', 'slide-out') # 从attributes里取出id, 赋值给self.conf['id']中
        # 若attributes中不存在键id, 则赋值'side-out'给self.conf['id']

        sugar('background', 'teal')
        # 默认背景为 纯色teal

        sugar('header', None) # 默认不进行用户设置
        # 默认背景为 纯色teal

        body = \
"""
<script>$(document).ready(function(){
 $(".button-collapse").sideNav();
});
</script>
<ul id="{{id}}" {{attributes_dict}}>
    <li>
        <div class="userView">

            <div class="background {{background}}"></div>

            {% if header %}
            {% for item in header %}
                <a href="{{item.href}}">{{item.content}}</a>
            {% endfor %}
            {% endif %}

        </div>
    </li>

{% for component in content %}
    <li>
        {{component.gen()}}
    </li>
{% endfor %}
</ul>
<a href="#" data-activates="{{id}}" class="button-collapse"><i class="material-icons">menu</i></a>
""" 

        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body

    @staticmethod
    def test():
        main = container()
        content1 = \
        collections([badge(href='#!', num=1, name='今日新闻'),
                     badge(href='#!', num=4, name='鬼畜专区'),
                     badge(href='#!', name='哲学论坛'),
                     badge(href='#!', num=14, name='血条众筹'),
                     
                    ])
        content2 = \
        collapsible([(icon('filter_drama'),badge(href = '#!', name = "First") , "<p>Lorem ipsum dolor sit amet.</p>"),
                     (icon('place'),       badge(href = '#!', name = "Second"), "place")
                     ])
        side = col(sidenav([content2, content1]), grid(l=2).loffset(6))
        main.contains(side)
        return Page(main).gen()
        


app = Flask(__name__)
app.debug = True


@app.route('/<concept_component>', methods=['GET'])
def index(concept_component):
    concept, component = concept_component.split('+')
    return getattr(eval(concept), component)()


app.run('localhost')
