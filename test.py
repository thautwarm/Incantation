# -*- coding: utf-8 -*-

from incantation.Module.CSS.Grid import Container 
from incantation.Module import abs
a = Container("1,2,3")
a.contains(Container("2,3,4"))
a.setIndent(2)
print(a.gen())