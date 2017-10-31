from incantation.template import Page 
from incantation.Module.abst import Seq
from incantation.Module.CSS.Grid import divider, section, container
from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def index():
    main = container()
    main.contains(
                Seq(section('<h5>A</h5><p>a</p>'),
                    divider(),
                    section('<h>B</h><p>b</p>')
                    )
                )
    return Page(main).gen()

app.run('localhost')
