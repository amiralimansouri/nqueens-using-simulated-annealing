import random
import math
import time

tempratue = 4000
def print_board(board,n):
    for x in board:
        for y in x:
            print(y, end=" ")
        print()
#This function simply prints the chess board
def check_zero(board,n):
    cnt =0
    b=0
    for i in range(n):
        for j in range(n):
            if board[i][j]=='q':
                for y in range(j + 1, 8, 1):
                    if board[i][y] == 'q':
                        cnt += 1
                        # right
                for y in range(j - 1, -1, -1):
                    if board[i][y] == 'q':
                        cnt += 1
                        # left
                b=j
                if i != 8:
                    for x in range(i + 1, 8, 1):
                        if b == 7:
                            break
                        b += 1
                        if board[x][b] == 'q':
                            cnt += 1
                            # bottom right
                b = j
                if i != 0:
                    for x in range(i - 1, -1, -1):
                        if b == 7:
                            break
                        b += 1
                        if board[x][b] == 'q':
                            cnt += 1
                            # top right
                b = j
                if i != 8:
                    for x in range(i + 1, 8, 1):
                        if b == -1:
                            break
                        b = b - 1
                        if board[x][b] == 'q':
                            cnt += 1
                            # bottom left
                b = j
                if i != 0:
                    for x in range(i - 1, -1, -1):
                        if b == -1:
                            break
                        b = b - 1
                        if board[x][b] == 'q':
                            cnt += 1
                            # top left
    return cnt
#this funtion checks for threats.it goes on and when it finds a queen.
#it checks every direction there can be another queen and when it reaches one, the number of threats++
#and at the end it returns the number of threats it found in the given board
def makesame(board,secboard,n):
    for i in range(n):
        for j in range(n):
            secboard[i][j]=board[i][j]
#copies one board to another one.here it copies board into secboard
def queenmove(secboard,n):
    rnd=random.randint(0,7)
    rows = 0
    for i in range(n-1,-1,-1):
        if secboard[i][rnd]=='q':
            rows=i
            break;
    rndpos=random.randint(0,7)
    while(rndpos ==rows):
        rndpos=random.randint(0,7)
    secboard[rndpos][rnd]='q'
    secboard[rows][rnd]=0
    """""""""
    threatcounts=check_zero(secboard,n)
    threatcountb=check_zero(board,n)
    if threatcounts>=threatcountb:
        while(threatcounts>=threatcountb):
            makesame(board,secboard,n)
            queenmove(board,secboard,n)
    else:
        threatcounttmp=check_zero(secboard,n)
        makesame(secboard, board, n)
        print_board(secboard,n)
        while(threatcounttmp!=0):
            makesame(secboard,board,n)
            queenmove(board,secboard,n)
            print_board(board,n)
    return board
    """""#here i made a recursive function so everytime our check_zero function returns
         #a number which is higher than the threats we already have, it calls itself again
         #and it does this until it reaches threats=0.but it wasnt working because from
         #a certain point where we have low threats.the random doesnt help the board
         #so it does it for a thousand times and quits.
    
#this function randomly picks one queen.generates another random number and if thi number is not
#the same as the current position,the queen moves to the new cell
def main():
    start_time=time.time()
    n =8
    done=0
    board = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        a=random.randint(0,7)
        board[a][i]='q'
        #for every column put a queen in a random cell
    print_board(board,n)
    print("the number of threats at first",check_zero(board,n))
    secboard = [[0 for i in range(n)] for j in range(n)]
    makesame(board,secboard,n)
    t=tempratue
    ch=0.99
    while t>0.001:
        t=t*ch
        queenmove(secboard,n)
        thcount_s=check_zero(secboard,n)
        thcount_b=check_zero(board,n)
        dif=thcount_s-thcount_b
        if dif<0 or random.uniform(0, 1) < math.exp(-dif / t):
            makesame(secboard,board,n)
        else:
            makesame(board,secboard,n)
        if thcount_s==0:
            done=done+1
            break
    if(done==1):
        print("successful.we made the chess board threatfree in ",time.time()-start_time)
    else:
        print("failed in",time.time()-start_time)
        last = check_zero(secboard, n)
        print("the number of threats at last is", last)
    print_board(board,n)
main()


