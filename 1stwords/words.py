file=open(r"C:\Users\91939\Downloads\backdrop.txt",'r')
data=file.read()
number_of_characters=len(data)
print("total no.of.characters:",number_of_characters)
file=open(r"C:\Users\91939\Downloads\backdrop.txt",'r')
data=file.read().replace(" ","")
n1=len(data)
print("no.of characters without white spaces",n1)
f=open(r"C:\Users\91939\Downloads\backdrop.txt",'r')
c1=0
for line in f:
    c1+=1
print("total no.of lines is",c1)
f1=open(r"C:\Users\91939\Downloads\backdrop.txt",'r')
c2=0
for line in f1:
    x=line.split()
    c2+=len(x)
print("no.of words:",c2)
