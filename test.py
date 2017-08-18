# -*- coding: utf-8 -*-

from incantation.Module.CSS.Grid import container, col, row, grid, section
from incantation.Module.CSS.Color import Indigo 
from incantation.Module import abst
from incantation.Module.abst import default_conf, gen_helper, Seq
a = container()
a.contains(container("1,2,3"))
a.setIndent(1)
print(a.gen())

cols    = Seq(
                col("1", grid(m=6,s=12,l=12)), 
                col("2", grid(m=6,s=12,l=12)),
                col("3", grid(m=6,s=12,l=12))
            )

print (row(cols,name = 1).setIndent(1).gen())
print(section("content").setIndent(1).gen())

