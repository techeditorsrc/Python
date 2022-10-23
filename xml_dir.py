#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: Create xml tree from folder functions
# License: GPL v3

import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
import base64

def str_to_base64(s):
    return base64.b64encode(s.encode('ascii')).decode('ascii')

def base64_to_str(s):
    return base64.b64decode(s).decode('ascii')

def write_file(path,file,data):
    if(path==""):
        path=os.path.dirname(__file__)
    path=os.path.join(path,file)
    f = open(path, "w")
    f.write(data)
    f.close()

def read_file(f):
    r=''
    f=open(f,'rb')
    r=f.read()
    f.close()
    return ascii(r)

def make_tree(path,r={'type':'directory','list':[]},tab=0,tab_space='\t',path2=''):
    for item in os.listdir(path):
        item_name=os.path.split(item)[1]
        item_ = os.path.join(path, item)
        if os.path.isfile(item_):
            data=''
            # data=str_to_base64(read_file(item_))
            x={'type':'file','path':os.path.join(path2,item_name),'name':item_name,'list':[],'data':data}            
            r['list'].append(x)
            # print(f'{tab_space*tab}{item_name}')
        elif os.path.isdir(item_):
            x={'type':'directory','path':os.path.join(path2,item_name),'name':item_name,'list':[]}
            r['list'].append(x)
            # print(f'{tab_space*tab}{"["}{item}{"]"}')
            make_tree(item_,x,tab=tab+1,tab_space=tab_space,path2=item)
        else:
            print(item_)
    return r

def get_xml(tree,tab=0,tab_space='\t',is_first=True):
    r=''
    if(is_first):
        r+='<?xml version="1.0"?>\n'
        r+='<root>\n'
        tab+=1
    for item in tree['list']:
        if(item['type']=='file'):
            r+=tab_space*tab+'<file name="'+item['name']+'" path="'+item['path']+'" data="'+item['data']+'" />\n'
            pass
        elif(item['type']=='directory'):
            r+=tab_space*tab+'<directory name="'+item['name']+'" path="'+item['path']+'">\n'
            r+=get_xml(item,tab+1,tab_space,False)            
            r+=tab_space*tab+'</directory>\n'
            pass
    if(is_first):
        r+='</root>'
    return r

tree=make_tree('/home/linux/Documents')
x=get_xml(tree)
print(x)
