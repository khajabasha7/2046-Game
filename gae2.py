import random

def add_new():
    a=random.randint(0,n-1)
    b=random.randint(0,n-1)
    while(mat[a][b]!=0):
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
    mat[a][b]=2

def start_game():
    print("Commands are as follows : ")
    print("'U' or 'u' : Move Up")
    print("'D' or 'd' : Move Down")
    print("'L' or 'l' : Move Left")
    print("'R' or 'r' : Move Right")
    for i in range(n):
        mat.append([0]*n)
    for i in range(2):
        add_new()

def compress():
    for i in range(n):
        for j in range(n):
            if 0 in mat[i]:
                mat[i].remove(0)
    for i in range(n):
        if len(mat[i])<n:
            mat[i]+=([0]*(n-len(mat[i])))

def merge():
    for i in range(n):
        for j in range(n-1):
            if mat[i][j]==mat[i][j+1]:
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
def reverse():
    for i in range(n):
        mat[i].reverse()

def transpose():
    for i in range(n):
        for j in range(i+1):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    
    
def move_left():
    compress()
    merge()
    compress()

def move_right():
    reverse()
    move_left()
    reverse()
    
def move_up():
    transpose()
    move_left()
    transpose()

def move_down():
    transpose()
    move_right()
    transpose()
    
def check_status():
    if 2048 in mat:
        return 1
    
    if 0 in mat:
        return 0
    
    for i in range(n):
        for j in range(n-1):
            if  mat[i][j]==mat[i][j+1]: #to check adjuscent
                return 0
        for k in range(n-1):
            if  mat[k][i]==mat[k+1][i]:#to check top and bottom
                return 0
    return 2

def print_mat():
    for i in range(n):
        for j in range(n):
            print(mat[i][j]," ",end="")
        print()



#######################################################################
print("welcome to 2048 game")
s=input("press any key to start the game: ")
n=int(input("choose the number of grids you want to play on: "))
mat=[]
start_game()
print_mat()
while(True):
    print("choose the movement to be performed:")
    move=input()
    if move=="U" or move=="u":
        move_up()
        status=check_status()
        if status==0:
            add_new()
            print_mat()
        if status==1:
            print_mat()
            print("You have won the game")
            break
        elif status ==2:
            print_mat()
            print("You lost the game")
            break
        
        
    if move=="D" or move=="d":
        move_down()
        status=check_status()
        if status==0:
            add_new()
            print_mat()
        elif status==1:
            print_mat()
            print("You have won the game")
            break
        elif status ==2:
            print_mat()
            print("You lost the game")
            break
        
        
    if move=="L" or move=="l":
        move_left()
        status=check_status()
        if status==0:
            add_new()
            print_mat()
        elif status==1:
            print_mat()
            print("You have won the game")
            break
        elif status ==2:
            print_mat()
            print("You lost the game")
            break
        
        
    if move=="R" or move=="r":
        move_right()
        status=check_status()
        if status==0:
            add_new()
            print_mat()
        elif status==1:
            print_mat()
            print("You have won the game")
            break
        elif status ==2:
            print_mat()
            print("You lost the game")
            break