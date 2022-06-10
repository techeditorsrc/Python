#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: function for bs4
# License: GPL v3

class tags():
    def __init__(self,p):
        self.p=p

    def parse_path(self,p):
        s=p.split('/')
        r=[]
        for i in s:
            s1=i.strip()
            if s1!='':
                s1=s1.split(':')
                r.append({'tag':s1[0],'index':int(s1[1])})
        return r

    def find_all(self,tag,next_tag_index,param={}):
        r=self.p
        if r!=None:
            r=r.find_all(tag,param)
            if next_tag_index!=-1:
                if next_tag_index>=0 and next_tag_index<len(r):
                    r=r[next_tag_index]
        return tags(r)

    def goto(self,path):
        path_=self.parse_path(path)
        p=self.p
        if p!=None:
            for i in path_:
                x=p.find_all(i['tag'])
                index=i['index']
                if index>=0 and index<len(x):
                    p=x[index]
                else:
                    p=None
                    break
        return tags(p)

def item(p,index):
    if p!=None:
        if isinstance(p,list) or isinstance(p,tuple):
            if index>=0 and index<len(p):
                return p[index]
            else:
                return None
        elif isinstance(p,dict):
            if index in p:
                return p[index]
            else:
                return None
        else:
            return None
    else:
        return None
   
# print(parse_path('div:10/table:0/tr:0/td:0'))
