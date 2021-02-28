from introduction import intro

import os

intro()

print("Enter 1st player name :- ")
p1=input()
print("Enter 2nd player name :- ")
p2=input()
cross="X"
circle="O"

a=[""," "," "," "," "," "," "," "," "," "]

def print_table(n):
    os.system("cls")
    print("\t WELCOME TO ... TIC TAC TOE ...\n")
    print("      |      |      ")
    print("  ",a[1]," | ",a[2],"  | ",a[3],"  ")
    print("______|______|______")
    print("      |      |      ")
    print("  ",a[4]," | ",a[5],"  | ",a[6],"  ")
    print("______|______|______")
    print("      |      |      ")
    print("  ",a[7]," | ",a[8],"  | ",a[9],"  ")
    print("      |      |      ")
    
def win_pos():
    if(a[5]!=" "):
        if(a[5]==a[1] and a[5]==a[9] or a[5]==a[3] and a[5]==a[7]):
            if a[5]=="X":
                return(1)
            else:
                return(0)
        if(a[5]==a[2] and a[2]==a[8] or a[5]==a[4] and a[4]==a[6]):
            if a[5]=="X":
                return(1)
            else:
                return(0)
    if(a[1]!=" "):
        if(a[1]==a[4] and a[4]==a[7] or a[1]==a[2] and a[2]==a[3]):
            if a[1]=="X":
                return(1)
            else:
                return(0)
    if(a[9]!=" "):
        if(a[9]==a[6] and a[3]==a[9] or (a[9]==a[8] and a[8]==a[7]) ):
            if a[9]=="X":
                return(1)
            else:
                return(0)
            
for i in range(1,12):
    if(i%2==0):
        print(p2," turn ")
        n=int(input())
        if(a[n]!=" "):
            print("You have entered wrong number")
            break
        a[n]=circle
        print_table(n)
        w=win_pos()
        if w==1:
            print(p1," wins")
            break
        elif (w==0):
            print(p2," player wins")
            break
    else:
        print(p1," turn ")
        n=int(input())
        if(a[n]!=" "):
            print("You have entered wrong number")
            break
        a[n]=cross
        print_table(n)
        w=win_pos()
        if w==1:
            print("\n  CONGRATULATIONS! Player",p1," wins")
            break
        elif w==0:
            print("\n  CONGRATULATIONS! ",p2, "player wins")
            break
    if(i==10):
        print("  OOO  Match Draw  OOO")
        break 
input()
