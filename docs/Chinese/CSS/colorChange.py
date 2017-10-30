from incantation.template import Page 
from incantation.Module.abst import Seq

from incantation.Module.CSS.Color import color, Teal
from incantation.Module.CSS.Grid import container, col, row, grid, divider
from incantation.Module.Component.Navbar import navbar

from flask import Flask, g, request, render_template, url_for, redirect
app = Flask(__name__)
app.debug = True

@app.route('/<ucolor>', methods=['GET'])
def index(ucolor):
    space = '&nbsp;'
    main = container()

    bar = navbar([
                  {'name':'百度', 'href':'https://www.baidu.com'},
                  dict(name = 'Glgoo', href='https://scholar.glgoo.org/'),
                  ], 
                href='#Bar', name = f'{space*5}Bar')
    
    html_color = color(major = ucolor).gen()

    bar.cons_class(html_color) # 从对象class的头部添加值

    main.contains(bar)
    return Page(main).gen()



app.run('localhost')