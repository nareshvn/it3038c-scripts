# Generate Random Number
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