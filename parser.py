#   Author: cat_prog
#  Website: https://cat-prog.itch.io/
#     Info: arser to create dictionary from string
#Parameter convert automaticaly convert string values to variable format
#License: GPL v3


def chars_in_str(p1,p2):
    c=True
    for i in p1:
        if i not in p2:
            c=False
            break
    return c

def str_int(p):
    if chars_in_str(p,'-0123456789'):
        r=(True,int(p))
    else:
        r=(False,p)
    return r

def str_float(p):
    if '.' in p:
        if chars_in_str(p,'-0123456789.'):
            r=(True,float(p))
        else:
            r=(False,p)
    else:
        r=(False,p)
    return r

def str_bool(p):
    x=p.lower()
    if x=='true':
        r=(True,True)
    elif x=='false':
        r=(True,False)
    else:
        r=(False,p)
    return r



#return dict from string
def parse_str(p,convert=False):
    read_str=False
    str_char=''
    key=''
    value=''
    is_escape=False
    r={}
    if p:
        if isinstance(p,str):
            s=p.strip()
            if s!='':
                count=len(s)
                i=0
                while(i<count):
                    key=''
                    value=''
                    #skip space
                    loop=i<count
                    while(loop):
                        c=s[i:i+1]
                        if c!=' ':
                            loop=False
                        else:
                            i+=1
                            loop=i<count
                    #read key
                    is_escape=False
                    loop=i<count
                    while(loop):
                        c=s[i:i+1]
                        if i>0:
                            is_escape=s[i-1:i]=='\\'
                        if c!=':' or (c==':' and is_escape):
                            key+=c
                            i+=1
                            loop=i<count
                        else:
                            i+=1
                            loop=False
                    #replace key escapes
                    
                    #skip space 
                    loop=i<count
                    while(loop):
                        c=s[i:i+1]
                        if c!=' ':
                            loop=False
                        else:
                            i+=1
                            loop=i<count                      
                    #read value
                    is_escape=False
                    loop=i<count
                    if loop:
                        c=s[i:i+1]
                        read_str=(c=='"' or c=="'")
                        if read_str:
                            str_char=c
                            i+=1
                    loop=i<count
                    while(loop):
                        c=s[i:i+1]
                        if i>0:
                            is_escape=s[i-1:i]=='\\'
                        if not read_str:
                            if c!=' ':
                                value+=c
                                i+=1
                                loop=i<count
                            else:
                                i+=1
                                loop=False
                        else:
                            if c!=str_char:
                                value+=c
                                i+=1
                                loop=i<count
                            else:
                                if is_escape:
                                    value+=c
                                    i+=1
                                    loop=i<count
                                else:
                                    i+=1
                                    loop=False
                    if read_str:
                        if str_char=='"':
                            value="'"+value+"'"
                        else:
                            value='"'+value+'"'
                    if convert:
                        p1=value[:1]
                        p2=value[-1:]
                        print(p1,p2)
                        r_int=str_int(value)                       
                        r_float=str_float(value)
                        r_bool=str_bool(value)
                        if r_int[0]:
                            value=r_int[1]
                        elif r_float[0]:
                            value=r_float[1]
                        elif r_bool[0]:
                            value=r_bool[1]
                        else:
                            value=value[1:-1]
                    r[key]=value
    return r

#print(parse_str('key1:123 key2:123.0 key3:true key4:"text"',convert=True))
