from ..abst import abstract_object,indent_setter, Seq, default_attr

class container(indent_setter, abstract_object):
    """
    See http://materializecss.com/grid.html.
    use help : >> help (container.init)
    """
    
    @default_attr(attr = "class", value = "container")
    def init(self, content = "" , **attributes):
        body   = \
"""
{{indent}}<div {{attributes_dict}}>
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
    
    @default_attr(attr = "class", value = "row")
    def init(self, content : Seq , **attributes):
        body = \
"""
{{indent}}<div {{attributes_dict}}>
{{indent}}{% for item in content %}
{{indent+Indent_unit}}{{item}}
{{indent}}{% endfor %}
{{indent}}</div>
"""
        self.conf.update(dict(content = content, indent = " ", attributes_dict = attributes))
        self.body = body

class col(indent_setter, abstract_object):
    """
    See http://materializecss.com/grid.html.
    use help : >> help (col.init)
    """
    def init(self, content, hold : dict(s = int , m = int, dict = int) , **attributes):
        body =\
"""
{{indent}}<div {{attributes_dict}}>
{{indent+Indent_unit}}{{content}}
{{indent}}</div>
"""
        dic = {"class": f"col s{hold['s']} m{hold['m']} l{hold['l']}" }
        attributes.update(dic)
        self.conf.update(dict(content = content, indent = " ", attributes_dict = attributes))
        self.body = body
    


