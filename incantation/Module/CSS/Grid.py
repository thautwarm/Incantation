from ..abs import abstract_component
class Container(abstract_component):
    def __init__(self,content,**attributes):
        body   = \
"""
{{indent}}<div class="container" {{attributes_dict_str}}>
{{indent}}<!-- Page Content goes here -->
{{indent}}{{content}}
{{indent}}</div>
"""
        self.conf = dict(content = content, indent = '',  attributes_dict = attributes)
        self.body = body

    def contains(self, content):
        self.conf["content"] = content
    
    def setIndent(self, i):
        self.conf["indent"] = i*"    " 


