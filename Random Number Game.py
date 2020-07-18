import random
import math
import time
def nearby(a): 
    y=int(math.ceil(a/ 10.0)) * 10
    print("Number is nearest to : ",y )

def divs(b):       #checks divisiblity
    for i in range (2,7):
        if(b%i==0):
            print("Divisible by",i)
            break
        else:
            continue

print("               Welcome to Our Game ..     ")
time.sleep(1.5)
print("\n")
print("               Guess it if you can !!  ;) ")
time.sleep(1)
print("\n")
st=input("Type yes to start the game ..!! \n")
time.sleep(1)
print("\n")
if(st.lower()=='yes'):
    score=10
    flag=0
    time.sleep(1)
    e=int(input("Please enter the range in which you want to play this game : "))
    x=random.randint(1,e+1) #creates a random iinteger number between 1 and 100 

    print("Initial score is :", score)

    while(score>0): #loop runs till score is greater than 0 
        time.sleep(1) 
        n=int(input("Enter the number less than " ,e ,": "))
        if(n>x):
            print("Oops! try a smaller number")
            score-=2 #negative 2 score for wrong answer
        elif(n<x):
            print("Hmm... Try a bigger number")
            score-=2 #negative 2 score for wrong answer
        elif(n==x):
            print("Exactly !! You are a champ :) ")
            print("Your score is : ",score) # displays score if greater than 0
            break
        if( flag==0 ):
            nearby(x)
            flag=1
            continue

        if (flag==1):
            divs(x)
            flag=2
    
    if(score<=0):
        print("LOOSERR!! Play that again xD ")
else:
    time.sleep(0.5)
    print("Exiting the game NOW ")
    print("thanks !!")

    quit()