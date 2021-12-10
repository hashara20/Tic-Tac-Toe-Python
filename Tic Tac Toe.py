
import random #import this to genarate random numbers

#difine a list for the board
board= ["1", "2", "3","4", "5", "6", "7", "8","9"]

#a function to draw the board
def draw_board():
    print("-------------------------")
    print("|  ", board[0],"  |  ",board[1], "  |  " ,board[2], "  |")
    print("-------------------------")
    print("|  ",board[3],"  |  ",board[4], "  |  ", board[5], "  |")
    print("-------------------------")
    print("|  ",board[6], "  |  ",board[7] ,"  |  " ,board[8] ,"  |")
    print("-------------------------")
    print(" ")


#taking the playes name as input
player = input("Enter your name: ")

#check whether the input is correct
for j in range(1,100):
    marker1 = input("Enter your marker(X or O) :  ")
    marker1 = marker1.upper()
    if marker1 == "X":
        marker2 = "O"
        break
    elif marker1 == "O":
        marker2 = "X"
        break
    else:
        print("Invalid input, Please enter again: ")
        j=j-1

print("Your marker is", marker1)
print("Coputers marker is ",marker2)



# a function to check whether the entered slot number is already taken one
def is_swap(c):

    if(board[c-1]=="X" or board[c-1]=="O"):
        return 1
    else:
        return 0


# a function to check whether the plauyer or computer is win
def is_win(m):
    if(m==marker1):
        if(board[0]==board[1]==board[2] or board[3]==board[4]==board[5]
                or board[6]==board[7]==board[8] or board[0]==board[3]==board[6] or
                board[1]==board[4]==board[7 or board[2]==board[5]==board[8]]
        or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]):


            print(player, " is Win, Congradulations: ")
            exit()


    elif(m==marker2):
        if (board[0] == board[1] == board[2] or board[3] == board[4] == board[5]
                or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or
                board[1] == board[4] == board[7 or board[2] == board[5] == board[8]]
                or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
            print("Computer is Win : ")
            exit()



#the function to play the game
def game_paly( ):

    print(" ")
    print(" Let's Play the TicTacToe")
    print(" ")

    for i in range(1,9):

        if i==1:
            draw_board()


        print("------Your turn------")
        a=int(input("Enter the slot number(1 to 9)  or Enter 0(zero) to exist:"))
        x=is_swap(a)

        if a>=1 and a<=9 and x!=1:
            board[a-1]=marker1
            draw_board()
            is_win(marker1)
        elif(x==1):
            print("That number is already taken, try another one:")
            i=i-1
            continue
        elif a==0:
            exit()
        else:
            print("Invalid Input, please enter again correct slot number:")
            i=i-1
            continue


        print("_______Computers turn_____")
        n = random.randint(1, 9) #genarating random numbers from 1 to 9
        print("Computer enters: ",n)
        y=is_swap(n)
        if(y!=1):
            board[n - 1] = marker2
            draw_board()
            is_win(marker2)
        else:
            print("That number is already taken, try another one: ")




#call game_play function
game_paly()












