r=int(input("Enter the number of rows"))
c=int(input("Enter number of cols"))
for i in range(r):
   for j in range(c):
     if i>j:
       print("$",end="")
     elif i==j:
       print("#",end="")
     elif i<j:
       print("@",end="")
   print()
