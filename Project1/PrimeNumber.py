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

print("Guess a number game....");
from random import seed
from random import randint
seed(1)
num=int(input("Guess my number between 0 and 100: "));
mynum=randint(0,100);
print ("My number : ",mynum);
if (num < 0 or num >100):
print(" you didnt follow my instructions ");
else:
if (num==mynum):
print("Guessed correctly ",num);
else:
if (mynum < num):
print("My random number ",mynum," is lesser than",num);
else:
print("My random number ",mynum, " is greater than",num);