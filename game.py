class Game:
    def aliveNeighbour(self,board,i,j,m,n):
        lives = 0
        for a in range(max(i-1,0),min(i+1,m-1)+1):
            for b in range(max(j-1,0),min(j+1,n-1)+1):
                lives+=board[a][b]&1
        lives-=board[i][j]&1
        return lives
    
    def gameOfLife(self, board):
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.aliveNeighbour(board,i,j,m,n)
                curr = board[i][j]
                
                if curr == 1 and lives ==2 or lives ==3:
                    board[i][j]=3
                if curr == 0 and lives ==3:
                    board[i][j]=2
        for i in range(m):
            for j in range(n):
                board[i][j]=board[i][j]>>1
    
    def createBoard(self,row,col,livesIndices):
        board = [[0 for i in range(col)]for j in range(row)]

        for lifeIndex in livesIndices:
            x,y=lifeIndex[0],lifeIndex[1]
            board[x][y]=1
        return board
    def getLivesIndices(self,board):
        resIndices=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==1:
                    resIndices.append([i,j])
        return resIndices