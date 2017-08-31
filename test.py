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
from incantation.Module.Component.Badges import collections, dropdown, badge, collapsible
from incantation.Module.Component.Icons import icon
from incantation.Module.Component.Button import FAB, raised
from incantation.Module.Component.Form import form, input_field
from incantation.Module.Component.Navbar import navbar




    
    
main  = container()

nav = navbar(
       [dict(href = 'https://baidu.com',  name = 'link1'),
        dict(href = 'https://google.com', name = 'link2')
       ],
       href = 'https://github.com/thautwarm', 
       name = 'Logo'
       )

cs = collections([badge(new = False,href = '#!', num = 1, name = 'Alan'),
                  badge(new = True, href = '#!', num = 4, name = 'Alan'),
                  badge(href = '#!', name = 'Alan'),
                  badge(new = False,href = '#!', num = 14,name = 'Alan')
                                ],
                                )


dd = dropdown([badge(new = False,href = '#!', num = 1, name = 'Alan'),
               badge(new = True, href = '#!', num = 4, name = 'Alan'),
               badge(href = '#!', name = 'Alan'),
               badge(new = False,href = '#!', num = 14,name = 'Alan')
                                ],
               name = 'a dropdown list', id = 'someid')

collap = collapsible([(icon('filter_drama'),badge(href = '#!', name = "First") , "<p>Lorem ipsum dolor sit amet.</p>"),
                      (icon('place'),       badge(href = '#!', name = "Second"), "place")
                     ])


a_col = col("contents", grid(s=6) )
a_row = row(Seq(a_col, a_col), name = "test_row")
b_row = row(Seq(col(cs, grid(s=6)), col(cs, grid(s=6).loffset(s=0, m =6, l=8))))
center_align(a_row)


a_table = table(
        ["name", "email", "phone number"],
        [
         ["thautwarm", "twshere@outlook.com", None],
         ["person1"  , "email1"             ,"phone1"], 
         ["deep"     , "dark"               ,"fantasy"],
         ["Ass"      , "Tol"                ,"Fo"]
        ],
        action = "somescirpt"
        ) 

# print(a_table.gen())
try_columns = blockquote("Columns")
try_table   = blockquote("Tables") 
fab = FAB([dict(color = 'red',  icon = icon("insert_chart"),  href = 'https://www.baidu.com'),
           dict(color = 'blue', icon = icon("publish"),       href = 'https://www.google.com'),
          ], loc = 'fixed', color = 'purple', icon = icon("publish"))

a_form = form(
            Seq(
            input_field(grid(s=12), field_name = 'Username', type = 'text',     icon = icon('mode_edit'), id = 'for-username'),
            input_field(grid(s=12), field_name = 'Password', type = 'password', icon = icon('brightness_auto'),   id = 'for-password'),
            input_field(grid(s=12), field_name = 'School',   type = 'text',     icon = icon('brightness_3'),   id = 'for-school'),
            input_field(grid(s=12), field_name = 'submit',   type = 'submit',   icon = icon('publish'),   id = 'for-submit')->> right_align,
            ),
            action = 'script',
            method = 'POST')

main.contains(Seq(try_columns, 
                  a_row, 
                  col(dd, grid(l = 12)),
                  collap, 
                  b_row, 
                  try_table, 
                  a_table, 
                  cs, 
                  fab, 
                  raised(icon = icon('add_alarm'), name = "YHZ", href = 'https://www.baidu.com'),
                  a_form
                  ))
main.setIndent(1)

page = Page( Seq(nav,main) )
page.write(to = './test.html')



#a = container()
#try_columns = blockquote("try columns")
#try_table   = blockquote("try tables") 
#t = table( ['name','email','GPA'],
#           [
#            ['thautwarm','twshere', '3.7'],
#            ['nightynight','thaut','4.0']
#           ],
#              )
#cols    = Seq(
#                col("this is column1", grid(s=12)),
#                col("and this is column2", grid(s=12))
#             )
#
#Row = row(cols)
#a.contains(Seq(try_columns, Row, try_table, t))
#a.setIndent(1)
#page = Page(a)
#print(page)
#page.write(to = './test.html')
#
#if False:
#    main  = container()
#    a_col = col("contents", grid(s=12) )
#    a_row = row(Seq(a_col, a_col), name = "test_row")
#    center_align(a_row)
#    a_row.setIndent(2)
#    print(a_row.gen())
#    a_table = table(
#        ["name", "email", "phone number"],
#        [
#            ["thautwarm","twshere@outlook.com",None],
#            ["person1", "email1", "phone1"],
#            ["deep","dark","fantasy"],
#            ["Ass","Tol","Fo"]
#        ],
#        action = "somescirpt"
#    ) 
#    try_columns = blockquote("try columns")
#    try_table   = blockquote("try tables") 
#    main.contains(Seq(try_columns, a_row, try_table, a_table))
#    page = Page(main)
#    page.write(to = './test.html')
    
    
    
    
    
    
    
    
