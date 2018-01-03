Id="p1"
def Prompt(board):
    global Id
    va1 = input("Enter row (0-2) : ")
    va2 = input("Enter colomn (0-2) : ")
    if va1>=0 and va1<=2 and va2>=0 and va2<=2:
        if board[va1][va2]!=-1:
            print "Already marked , prompt again  :"
            Prompt(board)
        else:
            if Id=="p1":
                board[va1][va2]=1
                Id="p2"
            else:
                board[va1][va2] = 0
                Id="p1"
    else:
        print "Invalid, prompt again :"
        Prompt(board)
    return;

def Decision(board):
    VALUE="false"
    if board[0][0]==1 and board[0][1]==1 and board[0][2]==1: VALUE="p1"
    elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1: VALUE="p1"
    elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1: VALUE="p1"
    elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1: VALUE="p1"
    elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1: VALUE="p1"
    elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1: VALUE="p1"
    elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1: VALUE="p1"
    elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1: VALUE="p1"
    elif board[0][0]==0 and board[0][1]==0 and board[0][2]==0: VALUE="p2"
    elif board[1][0] == 0 and board[1][1] == 0 and board[1][2] == 0: VALUE="p2"
    elif board[2][0] == 0 and board[2][1] == 0 and board[2][2] == 0: VALUE="p2"
    elif board[0][0] == 0 and board[1][0] == 0 and board[2][0] == 0: VALUE="p2"
    elif board[0][1] == 0 and board[1][1] == 0 and board[2][1] == 0: VALUE="p2"
    elif board[0][2] == 0 and board[1][2] == 0 and board[2][2] == 0: VALUE="p2"
    elif board[0][0] == 0 and board[1][1] == 0 and board[2][2] == 0: VALUE="p2"
    elif board[0][2] == 0 and board[1][1] == 0 and board[2][0] == 0: VALUE="p2"
    d=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==-1:
                d+=1
    if d==0: return "D";
    if VALUE=="p1": return 1;
    elif VALUE=="p2": return 2;
    return 3;

print "TIC TAC TOE"
print "1 is for Player 1"
print "0 is for Player 2"
board=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
while(1):
    if Id=="p1": print "Player 1 TURN : "
    elif Id=="p2": print "Player 2 TURN"
    for i in range(len(board)):
        for j in range(len(board[i])):
            print board[i][j],
        print
    Prompt(board)
    if Decision(board)==1:
        print ("PLAYER 1 WON")
        Id=""
        if Id == "p1":
            print "Player 1 TURN : "
        elif Id == "p2":
            print "Player 2 TURN"
        for i in range(len(board)):
            for j in range(len(board[i])):
                print board[i][j],
            print
        break
    elif Decision(board)==2:
        print ("PLAYER 2 WON")
        Id=""
        if Id == "p1":
            print "Player 1 TURN : "
        elif Id == "p2":
            print "Player 2 TURN"
        for i in range(len(board)):
            for j in range(len(board[i])):
                print board[i][j],
            print
        break