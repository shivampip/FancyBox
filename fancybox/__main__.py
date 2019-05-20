import sys 

from .box import Box 

def _introduce():
    print("")

    box= Box()
    box.border= 117
    box.bgcolor= 17
    box.fgcolor= 14
    
    title= "FANCY BOX"
    description= "Fancy Box is a Python module that allows you to print beautiful message boxes on command line. There are predefined message boxes, you can use or you can create you own custom box."
    box.makeboxwithheadbold(title, description)
    print("")
    
    

if __name__=='__main__':

    _introduce()