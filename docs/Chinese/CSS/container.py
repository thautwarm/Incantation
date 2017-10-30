from incantation.template import Page 
from incantation.Module.CSS.Grid import container, row
from incantation.Module.CSS.Color import color
from flask import Flask
app = Flask(__name__)
app.debug = True
def my_page(hasContainer:bool):
    a_row = row("This is a row.")
    a_row.cons_class(color('red').gen())

    if hasContainer:
        main = container()
        main.contains(a_row)
        res = main
    else:
        res = a_row
    return Page(res).gen()
@app.route('/<hasContainer>', methods=['GET'])
def index(hasContainer):
    return my_page(hasContainer == 'hasContainer')
app.run('localhost')