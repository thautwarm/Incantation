import incantation as inc

color = inc.Color('red').lighten_by(-3)
# print(color.__doc__)
print(str(
    inc.Container(color,
                  "123",
                  inc.Grid(s=2),
                  inc.Push(s=2)
                  ).set_indent(1)
))


print(inc.Align.vertical)

print(inc.Video('//www.youtube.com/embed/Q8TXgCzxEnw?rel=0').set_indent(1))

print(inc.ResponseVideo('//www.youtube.com/embed/Q8TXgCzxEnw?rel=0').set_indent(1))