#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
# License: GPL v3

def init_s(s):
    return [s,0,len(s),'']
    
def sp(p):
    s=p[0]
    x=p[1]
    c=p[2]
    if(x<c):
        l=True
        while(l):
            if s[x].strip()=='':
                x+=1
                if(x==c):
                    l=False
            else:
                l=False
    return [s,x,c,p[3]]
            
def read_token(p,ps=''):
    s=p[0]
    x=p[1]
    c=p[2]
    c1=len(ps)
    r=''
    if(x<c):
        l=True
        while(l):
            if(ps==''):
                if(s[x].strip()!=''):
                    r+=s[x]
                    x+=1
                    if(x==c):
                        l=False
                else:
                    l=False
            else:
                if(s[x:x+c1]!=ps):
                    r+=s[x]
                    x+=1
                    if(x==c-c1):
                        l=False
                else:
                    l=False
    return [s,x,c,r]
    
x=init_s('Hello World!')
x=read_token(x,'World!')
print(x[3])
