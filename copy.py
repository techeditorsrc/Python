#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: deep copy function
# License: GPL v3

def copy(p):
    r=p
    if isinstance(p,tuple):
        r=[]
        for i in p:
            r.append(copy(i))
        r=tuple(r)
        return r
    elif isinstance(p,list):
        r=[]
        for i in p:
            r.append(copy(i))
        return r
    elif isinstance(p,dict):
        r={}
        for key,value in p.items():
            r[key]=copy(value)
        return r
    else:
        return r
