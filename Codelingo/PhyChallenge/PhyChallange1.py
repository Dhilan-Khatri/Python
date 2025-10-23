board={"7":" ", "8":" ", "9":" ",
    "4":" ", "5":" ", "6":" ",
    "1":" ", "2":" ", "3":" ",}
boardkeys=[]
for key in board:
    boardkeys.append(key)

def printboard(board):
    print(board["7"]+"|"+board["8"]+"|"+board["9"])
    print("-----")
    print(board["4"]+"|"+board["5"]+"|"+board["6"])
    print("-----")
    print(board["1"]+"|"+board["2"]+"|"+board["3"])
def game():
    turn="X"
    count=0
    for i in range(10):
        printboard(board)
        print(f"It is Your Turn {turn}, What spot do you want to move?")
        move=input()
        if board[move]==" ":
            board[move]=turn
            count+=1
        else:
            print("This spot is already taken. Please choose a different spot.")
            continue
        if count>=5:
            if board["7"]==board["8"]==board["9"]!=" ":
                printboard(board)
                print("\nGame Over")
                print("\n **** "+turn+" won"+" ****")
                break
            elif board["4"]==board["5"]==board["6"]!=" ":
                printboard(board)
                print("\nGame Over")
                print("\n **** "+turn+" won"+" ****")
                break
            elif board["1"]==board["2"]==board["3"]!=" ":
                printboard(board)
                print("\nGame Over")
                print("\n **** "+turn+" won"+" ****")
                break
            elif board["7"]==board["5"]==board["3"]!=" ":
                printboard(board)
                print("\nGame Over")
                print("\n **** "+turn+" won"+" ****")
            elif board["9"]==board["5"]==board["1"]!=" ":
                printboard(board)
                print("\nGame Over")
                print("\n **** "+turn+" won"+" ****")
                break
            elif board["7"]==board["4"]==board["1"]!=" ":
                printboard(board)
                print("\nGame Over")
                print("\n **** "+turn+" won"+" ****")
                break
            elif board["8"]==board["5"]==board["2"]!=" ":
                printboard(board)
                print("\nGame Over")
                print("\n **** "+turn+" won"+" ****")
                break
            elif board["9"]==board["6"]==board["3"]!=" ":
                printboard(board)
                print("\nGame Over")
                print("\n **** "+turn+" won"+" ****")
                break
        if count == 9:
            print("\n Game Over")
            print("\n Tie")
        if turn=="X":
            turn="O"
        else:
            turn="X"
    restart=input("Do you want to play again(y/n)?")
    if restart=="y" or restart=="Y":
        for key in boardkeys:
            board[key]=" "
        game()
#if __name__=="__main__":
game()