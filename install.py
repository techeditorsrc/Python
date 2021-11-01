#  Author: Anton Nedilko
#   Email: arcs3567@gmail.com
#  Source: https://github.com/techeditorsrc
#    Info: Install packages tool
# License: GPL v3

import subprocess
import sys

msg1="\n\nPython installer 1.0\n"
msg2="Type package names with space, 'quit' for exit\n\n"

def message():
    print(msg1)
    print(msg2)

def install(package):
    try:
        print("Install ["+package+"]\n")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package,"--user"])
        print("\n")
    except:
        print("Error installing ["+package+"]\n")

l=len(sys.argv)
if l>1:
    message()
    for j in range(1,l):
        install(sys.argv[j])
        
while True:
    message()
    s=input(">")
    if s.lower()!="quit":
        p=s.split(" ")
        p1=[i for i in p if i.strip()!=""]
        for x in p1:
            install(x)
    else:
        break


