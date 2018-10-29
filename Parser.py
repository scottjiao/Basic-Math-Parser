from utils import *


def mathparser(str_in):
    postfix=infix2postfix(str_in)
    L=postfix.split(' ')
    numstack=[]
    while True:
        if L==[]:
            break
        item=L.pop(0)
        if item not in ['+','*']:
            #等价于push
            numstack.append(item)
        else:
            item0=numstack.pop(-1)
            item1=numstack.pop(-1)
            result=str(eval(item0+item+item1))
            numstack.append(result)
    return numstack[0]
#mathparser('( 5 + ( ( ( 2 ) + 4 ) * 2 ) )')
#to check            
