#generates prime numbers
print("Printing Prime Numbers...")
num=int(input("Enter any number : "))
Flag=False
nonPrime="";

if (num==0 or num > 0):
print(0);
if (num==1 or num > 1):
print(1);
for i in range(2, num+1):
for j in range(2, i):
if (i % j) == 0:
# print("i = ",i, " j = ", j, ";",i,"%",j," is ", i%j );
Flag=True
break
else:
Flag=False
if (Flag == False):
print(i)
