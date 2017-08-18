from ..abst import abstract_component

class color(abstract_component):
        """
        Number of input arguments should be 1 or 3.
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
DeepPurple \
       = color( major = ' deep-purple' )
Indigo = color (major = 'indigo')
  
    
    



    

