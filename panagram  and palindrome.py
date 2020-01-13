#1)PANAGRAM


def myfunc(a):
    
    list1=[]
    f=0
    ch=0
    for i in range(0,len(a)-f):
        #print(i)
        j=i+1
        while(j <(len(a)-f)):
            #print(j)
            if(a[j]==a[i]):
                #print("equal at")
                #print(j)
                #print(i)
                
        
                t=a[j]
                a[j]=a[len(a)-f-1]
                a[len(a)-f-1]=t
                f=f+1
                j=j+1
            
            else:
                j=j+1
    #for item in a:
     #   print(item)
    for item in range(0,len(a)-f):
        if(a[item].islower() ):
            
            print(a[item])
            ch=ch+1
    if(ch==26):
        print("panagram")
        print(ch)        
    else:
        print("not panagram")
            
def myfunc1(st):
    st=st.lower()
    list1=[]
    for i in  range(0,len(st)):
        list1.append(st[i])
    #list1=list1.split()    
    myfunc(list1)
    
#2)PALINDROME

def myfun(st):
    list1=[]
    for item in st:
        
        list1.append(item)
    
    
    f=0
    for item in list1:
        print(item)
    for i in range(0,len(list1)):
        if(list1[i]==list1[len(list1)-i-1]):
            f=f+1
    if(f==len(list1)):
        print("palindrome")
    else:
        print("not palindrome")




#3)project code





























#program to allocate position on the board for each key
def place_marker1(board, marker1, position):
    board[position]=marker1
def place_marker2(board, marker2, position):

    board[position]=marker2
    
 #program to display the board   
from IPython.display import clear_output

def display_board(board):
    
    
    print("   |     |")
    print(" "+  board[1]+" |"+" "+board[2]+ "   |" +" "+board[3])
    print(" --+-----+--")
    print("   |     |")
    
    print(" "+  board[4]+" |"+" "+board[5]+ "   |" +" "+board[6])
    print("   |     |")
    print(" --+-----+--")
    print("   |     |")
   
    print("  "+  board[7]+"|"+" " +board[8]+ "   |" +" "+board[9])
    print("   |     |")

#program to determine which player gets which key
def player_input():
    marker=''
    while(marker!='X'and marker!='O'):
        
        marker=input("player 1 please choose x or o")
    
    player1=marker
    if player1=='X':
        player2= 'O'
    else:
        player2= 'X'
    return(player1,player2)



#program to find if a player has won or not
def win_check(board, marker):
    list1=[]
    for i in range(1,len(board)):
        if(board[i]==marker):
            list1.append(i)
    for item in list1:
        print(item)
    if(1 in list1 and 2 in list1 and 3 in list1):
        return(True)
    elif(1 in list1 and 4 in list1 and 7 in list1):
        return(True)
    elif(2 in list1 and 5 in list1 and 8 in list1):
        return(True)
    elif(3 in list1 and 6 in list1 and 9 in list1):
        return(True)
    elif(4 in list1 and 6 in list1 and 5 in list1):
        return(True)
    elif(7 in list1 and 8 in list1 and 9 in list1):
        return(True)
    elif(1 in list1 and 5 in list1 and 9 in list1):
        return(True)
    elif(3 in list1 and 5 in list1 and 7 in list1):
        return(True)
    else:
        return(False)

#progrm to determine who will start first    
 def myfunc():
        import random
        m=random.choice( ['X', 'O'] )
        print("player to start is with marker {}".format(m))
        return(m)


#program for checking postion is free or not
def player_choice(board):
    
    x=int(input("Enter your position player :"))
    
    def space_check(board, position):
        
        if(board[position]==''):
            
            print('free')
            return(position)
        
        else:
            print("not free")
            player_choice(board)
    space_check(board,x)
    
#progrm to check if board is full
def full_board_check(board):
    
    if("" in board):
        return(False)
    else:
        return(True)    
   #program to check if you want to play again    
def replay():
    
    p=input("do you want to continue :{y/n}")
    if(p=='y'):
        return(True)
    else:
        return(False)
    
    
    
 test_board = ['','','','','','','','','']
    marker1 , marker2=player_input()
    m=myfunc()

    if(m==marker1):
        def myfun():
            if(full_board_check(test_board)):
                print("draw game")
                replay()
            else:  
                pos=player_choice(test_board)
                place_maker1(test_board,marker1,pos)
                dislay_board(test_board)
                if (win_check(test_board,marker1)):
                    print("game over player1 won")
                    replay()
                else:
                    pos=player_choice(test_board)
                    player_maker2(test_board,marker2,pos)
                    display(test_board)
                    if (win_check(test_board,marker2)):
                        print("game over player2 won")
                        replay()
                    else:
                        myfun()
            
    
    else:
        def myfun1():
            if(full_board_check(test_board)):
                print("draw game")
                replay()
            else:  
                pos=player_choice(test_board)
                place_maker2(test_board,marker2,pos)
                dislay_board(test_board)
                if (win_check(test_board,marker2)):
                    print("game over player2 won")
                    replay()
                else:
                    pos=player_choice(test_board)
                    player_maker1(test_board,marker1,pos)
                    display(test_board)
                    if (win_check(test_board,marker1)):
                        print("game over player1 won")
                        replay()
                    else:
                        myfun1()
