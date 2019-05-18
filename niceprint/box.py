from .textprocessor import divide

def _print_line(text, n):
    n= n-2
    rs= n-len(text)
    even= False 
    if(rs%2==0):
        even= True 
    rs= int(rs/2)
    
    print('|', end="")
    print(' '*rs, end= "")
    print(text, end= "")
    if(even):
        print(' '*rs, end= "")
    else:
        print(' '*(rs+1), end= "")
    print('|')



def makebox(text, n=50):
    print('_'*n)
    print('|', end="")
    print(' '*(n-2), end="")
    print('|')

    for tt in divide(text, n-10):
        _print_line(tt, n)
    
    print('|', end="")
    print('_'*(n-2), end="")
    print('|')
    print("")



