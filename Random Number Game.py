import random
from time import sleep
from os import system, name 
  

def clear(): #clear screen function 
    if name == 'nt': 
        _ = system('cls') 

def nearby(a): 
    print("*****        HINT 1        *****")
    y=int(round(a/5.0)*5.0)
    print("Number in nearest to 5 : ",y )

def divs(b):  
    print("*****        HINT 2        *****")     #checks divisiblity
    print("\nNumber is divisible by : \n")
    for i in range (2,6):
        if(b%i==0):
            print(i,"\n")
        else:
            continue
 


print("               Welcome to Our Game ..     ")
sleep(1.5)
print("\n")
print("               Guess it if you can !!  ;) ")
sleep(1)
print("\n")
st=input("Type yes to start the game ..!! \n")
sleep(1)
print("\n")
try :
    if(st.lower()=='yes' or st.lower()=='y'):
        score=10
        flag=-1
        sleep(1)
        print("Please enter the inputs below ")
        e1=int(input("\nThe range must Start from :  "))
        e2=int(input("\nThe range must End to :  "))
    
        x=random.randint(e1,e2) #creates a random iinteger number between input range

        print("\nInitial score is :", score)
        sleep(1)

        while(score>0): #loop runs till score is greater than 0 
            sleep(1)
            clear()
            print("\nEnter the number greater than",e1-1,"and less than",e2+1,":")
            n=int(input())
            if(n>e2 or n<e1):
                print("You are voilating rules** \n Reducing 5 points as penalty !! \n")
                score-=5
                if score < 0:
                    raise Exception("OOPS !! try it again")
            elif(n>x):
                print("\nOops! try a smaller number\n")
                score-=2 #negative 2 score for wrong answer
            elif(n<x):
                print("\nHmm... Try a bigger number\n")
                score-=2 #negative 2 score for wrong answer
            elif(n==x):
                print("\nExactly !! You are a champ :) \n")
                print("\nYour score is : ",score,"\n") # displays score if greater than 0
                break
            
            s=input("\nDo you want to use a hint by reducing 1 point ? (y/n)")
            if(s.lower()=='y'):
                flag+=1
            else:
                pass

            if( flag==0):
                nearby(x)
                sleep(2)
               # flag=1
                score-=1
                print("Updated score : ",score)
                sleep(1)
                continue

            if (flag==1):
                divs(x)
                print("\n")
                sleep(2)
                score-=1
                print("Updated score : ",score)
                sleep(1)
                

            if(flag>=2):
                print("\nNo more hints available !!")
    
        if(score<=0):
            print("\nLOOSERR!! Play that again xD ")
    else:
        sleep(0.5)
        quit()
        clear()
except ValueError:
    print("\nNot an integer! Please try again ... \n")
    quit()
except:
    print("Exiting the game NOW \n")
    print("thanks !! \n")
    quit()
