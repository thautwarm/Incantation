# -*- coding: utf-8 -*-

from incantation.Module.CSS.Grid import container, col, row
from incantation.Module.CSS.Color import Indigo 
from incantation.Module import abst
from incantation.Module.abst import default_conf, gen_helper, Seq
a = container()
a.contains(container("1,2,3"))
a.setIndent(1)
print(a.gen())

cols    = Seq(
                col("1", dict(m=6,s=12,l=12)), 
                col("2", dict(m=6,s=12,l=12)),
                col("3", dict(m=6,s=12,l=12))
            )

print (row(cols,name = 1).setIndent(2).gen())
