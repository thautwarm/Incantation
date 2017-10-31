from incantation.template import Page 
from incantation.Module.abst import Seq
from incantation.Module.CSS.Grid import  row, grid, col
from incantation.Module.CSS.Color import color
from incantation.Module.CSS.Table import table
from flask import Flask
app = Flask(__name__)
app.debug = True
def my_page(gridNum):
    gridNum = int(gridNum)
    table_example = table(["A","B","C"],
                          [[1,2,3],
                           [2,3,4],
                           [5,6,7]
                          ]).cons_class('striped')
    

    a_row = row(
                Seq(
                    col(table_example, grid(l = gridNum)),
                    col(table_example, grid(l = 12-gridNum)),
                    )
                )
    return Page(a_row).gen()
@app.route('/<gridNum>', methods=['GET'])
def index(gridNum):
    return my_page(gridNum)
app.run('localhost')