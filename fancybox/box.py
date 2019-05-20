from .textprocessor import divide
from .style import BOLD, FG_8BIT, BG_8BIT, END


class Box:
    def __init__(self):
        self.n= 50
        self.padding= 10
        self.fgcolor= 17
        self.bgcolor= 51
        self.border= 17

    def _print_line(self, text, lines=('┃','┃')):
        n= self.n-2
        rs= n-len(text)
        even= False 
        if(rs%2==0):
            even= True 
        rs= int(rs/2)

        print(lines[0], end="")
        print(FG_8BIT.format(self.fgcolor), end= "")
        print(' '*rs, end= "")
        print(text, end= "")
        if(even):
            print(' '*rs, end= "")
        else:
            print(' '*(rs+1), end= "")
        print(FG_8BIT.format(self.border), end="")    
        print(lines[1])


    def makebox(self, text):
        print(BOLD+FG_8BIT.format(self.border)+BG_8BIT.format(self.bgcolor), end="")
        print('▛', end= "")
        print('▀'*(self.n-2), end="")
        print('▜')

        for tt in divide(text, self.n-10):
            self._print_line(tt, lines=('▌','▐'))

        print(FG_8BIT.format(self.border), end="")
        print('▙', end="")
        print('▄'*(self.n-2), end="")
        print('▟')
        print(END, end="")

    def addbox(self, text):
        print(BOLD+FG_8BIT.format(self.border)+BG_8BIT.format(self.bgcolor), end="")

        self._print_line("", lines=('▌','▐'))
        for tt in divide(text, self.n-10):
            self._print_line(tt, lines=('▌','▐'))

        print(FG_8BIT.format(self.border), end="")
        self._print_line("", lines=('▌','▐'))
        print('▙', end="")
        print('▄'*(self.n-2), end="")
        print('▟')
        print(END, end="")

    def makeboxwithheadbold(self, title, text, n=50):
        self.makebox(title)
        self.addbox(text)
        

        








