#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: Project manager (beta)
# License: GPL v3

class task():
  def __init__(self,name,ready=False,info=''):
    self.name=name
    self.info=[].append(info)
    self.type='task'
    self.ready=ready
    self.date_start=None
    self.date_finish=None

  def setdate(self,ds,df):
    if(ds):
      self.date_start=ds
    if(df):
      self.date_finish=df

  def done(self):
    self.ready=True

  def reset(self):
    self.ready=False

class project():

  def save(self):
    self.save_ptr=self.tasks

  def restore(self):
    self.tasks=self.save_ptr

  def __init__(self,name,tasks=[]):
    self.projects=[]
    self.tasks=[]
    self.save_ptr=self.tasks
    self.type='project'
    self.name=name
    self.date_start=None
    self.date_finish=None


  def setdate(self,ds,df):
    if(ds):
      self.date_start=ds
    if(df):
      self.date_finish=df

  def find_project_(self,ps):
    r=-1
    c=len(self.projects)
    if(c>0):
      for x in range(c):
        if(self.projects[x].name==ps):
          r=x
          break
    return r

  def find_project(self,ps):
    result={
      'path_src':ps,
      'path':[],
      'project':None
    }
    r=[]
    r_found=True
    obj=self
    s=ps.split('/')
    for x in s:
      j=None
      x1=self.find_project_(x)
      if(x1!=-1):
        r.append(self.projects[x1])
        obj=self.projects[x1]
      else:
        r=[]
        r_found=False
        break
    if(r_found):
      result['path']=r
      c=len(r)
      if(c>0):
        result['project']=r[c-1]
    return r
            
  def find_task_(self,ts):
    r=-1
    c=len(self.tasks)
    if(c>0):
      for x in range(c):
        if(self.tasks[x].name==ts):
          r=x
          break
    return r

  def find_task(self,ts):
    result={
      'path_src':ts,
      'path':[],
      'project':None,
      'task':None
    }
    r=[]
    r_found=True
    s=ts.split('/')
    c=len(s)
    # print(s,c)
    if(c==1):
      x1=self.find_task_(s[0])
      if(x1!=-1):
        r.append(self.tasks[x1])
    elif(c>1):
      obj=self
      for x in range(0,c-1):
        x1=obj.find_project_(s[x])
        if(x1!=-1):
          r.append(obj.projects[x1])
          obj=obj.projects[x1]
        else:
          r=[]
          r_found=False
          break
      if(r_found):
        result['path']=r
        c1=len(r)
        if(c1==c-1)and(c>0):
          result['project']=r[c1-1]
        x1=obj.find_task_(s[c-1])  
        if(x1!=-1):
          # r.append(obj.tasks[x1])
          result['task']=obj.tasks[x1]
    return result
  
  def add_project(self,project_name,tasks=[]):
    self.projects.append(project(project_name))
    obj=self.projects[len(self.projects)-1]
    for x in tasks:
      obj.tasks.append(x)
    return self
  
  def del_project(self,project_name):
    x1=self.find_project_(project_name)
    if(x1!=-1):
      del self.projects[x1]

  def add_task(self,task_name):
    self.tasks.append(task(task_name))

  def del_task(self,task_name):
    x1=self.find_task_(task_name)
    if(x1!=1):
      del self.tasks[x1]

  def get_ready(self):
    r={}
    c=len(self.tasks)
    r['tasks']=c
    r['ready']=0
    r['percent']=0
    if(c>0):
      for x in range(c):
        if(self.tasks[x].ready):
          r['ready']+=1
    if(r['ready']>0):
      r['percent']=r['ready']*100/r['tasks']
    return r

  def get_ready_all_(self,xr):
      r={
        'tasks':xr['tasks'],
        'ready':xr['ready'],
        'percent':0
        }
      for x in self.projects:
        x1=x.get_ready_all_(r)
        r['tasks']+=x1['tasks']
        r['ready']+=x1['ready']
      for x2 in self.tasks:
        r['tasks']+=1
        if(x2.ready):
          r['ready']+=1
      return r      
      

  def get_ready_all(self):
    r={
      'tasks':0,
      'ready':0,
      'percent':0
      }
    r=self.get_ready_all_(r)
    if(r['ready']>0):
      r['percent']=r['ready']*100/r['tasks']
    return r
  
  def done(self,*tasks):
    for x in tasks:
      x1=self.find_task_(x)
      if(x1!=-1):
        self.tasks[x1].done()

prg=project('test',[task('task1'),task('task2')])
prg.add_project('test2',[task('test2_task'),task('test2_task2')])
t=prg.find_task('test2/test2_task')
print(t['project'].name)
# print(prg.find_project_('test2'))


    
