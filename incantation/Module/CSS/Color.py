from ..abst import abstract_object

class color(abstract_object):
        """
        Number of input arguments should be 1 or 3.
        See http://materializecss.com/color.html.
        """
        def init(self,  major  : "blue,red,yellow, ..."     = "blue",
                        degree : "lighten, darken, accent"  = "",
                        micro  : "int, None" = ""):
            if degree and micro:
                self.conf.update(dict(major = major , degree = degree, micro = micro))
                self.body = "{{major}} {{degree}}-{{micro}}"
            else:
                self.conf.update(dict(major = major))
                self.body = "{{major}}"

            
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
       
  
    
    



    

