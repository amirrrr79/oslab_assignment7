import random

b=[]
g=[]
result=[]
boys=['ali','reza','yasin','benyamin','mehrdad','sajjad','aidin','shahin']
girls=['sara','zari','neda','homa','eli','goli','mari','mina']

for i in range(8):
    while len(b)!=len(boys) or len(g)!=len(girls):
        boy=random.choice(boys)
        girl=random.choice(girls)
        if boy not in b:
            b.append(boy)
        if girl not in g:
            g.append(girl)
for  i in range(8):
    p=(b[i],g[i])
    result.append(p)
    
print('result=',result)  
                              
    
    
    
   
             



    
                







