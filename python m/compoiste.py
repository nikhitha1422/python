str=input("enter the string:")
c=input("enter the character to find:")
res=none
j=0
while j<len(str):
  for i in range(0,len(str),1):
    if str[i]==c:
       res=true
       print(str[i],"index:",i)
       j=j+1
 if res==None:
    print("Character not found")  
