#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: deep copy function
# License: GPL v3

class table():
  def newcolumn(self,name=""):
    return {"name":name,"items":[]}
    
  def __init__(self,name="",columns=[]):
    self.name=name
    self.columns=[]
    for i in columns:      
      self.columns.append(self.newcolumn(name=i))
    
  def get_column_by_index(self,index):
    if index<len(self.columns):
      return self.columns[index]
    else:
      return None
  
  def get_column_by_name(self,name):
    r=None
    for i in self.columns:
      if i["name"]==name:
        r=i
        break
    return r
      
  def add_item(self,column_index,item):
    if column_index>=0 and column_index<len(self.columns):
      self.columns[column_index]["items"].append(item)
      
  def add_empty_row(self):
    for i in self.columns:
      i["items"].append("")

  def column_count(self):
    return len(self.columns)
    
  def row_count(self):
    if len(self.columns)>0:
      return len(self.columns[0]["items"])
    else:
      return 0

  def add_row(self,*items,begin_column=0):
    self.add_empty_row()
    x=begin_column
    l=len(self.columns)
    cl=self.row_count()-1
    for i in items:
      if x<l:
        self.columns[x]["items"][cl]=i
        x+=1
      else:
        break

  def add_row_by_column_names(self,**items):
    self.add_empty_row()
    for key,value in items.items():
      x=self.get_column_by_name(key)
      j=self.row_count()-1
      if x:
        x["items"][j]=value
        
  def fill_row(self,*items,row_index=0,begin_column=0):
    r=self.row_count()
    if row_index>=0 and row_index<r:
      x=begin_column
      l=len(self.columns)
      for i in items:
        if x<l:
          self.columns[x]["items"][row_index]=i
          x+=1
        else:
          break
      
  def fill_row_by_column_names(self,row_index=0,**items):
    r=self.row_count()
    if row_index>=0 and row_index<r:
      for key,value in items.items():
        x=self.get_column_by_name(key)
        if x:
          x["items"][row_index]=value

  def insert_row(self,*items,row_index=0,begin_column=0):
    l=len(self.columns)
    if l>0:
      if row_index<0:
        row_index=0
      cl=self.row_count()
      if row_index>cl:
        row_index=cl
      self.add_empty_row()
      if row_index<cl:
        for j in self.columns:
          for i in reversed(range(row_index,cl)):
            print(i)
            j["items"][i+1]=j["items"][i]
          j["items"][row_index]=""
        
      x=begin_column
      for i in items:
        if x<l:
          self.columns[x]["items"][row_index]=i
          x+=1
        else:
          break
          
  def insert_row_by_column_names(self,row_index=0,begin_column=0,**items):
    l=len(self.columns)
    if l>0:
      if row_index<0:
        row_index=0
      cl=self.row_count()
      if row_index>cl:
        row_index=cl
      self.add_empty_row()
      if row_index<cl:
        for j in self.columns:
          for i in reversed(range(row_index,cl)):
            print(i)
            j["items"][i+1]=j["items"][i]
          j["items"][row_index]=""
      for key,value in items.items():
        x=self.get_column_by_name(key)
        if x:
          x["items"][row_index]=value
      
  def copy(self,name,begin_row,end_row):
    r3=table(name)
    rc=self.row_count()
    if begin_row<0:
      r1=0
    elif begin_row>=rc:
      r1=rc-1
    else:
      r1=begin_row
    if end_row<0:
      r2=0
    elif end_row>=rc:
      r2=rc-1
    else:
      r2=end_row
    if r1>=r2:
      r=range(r1,r2+1)
    else:
      r1,r2=r2,r1
      r=reversed(range(r1,r2+1))
    rcx=0
    for j in self.columns:
      r3.columns.append(self.newcolumn(j["name"]))
      if rc>0:
        if r1>=r2:
          r=range(r1,r2+1)
        else:
          r1,r2=r2,r1
          r=reversed(range(r1,r2+1))
        for i in r:
           r3.columns[rcx]["items"].append(j["items"][i])
      rcx+=1
    return r3
          
  def delete_row(self,index):
    if index>=0:
      for j in self.columns:
        if index<len(j["items"]):
          del j["items"][index]  
  
  def clear(self):
    for i in self.columns:
      i["items"]=[]

x=table(name="Table1",columns=["Column1","Column2","Column3","Column4","Column5"])
x.add_row("A","B","C",begin_column=1)
x.insert_row(1,2,3,row_index=0)
y=x.copy("",0,0)
z=y
print(len(z.columns))
for i in z.columns:
  print(i["name"],i["items"])
