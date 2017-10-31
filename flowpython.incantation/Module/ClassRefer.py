#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 16:04:07 2017

@author: misakawa
"""

class indicates:
    content = dict()
    def log(name, explanation, url):
        indicates.content[name] = dict(explanation = explanation, doc_url = url)
indicates.log('Pulse',  expl, 'http://materializecss.com/pulse.html') where:
    expl = ["btn btn-floating pulse",
            "btn btn-floating btn-large pulse", 
            "btn btn-floating btn-large cyan pulse"]

indicates.log('Shadow', expl, 'http://materializecss.com/shadow.html') where:
    expl = ['z-depth-1','z-depth-<int>']
    
indicates.log("Transitions", expl, 'http://materializecss.com/css-transitions.html') where:
    expl = ['scale-transition', 'scale-out', 'scale-in', 'flow-text']


    
    
    
    