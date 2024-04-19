board =[
    [1,9,1,4,2,3,8,9,1],
    [4,9,1,4,2,3,8,9,1],
    [2,9,1,4,2,3,8,9,1],
    [9,9,1,4,2,3,8,9,1],
    [1,9,1,4,0,3,8,9,1],
    [8,9,1,4,2,3,8,9,1],
    [1,9,1,4,2,3,8,9,1],
    [7,9,1,4,2,3,8,9,1],
    [3,9,1,4,2,3,8,9,0],
]

def print_board(bo):
    for i in range(len(bo)):
        if i %3 == 0 and i!=0:
            print("-----------")

        for j in range(len(bo)):
            if j%3==0 and j!=0:
                print("|",end="")
            
            if j==8:
                print(bo[i][j])
            else:
                print(bo[i][j] , end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j]==0:
                print("found 0 in position ",i,j)

print_board(board)
find_empty(board)