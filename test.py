# -*- coding: utf-8 -*-

from incantation.Module.CSS.Grid import container 
from incantation.Module.CSS.Color import Indigo 
from incantation.Module import abst
from incantation.Module.abst import default_conf, gen_helper
a = container("1,23,", **{"class": "1"} )
a.contains(container("1,2,3"))
a.setIndent(1)
print(a.gen())