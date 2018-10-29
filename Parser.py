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
            if item=='+':
                result=int(item0)+int(item1)
            elif item=='*':
                result=int(item0)*int(item1)
            else:
                raise ValueError('illegal item is {}'.format(item))
            numstack.append(result)
    return numstack[0]
#mathparser('( 5 + ( ( ( 2 ) + 4 ) * 2 ) )')
#to check            
