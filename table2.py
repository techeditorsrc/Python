#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: print table
# License: GPL v3

import os

def get_str(s,width,align):
  r=''
  if(width==0):
    return ''
  l=len(s)
  j=(width-l)
  if(align=='left'):
    x1=''
    x2=' '*j
  elif(align=='center'):
    x_1=int(j/2)
    x1=' '*x_1
    x2=' '*(j-x_1)
  elif(align=='right'):
    x1=' '*j
    x2=''
  if(l<width):
    r=x1+s+x2
  elif(l==width):
    r=s
  elif(l>width):
    # l2=l-width
    # x3=int(l2/2)
    # x4=l-(l2-x3)
    # print(x3,x4)
    x3=0
    x4=l-(l-width)
    r=s[x3:x4]
  return r

def print_row(items,ch='',line=''):
  l=len(items)
  s=''
  x=0
  if(line==''):
    for item,width,align in items:
      s=s+get_str(item,width,align)
      if(x<l-1):
        s=s+ch
      x=x+1
  else:
    for item,width,align in items:
      s=s+get_str(line*width,width,align)
      if(x<l-1):
        s=s+ch
      x=x+1
  print(s)

os.system('clear')

print_row([
  ('Rows',7,'center'),
  ('X',10,'center'),
  ('Y',10,'center')
],'|'
)
print_row([
  ('',7,'left'),
  ('',10,'right'),
  ('',10,'right')
],'+','-'
)

print_row([
  ('Row1',7,'left'),
  ('value1',10,'right'),
  ('value2',10,'right')
],'|'
)
print_row([
  ('Row2',7,'right'),
  ('value1',10,'right'),
  ('value2',10,'right')
],'|'
)
print_row([
  ('Row3',7,'right'),
  ('value1',10,'right'),
  ('value2',10,'right')
],'|'
)
print_row([
  ('',7,'left'),
  ('',10,'right'),
  ('',10,'right')
],'+','-'
)
