# -*- coding: utf-8 -*-

from incantation.Module.CSS.Grid import container, col, row, grid, section
from incantation.Module.CSS.Color import Indigo 
from incantation.Module.CSS.Helpers import align, left_align, right_align
from incantation.Module import abst
from incantation.Module.abst import default_conf, gen_helper, Seq
from incantation.template import Page
a = container()
cols    = Seq(
                col("1", grid(m=6,s=12,l=12)), 
                col("2", grid(m=6,s=12,l=12)),
                col("3", grid(m=6,s=12,l=12))
            )
Row = row(cols,name = "1")
a.contains(Row)
a.setIndent(1)
page = Page(a)
print(page)
page.write()
