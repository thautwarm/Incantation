# -*- coding: utf-8 -*-

from incantation.Module.CSS.Grid import container, col, row, grid, section
from incantation.Module.CSS.Color import Indigo 
from incantation.Module.CSS.Helpers import align, left_align, right_align, center_align
from incantation.Module.CSS.Media import video_container
from incantation.Module import abst
from incantation.Module import blockquote
from incantation.Module.CSS.Table import table
from incantation.Module.abst import default_conf, gen_helper, Seq
from incantation.template import Page



a = container()
try_columns = blockquote("try columns")
try_table   = blockquote("try tables") 
t = table( ['name','email','GPA'],
           [
            ['thautwarm','twshere', '3.7'],
            ['nightynight','thaut','4.0']
           ],
              )
cols    = Seq(
                col("this is column1", grid(s=12)),
                col("and this is column2", grid(s=12))
             )

Row = row(cols)
a.contains(Seq(try_columns, Row, try_table, t))
a.setIndent(1)
page = Page(a)
print(page)
page.write(to = './test.html')

if False:
    main  = container()
    a_col = col("contents", grid(s=12) )
    a_row = row(Seq(a_col, a_col), name = "test_row")
    center_align(a_row)
    a_row.setIndent(2)
    print(a_row.gen())
    a_table = table(
        ["name", "email", "phone number"],
        [
            ["thautwarm","twshere@outlook.com",None],
            ["person1", "email1", "phone1"],
            ["deep","dark","fantasy"],
            ["Ass","Tol","Fo"]
        ],
        action = "somescirpt"
    ) 
    try_columns = blockquote("try columns")
    try_table   = blockquote("try tables") 
    main.contains(Seq(try_columns, a_row, try_table, a_table))
    page = Page(main)
    page.write(to = './test.html')
    
    
    
    
    
    
    
    
    
    
    
