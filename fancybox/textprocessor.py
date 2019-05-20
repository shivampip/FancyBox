

def divide(text, n):
    count= 0
    out= []
    while(count<len(text)):
        if(len(text)>=count+n):
            ch= text[count+n]
        else:
            ch= ' '
        if(ch!=' '):
            index= text[count: count+ n].rindex(' ')
            temp= text[count: count+index]
            count+= len(temp) 
        else:
            temp= text[count: count+n]
            count+=n 
        out.append(temp.strip())
    return out 