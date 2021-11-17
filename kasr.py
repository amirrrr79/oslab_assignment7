class kasr:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def add(self):
        if self.b==0 or self.d==0:
          print('eror makhraj>0')
          exit()  
        if(self.b==self.d):
            sorat=self.a+self.c
            makhraj=self.d
            print('sum=',sorat,'/',makhraj) 
        else:
            sorat=(self.a*self.d)+(self.c*self.b)
            makhraj=self.b*self.d
            print('sum=',sorat,'/',makhraj)


    def sub(self):
        if self.b==0 or self.d==0:
            print('eror makhraj>0')
            exit()  
        if(self.b==self.d):
            sorat=self.a-self.c
            makhraj=self.d
            print('sub=',sorat,'/',makhraj) 
        else:
            sorat=(self.a*self.d)-(self.c*self.b)
            makhraj=self.b*self.d
            print('sub=',sorat,'/',makhraj)

        
    def multy(self):
        if self.b==0 or self.d==0:
          print('eror makhraj>0')
          exit()  
        sorat=self.a*self.c
        makhraj=self.b*self.d
        print('mul=',sorat,'/',makhraj)
          

    def divid(self):
        if self.b==0 or self.d==0:
           print('eror makhraj>0')
           exit()  
        makhraj=self.b*self.c  
        sorat=self.a*self.d
        print('divid=',sorat,'/',makhraj)
          

while True:
    print('______________________________________')  
    print('1-add')
    print('2-mul')
    print('3-sub')
    print('4-divid')
    print('5-exit')
    print('_______________________________________')
    choice=int(input('Enter choice='))
    print('_______________________________________')

    if choice==1:
      x=int(input('sorat kasr1='))
      y=int(input('makhraj kasr1='))
      w=int(input('sorat kasr2='))
      z=int(input('makhraj kasr2='))
      sorat1=int(x)
      mahkraj1=int(y)
      sorat2=int(w)
      mahkraj2=int(z)
      f=kasr(sorat1,mahkraj1,sorat2,mahkraj2)
      f.add()
    if choice==2:
      x=int(input('sorat kasr1='))
      y=int(input('makhraj kasr1='))
      w=int(input('sorat kasr2='))
      z=int(input('makhraj kasr2='))
      sorat1=int(x)
      mahkraj1=int(y)
      sorat2=int(w)
      mahkraj2=int(z)
      f=kasr(sorat1,mahkraj1,sorat2,mahkraj2)
      f.multy()
    if choice==3:
      x=int(input('sorat kasr1='))
      y=int(input('makhraj kasr1='))
      w=int(input('sorat kasr2='))
      z=int(input('makhraj kasr2='))
      sorat1=int(x)
      mahkraj1=int(y)
      sorat2=int(w)
      mahkraj2=int(z)
      f=kasr(sorat1,mahkraj1,sorat2,mahkraj2)
      f.sub()
    if choice==4:
      x=int(input('sorat kasr1='))
      y=int(input('makhraj kasr1='))
      w=int(input('sorat kasr2='))
      z=int(input('makhraj kasr2='))
      sorat1=int(x)
      mahkraj1=int(y)
      sorat2=int(w)
      mahkraj2=int(z)
      f=kasr(sorat1,mahkraj1,sorat2,mahkraj2)
      f.divid()
    if choice==5:
        print('good by')  
        exit()

       


        
        
    


