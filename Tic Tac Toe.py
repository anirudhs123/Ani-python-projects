











char='y'
def replay():
        char=input("do you want to continue :{y/n}")
        return(char)
        
        
        return(char)
while(replay()!='n'):
    x=0
    test_board = [' ']*9


#program to allocate position on the board for each key
    def place_marker1(board, marker1, position):
        board[position]=marker1
    def place_marker2(board, marker2, position):
        board[position]=marker2
    
 #program to display the board   
    from IPython.display import clear_output

    def display_board(board):
        clear_output()  # Remember, this only works in jupyter!print('   |   |')
        print('   |   |')
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
        print('   |   |')
        print('        ')
        print('        ')
        print('-----------')
        print('   |   |')
        print('   |   |')
        print(' ' + '0' + ' | ' + '1' + ' | ' + '2')
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + '3' + ' | ' + '4' + ' | ' + '5')
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + '6' + ' | ' + '7' + ' | ' + '8')
        print('   |   |')
    
    
    
    

#program to determine which player gets which key
    def player_input():
        marker=''
        while(marker!='X'and marker!='O'):
            marker=input("player 1 please choose x or o")
    
        player1=marker
        if player1=='X':
            player2='O'
        else:
            player2= 'X'
        return(player1,player2)



#program to find if a player has won or not
    def win_check(board, marker):
        list1=[]
        for i in range(0,len(board)):
            if(board[i]==marker):
                list1.append(i)
               # for item in list1:
                  #  print(item)
        if(0 in list1 and 1 in list1 and 2 in list1):
            return(True)
        elif(0 in list1 and 3 in list1 and 6 in list1):
            return(True)
        elif(1 in list1 and 4 in list1 and 7 in list1):
            return(True)
        elif(2 in list1 and 5 in list1 and 8 in list1):
            return(True)
        elif(3 in list1 and 5 in list1 and 4 in list1):
            return(True)
        elif(6 in list1 and 7 in list1 and 8 in list1):
            return(True)
        elif(0 in list1 and 4 in list1 and 8 in list1):
            return(True)
        elif(2 in list1 and 4 in list1 and  6 in list1):
            return(True)
        else:
            return(False)

#progrm to determine who will start first    
    def myfunc():
        import random
        m=random.choice( ['X', 'O'] )
        print("player to start is with marker {}".format(m))
        return(m)

    def space_check(board,x):
        if(board[x]==' '):
            print('free')
            return(x)
        
        else:
            print("not free")
            player_choice(test_board)
        
            
    


#program for checking postion is free or not
    def player_choice(board):
        global x
        x=int(input("Enter your position player :"))
        space_check(test_board,x)
    

    
    
#program to check if board is full
    def full_board_check(board):
        if(" " in board):
            return(False)
        else:
            return(True)    
#program to check if you want to play again    
    def replay():
        char=input("do you want to continue :{y/n}")
        if(char=='n'):
            exit()
        else:
            return(char)
    
    
    
    def myfun1():
        if(full_board_check(test_board)):
            print("draw game")
            replay()
        else:  
            
            pos=player_choice(test_board)
            place_marker2(test_board,marker2,x)
            display_board(test_board)
            if (win_check(test_board,marker2)):
                print("game over player2 won")
                replay()
            else:
                pos=player_choice(test_board)
                place_marker2(test_board,marker1,x)
                display_board(test_board)
                if (win_check(test_board,marker1)):
                    print("game over player1 won")
                    replay()
                
                    
                else:
                    myfun1()
    def myfun():
        if(full_board_check(test_board)):
            print("draw game")
            replay()
        else:  
            
            pos=player_choice(test_board)
            place_marker2(test_board,marker1,x)
            display_board(test_board)
            if (win_check(test_board,marker1)):
                print("game over player1 won")
                replay()
            else:
                pos=player_choice(test_board)
                place_marker2(test_board,marker2,x)
                display_board(test_board)
                if (win_check(test_board,marker2)):
                    print("game over player2 won")
                    replay()
                
                    
                else:
                    myfun()
           
        
    
    
    test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    marker1,marker2=player_input()
    print("player 1  {}".format(marker1))
    print("player 2  {}".format(marker2))
    m=myfunc()

    if(m==marker1):
        myfun()
    else:
        myfun1()
       
        
    
       
        
    
    
