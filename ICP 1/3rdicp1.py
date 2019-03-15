string=input("Enter string:")
count1=0
count2=0
count3=1
for n in string:
      if(n.isdigit()):
            count1=count1+1
      if(n.isalpha()):
            count2=count2+1
      if(n==' '):
            count3=count3+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)
print("The number of words is")
print(count3)