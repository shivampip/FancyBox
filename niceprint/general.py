
class NPApp:
    def __init__(self):
        self.n= 50

    def setn(self, n):
        self.n= n

    def header(self, text, c= " "):
        sl= int((self.n-len(text))/2)
        print('-'*self.n)
        print(c*sl, end= "")
        print(text, end= "")
        print(c*sl)
        print('-'*self.n)


    def body(self, text):
        count= 0
        while(count<len(text)):
            if(len(text)>=count+self.n):
                ch= text[count+self.n]
            else:
                ch= ' '
            if(ch!=' '):
                index= text[count: count+ self.n].rindex(' ')
                temp= text[count: count+index]
                count+= len(temp) 
            else:
                temp= text[count: count+self.n]
                count+=self.n 
            print(temp.strip()) 


    def footer(self):
        print('-'*self.n)
        print('-'*self.n)
