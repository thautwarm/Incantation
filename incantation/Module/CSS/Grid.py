from ..abs import abstract_component,indent_setter

class Container(indent_setter, abstract_component):
    def init(self,content,**attributes):
        body   = \
"""
{{indent}}<div class="container" {{attributes_dict_str}}>
{{indent}}<!-- Page Content goes here -->
{{indent+Indent_unit}}{{content}}
{{indent}}</div>
"""
        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body

    def contains(self, content):
        self.conf["content"] = content
    
    


