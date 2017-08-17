
def color(major  :"blue,red,yellow, ..."     = "blue",
          degree : "lighten, darken, accent" = "lighten",
          micro  :"int, None" = 1):
    return lambda : f"{major} {degree}-{micro}"
    
class color:
        def __init__(self, major  : "blue,red,yellow, ..."     = "blue",
                           degree : "lighten, darken, accent" = "lighten",
                           micro  : "int, None" = 1):
        self.conf = dict(major = major , degree = degree, micro = micro)

        def setIndent(self, i):pass
        
    


    

