from ..abst import abstract_object,indent_setter, Seq

class container(indent_setter, abstract_object):
    """
    See http://materializecss.com/grid.html.
    use help : >> help (container.init)
    """
    
    def init(self, content, **attributes):
        body   = \
"""
{{indent}}<div class="container" {{attributes_dict}}>
{{indent}}<!-- Page Content goes here -->
{{indent+Indent_unit}}{{content}}
{{indent}}</div>
"""
        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body

    def contains(self, content):
        self.conf["content"] = content
        
    
class row(indent_setter, abstract_object):
    """
    See http://materializecss.com/grid.html.
    use help : >> help (grid.init)
    """
    def init(self, content : Seq, **attributes):
        body = \
"""
{{indent}}<div class="row" {{attributes_dict}}>
{{indent}}{% for item in content %}
{{indent+Indent_unit}}{{item}}
{{indent}}</div>
"""
        self.conf.update(dict(content = content, indent = " ", attributes_dict = attributes))
        self.body = body
        
    
    


