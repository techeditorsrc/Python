#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: CPU 6502 Emulator Beta
# License: GPL v3

#What did:
#Main class, CPU 6502 structure, status class

#Roadmap:
#Parser

class flag():
    value=0
    name=''
    def set(self,r=True):
        if r:
            self.value=1
    
    def get(self):
        return self.value
    
    def clear(self):
        self.value=0

class status():
    def __init__(self,flag_count,flag_names=None):
        self.count=flag_count
        self.flag=[]
        for x in range(flag_count):
            self.flag.append(flag())
        if(flag_names):
            c=self.count-1
            for x in flag_names:
                if(x!=''):
                    setattr(self,x,c)
                    self.flag[c].name=x
                c=c-1

    def find(self,flag_name):
        c=self.count-1
        for x in self.flag:
            if(x.name==flag_name):
                return x
            c-=1
        return None

    def iter(self,call,flags):
        if(len(flags)==0):
            for x in self.flag:
                    call(x)
        else:
            for x in flags:
                flagType=type(x)
                if(flagType==int):
                    call(self.flag[x])
                elif(flagType==str):
                    call(self.find(x))
                else:
                    call(x)

    def set(self,*flags):
        def call(x):
            x.set()
        self.iter(call,flags)

    def clear(self,*flags):
        def call(x):
            x.clear()
        self.iter(call,flags)

    def get(self,flag):
        flagType=type(flag)
        if(flagType=='int'):
            return self.flag[flag]
        elif(flagType=='str'):
            return self.find(flag)
    
    def toInt(self):
        r=0
        for x in range(self.count):
            r=r & (self.flag[x] << x)
        return r
    
    def fromInt(self,value):
        for x in range(self.count):
            self.flag[x]=(value >> x) & 1

    def read_addr(self,addr):
        pass

    def write_addr(self,addr):
        pass

class cpu6502():
    def __init__(self):
        self.a=0
        self.x=0
        self.y=0
        self.pc=0
        self.s=0
        #status flag from 7 to 0 bit
        # self.p=[0,0,0,0,0,0,0,0]
        self.p=status(8,['negative','overflow','','break','decimal','interruptdisable','zero','carry'])

x=status(8,['negative','overflow','','break','decimal','interruptdisable','zero','carry'])
x.set('overflow','break',7)
s=''
for x in reversed(x.flag):
    if x.name=='':
        s1='-'
    else:
        s1=x.name
    s=s+f"{s1}={x.get()} "
print(s)
