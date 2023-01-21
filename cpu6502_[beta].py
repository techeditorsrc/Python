#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: CPU 6502 Emulator Beta
# License: GPL v3

#What did:
#Main class, CPU 6502 structure

#Roadmap:
#Parser

class flag():
    def __init__(self,flags=[]):
        self.flags=flags
        self.flag=[0]*len(self.flags)

    def set_flag(self,index,value):
        if index in range(len(self.flags)):
            self.flag[index]=value

    def set(self,*flags):
        l=len(self.flag)
        if l>0:
            for x in flags:
                x1=type(x)
                if x1==int:
                    self.set_flag(x,1)
                elif x1==str:
                    self.set_flag(self.flags.index(x),1)
        else:
            for x in range(l):
                self.flag[x]=1

    def clear(self,*flags):
        l=len(self.flag)
        if l>0:
            for x in flags:
                x1=type(x)
                if x1==int:
                    self.set_flag(x,0)
                elif x1==str:
                    self.set_flag(self.flags.index(x),0)
        else:
            for x in range(l):
                self.flag[x]=0

    def get(self,flag):
        r=0
        x=type(flag)
        l=len(self.flag)
        if x==int:
            if flag in range(l):
                r=self.flag[flag]
        elif x==str:
            index=self.flags.index(flag)
            if index in range(l):
                r=self.flag[index]
        return r

    def if_flag(self,flag):
        return self.get(flag)==1

    def to_int(self):
        r=0
        for x in self.flag:
            r=(r << 1)or(x)
        return r
    
    def from_int(self,i):
        l=len(self.flag)
        self.clear()
        for x in range(l):
            self.flag[-1-x]=i and 1
            i>>=1

class cpu6502():
    def __init__(self):
        self.x=0
        self.y=0
        self.a=0
        self.cmd=["ADC","AND","ASL","BCC","BCS","BEQ","BIT","BMI","BNE","BPL","BRK","BVC","BVS","CLC","CLD","CLI","CLV","CMP","CPX","CPY","DEC","DEX","DEY","EOR","INC","INX","INY","JMP","JSR","LDA","LDX","LDY","LSR","NOP","ORA","PHA","PHP","PLA","PLP","ROL","ROR","RTI","RTS","SBC","SEC","SED","SEI","STA","STX","STY","TAX","TAY","TSX","TXA","TXS","TYA"]
        self.flag=flag(['n','v','_','b','d','i','z','c'])
    
    def if_carry(self):
        return self.flag.if_flag('c')
    
    def if_zero(self):
        return self.flag.if_flag('z')

    def is_int(self,s):
        l=len(s)
        r=l>0
        if r:
            if s[0]=='-':
                s=s[1:]
                l=len(s)
                r=l>0 and s.count('-')==0
            if r:
                d='0123456789'
                for x in s:
                    if not x in d:
                        r=False
                        break
        return r

    def is_hex(self,s):
        s1=s.lower()
        if s1[0]=='$':
            s1=s1[1:]
        r=len(s1)>0                
        if r:
            d='0123456789abcdef'
            for x in s1:
                if not x in d:
                    r=False
                    break
        return r

    def is_oct(self,s):
        s1=s.lower()
        if s1[0]=='o':
            s1=s1[1:]
        r=len(s1)>0
        if r:
            d='0123457'
            for x in s1:
                if not x in d:
                    r=False
                    break
        return r

    def is_bin(self,s):
        s1=s.lower()
        if s1[0]=='b':
            s1=s1[1:]
        r=len(s1)>0
        if r:
            d='01'
            for x in s1:
                if not x in d:
                    r=False
                    break
        return r

    def to_int(self,s):
        sign=1
        r=0
        s1=10
        if(s[0]=='-'):
            sign=-1
            s=s[1:]
        if s[0]=='$':
            s=s[1:]
            s1=16
        elif s[0]=='b':
            s=s[1:]
            s1=2
        elif s[0]=='o':
            s=s[1:]
            s1=8
        return int(s,s1)*sign
