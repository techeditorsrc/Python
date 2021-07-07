#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: can be used for styles
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

p_str,p_int,p_float,p_bool=0,1,2,3

def param(param_type,param_value):
    return {'type':param_type,'value':param_value}

def add_style(l,style_name,param_name,param_type,param_value):
    if not style_name in l:
        l[style_name]={}
    l[style_name][param_name]=param(param_type,param_value)
    return l

def read_param(l,style_name,param_name,default_value):
    if style_name in l:
        if param_name in l[style_name]:
            return l[style_name][param_name]
        else:
            return default_value
    else:
        return default_value

def copy_style(l,style_name):
    r={}
    if style_name in l:
        r=copy(l[style_name])
    return r

def combine_param(l,style_name,l2):
    if not style_name in l:
        l[style_name]={}
    for key,value in l2:
        l[style_name][key]=value
    return l

def search_param_substr(p,s):
    r=True
    x=0
    for i in s:
        if p[x:x+1]!=i:
            r=False
            break
        x+=1
    return r

def exclude_param(l,style_name,*p):
    if style_name in l:
        for i in p:
            if i[-1:]=='*':
                print('ok')
                j=i[:-1]
                print(j)
                loop=True
                while(loop):
                    loop=False
                    for key,value in l[style_name].items():
                        if search_param_substr(key,j):
                            del l[style_name][key]
                            loop=True
                            break
            else:
                for key,value in l[style_name].items():
                    if key==i:
                        del l[style_name][key]
                        break
    return l

def delete_style(l,style_name):
    if style_name in l:
        del l[style_name]
    return l


class app():
    def __init__(self):
        pass

style={}
style=add_style(style,'style1','align-left',p_str,'left')
style=add_style(style,'style1','align-right',p_str,'right')
style=add_style(style,'style1','padding',p_int,10)
style=add_style(style,'style1','padding-top',p_int,10)
style=exclude_param(style,'style1','align*')
print(style)
