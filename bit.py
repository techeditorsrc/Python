#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: Bitwise functions (beta)
# License: GPL v3

def setbit(x,index):
  return x | (1<<(index-1))

def clearbit(x,index):
  return x & (0xffffffff & (1<<(index-1)))  

def inttobin(x):
  r=''
  for j in range(32):
    r=str((x>>j)& 1)+r
  return r

def bintoint(x):
  r=0
  c=len(x)
  for j in range(c):
    r=r | int(x[j])<<(c-j-1)
  return r

def shl(x,count):
  return x<<count

def shr(x,count):
  return x>>count

def xor(x,y):
  return ~ (x | y)

def and_list(x):
  r=x[0]
  for j in x:
    r=r & j
  return r

def or_list(x):
  r=x[0]
  for j in x:
    r=r | j
  return r

def nand_list(x):
  r=x[0]
  for j in x:
    r=r & j
  r= ~ r
  return r

def nor_list(x):
  r=x[0]
  for j in x:
    r=r | j
  r= ~ r
  return r

def add_s(x,y):
  r=x+y
  if(r)>0xff:
    return 0xff
  else:
    return r

def create_4bit_mask_list(x):
  r=[((0xf0*int((i & 0xf0)>0)) | (0xf*int((i & 0xf)>0))) for i in x]

#shl list of 32 bit int to {x} bytes
def shl_list(x,count):
  c=len(x)
  if(count==0 or c==0):
    return
  cx=int(count/4)
  if(cx>=c):
    for i in range(c):
      x[i]=0
      return
  cm=count % 4
  if(cm==0):
    if(cx==0):
      return
    else:
      for i in range(c-cx):
        x[i]=x[i+cx]
      for i in range(c-cx,c):
        x[i]=0
  else:
    cm=cm << 3
    x[0]=x[cx]<<cm
    for i in range(1,c-cx):
      x[i-1]=x[cx+i-1] | (x[cx+i] >> (32-cm))
      x[i]=x[cx+i] << cm
    if(cx>0):
      for i in range(c-cx,c):
        x[i]=0

#shr list of 32 bit int to {x} bytes
def shr_list(x,count):
  c=len(x)
  if(count==0 or c==0):
    return
  cx=int(count/4)
  if(cx>=c):
    for i in range(c):
      x[i]=0
      return
  cm=count % 4
  if(cm==0):
    if(cx==0):
      return
    else:
      for i in reversed(range(c-cx)):
        x[i+cx]=x[i]
      for i in range(cx):
        x[i]=0
  else:
    cm=cm << 3
    x[c-1]=x[c-cx-1]<<cm
    for i in range(1,c-cx):
      x[c-1-i-1]=x[c-1-cx+i-1] | (x[c-1-cx+i] >> (32-cm))
      x[c-1-i]=x[c-1-cx+i] << cm
    if(cx>0):
      for i in range(cx):
        x[i]=0
