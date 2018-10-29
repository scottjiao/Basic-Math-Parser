#utils  
def trackToSubTreeRoot(node):
    temp=node
    while True:
        if temp.parent==None or temp.parent.val=='':
            break
        temp=temp.parent
    return temp
#utils 
def trackToRoot(node):
    temp=node
    while True:
        if temp.parent==None:
            break
        temp=temp.parent
    return temp

#utils 
def trackToSubTreeRightLeaf(node):
    if node.val=='':
        return node
    temp=trackToSubTreeRoot(node)
    while True:
        if temp.right==None or temp.right.val=='':
            break
        temp=temp.right
        
    return temp
#utils         
class node(object):
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right =None
        self.parent=None
    def generateLeft(self,y):
        self.left=node(y)
        self.left.parent=self
        return
    def generateRight(self,y):
        self.right=node(y)
        self.right.parent=self
        return
    def generateParentFromRight(self,x):
        self.parent=node(x)
        self.parent.left=self
    def generateParentFromLeft(self,x):
        self.parent=node(x)
        self.parent.right=self
#utils 
def constructTreeFromInFix(str_in):
    if str_in=='':
        return None
    j=0
    i=0
    buffer=''
    #先建立列表
    str_list=[]
    while True:
        if i>=len(str_in):
            if buffer:
                str_list.append(buffer)
            break
        if str_in[i]!=' ':
            buffer+=str_in[i]
            j=1
        else:
            if j==1:
                str_list.append(buffer)
                buffer=''
            j=0
        i+=1
    #return str_list
    '''
    定理：
    +与*之前一定是二叉张满子树
    Design Rules:
        '*':
            溯至最右下部分
            把当前位置结点替换为'*'结点,其左子节点为原结点，temp指向'*'
        '+':
            首先回溯至子树顶，若有parent '' ，那么在子树顶与parent之间插入一个'+'并指向它，
            若无，则增加一个右parent结点'+'并指向它
        ')':
            回溯至子树顶，指向子树顶的'' node的parent(如果有的话，没有就指向自己)
        '(':
            断言：一定是非张满子树，并且temp指向一个运算符结点或者是''结点
            运算符结点右字结点加一个''结点，然后指向它
            ''结点左边字结点加一个''结点，然后指向它
        'num':
            总是插入右边，右边没有空位则报错,指向本结点
    '''
    #建立后面的结点
    for i in range(len(str_list)):
        #循环体在这里开始
        if i:
            if str_list[i]=='+':
                temp=trackToSubTreeRoot(temp)
                if temp.parent==None:
                    temp.generateParentFromRight('+')
                    temp=temp.parent
                elif temp.parent.val=='':
                    parent=temp.parent
                    new=node('+')
                    parent.left=new
                    new.parent=parent
                    new.left=temp
                    temp.parent=new
                    temp=temp.parent
            elif str_list[i]=='*':
                #print(temp.val,i)
                temp=trackToSubTreeRightLeaf(temp)
                #print(temp.val,i)
                new=node('*')
                parent=temp.parent
                if parent.right is temp:
                    #print(temp.val,i)
                    parent.right=new
                    new.parent=parent
                    new.left=temp
                    temp.parent=new
                    temp=temp.parent
                elif parent.left is temp:
                    #print(temp.val,i)
                    parent.left=new
                    new.parent=parent
                    new.left=temp
                    temp.parent=new
                    temp=temp.parent
            elif str_list[i]=='(':
                if temp.val=='':
                    new=node('')
                    temp.left=new
                    new.parent=temp
                    temp=temp.left
                elif temp.val!='':
                    new=node('')
                    temp.right=new
                    new.parent=temp
                    temp=temp.right
                    
            elif str_list[i]==')':
                temp=trackToSubTreeRoot(temp)
                temp=temp.parent
            else:
                if temp.right==None:
                    temp.generateRight(str_list[i])
                    temp=temp.right
                elif  temp.left==None:
                    temp.generateLeft(str_list[i])
                    temp=temp.left
                else:
                    raise ValueError('no space for new num')
            if temp==None:
                print(i)
                raise ValueError    
        #最开始的case
        else:
            if str_list[i]=='(':
                temp=node('')
            elif str_list[i] and str_list[i]!='(':
                temp=node(str_list[i])
                
    root=trackToRoot(temp)
    return root
#utils 
def fromTreeToPostFix(rootNode,L):
    #use post tranversal
    if rootNode:
        fromTreeToPostFix(rootNode.left,L)
        fromTreeToPostFix(rootNode.right,L)
        L.append(rootNode.val)
            
def infix2postfix(str_in):
    """
    :type str_in: str
    :rtype: str
    """
    #construct binary tree by infix
    #property: every number has to be the leaf node
    rootNode=constructTreeFromInFix(str_in)
    L=[]
    fromTreeToPostFix(rootNode,L)
    L=[l for l in L if l!='']
    return ' '.join(L)
    
#L=infix2postfix(str_in)
