# -*- coding: utf-8 -*-

def align(self):
    if self -> not hasattr(_, 'align_setted'):
        self.align_setted = True
    else:
        raise BaseException("Alignment has been set twice!!!")
    def _f(mode):
        mode = mode.replace(" ","")
        if mode not in ("left","right", "center"):
            raise ValueError('''Found align-mode not in  ("left","right", "center")!!!''')
        self.cons_attr('class')(mode+'-align')
        return self
    return _f

def left_align(self):
    return align(self)("left")

def right_align(self):
    return align(self)("right")

def center_align(self):
    return align(self)("center")

    