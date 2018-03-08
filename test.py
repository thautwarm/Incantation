import incantation as inc

color = inc.Color('red').lighten_by(-3)
print(str(color))

print(str(
    inc.Container(color,
                  inc.Grid(s=2),
                  inc.Push(s=2)
                  )
))
