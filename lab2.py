t=input("Enter txt:")
i=len(t)
while(i>0):
    i = i-1                 #2
    print(t[i], end="")



w = input("word=")
for x in w:
    print(x+x,end="")   
    
n = input("введіть щось")[::-1]
print(n)