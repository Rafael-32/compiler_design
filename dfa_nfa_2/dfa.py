def start(c):
    if c=='a':
        dfa=1
    elif c=='b':
        dfa=2
    else:
        dfa=-1
    return dfa
def state1(c):
    if c=='a':
        dfa=2
    elif c=='b':
        dfa=3
    else:
        dfa=-1
    return dfa
def state2(c):
    if c=='a':
        dfa=3
    elif c=='b':
        dfa=-1
    else:
        dfa=-1
    return dfa
def state3(c):
    dfa=-1
    return dfa
def isaccepted(string):
    l=len(string)
    dfa=0
    for i in range(l):
        if dfa==0:
            dfa=start(string[i])
        elif dfa==1:
            dfa=state1(string[i])
        elif dfa==2:
            dfa=state2(string[i])
        elif dfa==3:
            dfa=state3(string[i])
        else:
            return 0
    if(dfa==3):
        return 1
    else:
        return 0
if __name__=="__main__":
    string=input()
    if(isaccepted(string)):
        print("Accepted")
    else:
        print("Rejected")
    
