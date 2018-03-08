from pprint import pprint

import incantation as inc

color = inc.Color('red').lighten_by(-3)
print(str(
    inc.Container(color,
                  "123",
                  inc.Grid(s=2),
                  inc.Push(s=2)
                  ).set_indent(1).append(color)
))


print(inc.Align.vertical)
print(inc.Video('//www.youtube.com/embed/Q8TXgCzxEnw?rel=0').set_indent(1))

print(inc.ResponseVideo('//www.youtube.com/embed/Q8TXgCzxEnw?rel=0').append(inc.ZDepth(2).rise(2)).set_indent(1))


print(inc.Th())

x = str(inc.Table([[1, 2, 3], [2, 3, 4]], ['a', 'b', 'c'], index=[1, 2]).set_indent(0))
inc.DropdownButton.help()

x = inc.Dropdown(id='dropdown2')
print(x)
print(x.link())
inc.Dropdown.help()