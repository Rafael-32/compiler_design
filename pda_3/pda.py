def f0(c):
    if c=='a':
        l.append(c)
        return 0
    elif c=='b':
        if len(l)==0:
            return -1
        else:
            l.pop()
            return 1
    else:
        return -1
def f1(c):
    if c=='a':
        return -1
    elif c=='b':
        if len(l)==1:
            l.pop()
            return 2
        else:
            l.pop()
            return 1
    else:
        return -1
def isaccepted(s):
    pda=0
    for i in s:
        if pda==0:
            pda=f0(i)
        elif pda==1:
            pda=f1(i)
        elif pda==2:
            print("Accepted")
        else:
            print("Rejected")
if __name__=="__main__":
    s=input()
    l=[]
    isaccepted(s)
    
