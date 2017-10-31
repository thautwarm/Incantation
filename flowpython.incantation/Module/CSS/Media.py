# -*- coding: utf-8 -*-
from ..abst import abstract_object,indent_setter, default_attr

class img(indent_setter, abstract_object):
    """
    See http://materializecss.com/media-css.html
    user help : >> help (img.init)
    ------------------------------
        Guide:
            >> im = img(src = "cool_pic.jpg")
            >> im.append_class("responsive-img")
            >> im.append_class("class")
        which equals:
            >> im = img(**{'src': 'cool_pic.jpg', 'class':'responsive-img class'})
    """
    def init(self, **attributes):
        body = \
"""
{{indent}}<img  {{attributes_dict}}>
"""
        self.conf.update(dict(indent = " ", attributes_dict=attributes))
        self.body = body
        

class video_container(indent_setter, abstract_object):
    """
    See http://materializecss.com/media-css.html
    user help : >> help (video_container.init)
    ------------------------------
        Guide:
            >> video = video_container(src = "//www.youtube.com/embed/Q8TXgCzxEnw?rel=0")
            
        Take care that `video_container` takes some default arguments:
            
            video = video_container(src = "//www.youtube.com/embed/Q8TXgCzxEnw?rel=0")
        equals 
            video = video_container(src   = "//www.youtube.com/embed/Q8TXgCzxEnw?rel=0",
                                    width = 853,
                                    height= 480,
                                    frameborder = 0)
    """
    @default_attr(attr = 'frameborder', value = "0")
    @default_attr(attr = 'width' , value = "853")
    @default_attr(attr = 'height', value = "480")
    def init(self, **attributes):
        body = \
"""
{{indent}}<div class="video-container">
{{indent+Indent_unit}}<iframe {{attributes_dict}} allowfullscreen></iframe>
{{indent}}</div>
"""
        self.conf.update(indent = " ", attributes_dict = attributes)
        self.body = body
        
class responsive_video(indent_setter, abstract_object):
    """
    See http://materializecss.com/media-css.html
    user help : >> help (video_container.init)
    ------------------------------
        Guide:
            >> video = responsive_video(src = "movie.mp4")
        which equals:
            >> video = responsive_video(src = "movie.mp4", type = "video/mp4")
    """
    
    @default_attr(attr = 'type', value = 'video/mp4')
    def init(self, **attributes):
        body = \
"""
{{indent}}<video class="responsive-video" controls>
{{indent+Indent_unit}}<source {{attributes_dict}}>
{{indent}}</video>
"""
        self.conf.update(indent = " ", attributes_dict = attributes)
        self.body = body

    
        
        
        
        
        