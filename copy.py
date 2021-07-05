#  Author: cat_prog
#  Source:https://github.com/techeditorsrc
#    Info: parser to create dictionary from string
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
