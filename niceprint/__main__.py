import sys 
from .box import makebox
from .general import NPApp

def _introduce():
    npa= NPApp()
    npa.header("NICE PRINT")
    makebox("Nice print is a Python module which allows you to nicely print text data on Windows commad prompt or Linux Terminal. It is my first python package. It's like a demo for me. I really like it.")
    npa.footer()


#def show_args(args):
#    for arg in args:
#        print("Next arg is : {}".format(arg))


if __name__=='__main__':
    _introduce()
    #args= sys.argv
    #show_args(args) 