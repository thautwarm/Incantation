# -*- coding: utf-8 -*-

from incantation.Module.CSS.Grid import container, col, row, grid, section
from incantation.Module.CSS.Color import Indigo 
from incantation.Module.CSS.Helpers import align, left_align, right_align
from incantation.Module.CSS.Media import video_container
from incantation.Module import abst
from incantation.Module.CSS.Table import table
from incantation.Module.abst import default_conf, gen_helper, Seq
from incantation.template import Page
a = container()
t = table( [
            ['thautwarm','twshere', '3.7'],
            ['nightynight','thaut','4.0']
           ],
              ['name','email','GPA'])
cols    = Seq(
                col(video_container(src =""), grid(m=6,s=12,l=12)), 
                col("2", grid(m=6,s=12,l=12)),
                col("3", grid(m=6,s=12,l=12))
            )
Row = row(cols,name = "1")
a.contains(Seq(Row, t))
a.setIndent(1)
page = Page(a)
print(page)
page.write()
