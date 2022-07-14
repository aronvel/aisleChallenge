from game import Game
if __name__ == "__main__":
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []
    maxRow,maxCol=0,0
    while True:
        try:
            line = list(map(int,input().split(",")))
            contents.append(line)
            maxRow=max(line[0],maxRow)
            maxCol=max(line[1],maxCol)
        except EOFError:
            break
    
    game = Game()
    board=game.createBoard(maxRow+1,maxCol+1,contents)
    game.gameOfLife(board)
    livesAfterOneGen = game.getLivesIndices(board)
    for life in livesAfterOneGen:
        print(life[0],",",life[1])