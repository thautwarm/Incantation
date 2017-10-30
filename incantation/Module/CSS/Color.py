from ..abst import abstract_object

class color:
        """
        Number of input arguments should be 1 or 3.
        See http://materializecss.com/color.html.
        """
        def __new__(major  : "blue,red,yellow, ..."     = "blue",
                    degree : "lighten, darken, accent"  = "",
                    micro  : "int, None" = ""):
            if degree and micro:
                return f"{{major}} {{degree}}-{{micro}}"
            else:
                return f"{{major}}"
                

            
Red    = color( major = 'red'   )
Pink   = color( major = 'pink'  )
Purple = color( major = 'purple')
Indigo = color( major = 'indigo')
Blue   = color( major = 'blue'  )
Cyan   = color( major = 'cyan'  )
Teal   = color( major = 'teal'  )
Green  = color( major = 'green' )
Lime   = color( major = 'lime'  )
Yellow = color( major = 'yellow')
Amber  = color( major = 'amber' )
Orange = color( major = 'orange')
Brown  = color( major = 'brown' )

BlueGrey   = color( major = 'blue-grey'    )
LightGreen = color( major = 'light-green'  )
LightBlue  = color( major = 'light-blue'   )
DeepPurple = color( major = ' deep-purple' )
       
  
    
    



    

