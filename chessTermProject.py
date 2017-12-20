#KASDAN BAKOS
#CHESS TERM PROJECT

#CITE: BAREBONES EVENT CODE FROM 15112 WEBSITE
#CITE: MODE EVENT CODE FROM 15112 WEBSITE
#CITE: IMAGES EXAMPLE FROM 15112 WEBSITE - imagesDemo1.py


'''
#THINGS I NEED TO FIX:
    NOTHING (-: 

'''

from tkinter import *
import copy
import random




####################################
# init
####################################

def init(data):
    data.mode = "startScreen"
    data.moves = [
              [
              [2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]
              ], #knight

              [
              [1,0],[2,0]
              ], #pawn
              
              [
              [1,-1],[1,0],[1,1],[0,-1],[0,1],[-1,-1],[-1,0],[-1,1],[0,-2],[0,2]
              ], #king
              
              [
               [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]], #left
               [[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7]], #right
               [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]], #down
               [[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0]], #up
               [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]], #down-R
               [[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7]],#down-L
               [[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7]], #up-L
               [[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7]] #up-R

                ], #queen

              [
               [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]], #left
               [[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7]], #right
               [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]], #down
               [[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0]] #up
                ], #rook

              [
               [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]], #down-R
               [[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7]], #up-R
               [[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7]],#up-L
               [[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7]] #down-L
                ] #bishop
              ]


    #PLAYER 1 PIECES
    data.whiteBishop = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/whiteBishop.gif")
    data.whiteBishopR = data.whiteBishop.subsample(3,3)

    data.whiteKing = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/whiteKing.gif")
    data.whiteKingR = data.whiteKing.subsample(3,3)
    
    data.whiteKnight = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/whiteKnight.gif")
    data.whiteKnightR = data.whiteKnight.subsample(3,3)
    
    data.whitePawn = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/whitePawn.gif")
    data.whitePawnR = data.whitePawn.subsample(3,3)
    
    data.whiteQueen = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/whiteQueen.gif")
    data.whiteQueenR = data.whiteQueen.subsample(3,3)
    
    data.whiteRook = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/whiteRook.gif")
    data.whiteRookR = data.whiteRook.subsample(3,3)

    #PLAYER 2 PIECES
    data.blackBishop = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/blackBishop.gif")
    data.blackBishopR = data.blackBishop.subsample(3,3)

    data.blackKing = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/blackKing.gif")
    data.blackKingR = data.blackKing.subsample(3,3)

    data.blackKnight = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/blackKnight.gif")
    data.blackKnightR = data.blackKnight.subsample(3,3)

    data.blackPawn = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/blackPawn.gif")
    data.blackPawnR = data.blackPawn.subsample(3,3)

    data.blackQueen = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/blackQueen.gif")
    data.blackQueenR = data.blackQueen.subsample(3,3)

    data.blackRook = PhotoImage(file="/Users/Kasdan/Documents/CMU S17/15112/Term Project/TP Deliverable Final/chessPieces gifs/blackRook.gif")
    data.blackRookR = data.blackRook.subsample(3,3)

    #team = [[piece, row, col, team, moves]]
    data.player1 = [
        ['Rook',0,0,'green',False], ['Knight',0,1,'green'],
        ['Bishop',0,2,'green'],['Queen', 0,3,'green'],
        ['King',0,4,'green',False, False, False],
        ['Bishop',0,5,'green'],['Knight',0,6,'green'],
        ['Rook',0,7,'green',False],
        ['Pawn',1,0,'green'],['Pawn',1,1,'green'], 
        ['Pawn',1,2,'green'], ['Pawn',1,3,'green'], 
        ['Pawn',1,4,'green'], ['Pawn',1,5,'green'], 
        ['Pawn',1,6,'green'], ['Pawn',1,7,'green']
                ]
    data.player2 = [
        ['Rook',7,0,'red',False], ['Knight',7,1,'red'], ['Bishop',7,2,'red'],
        ['Queen',7,3,'red'], ['King',7,4,'red',False, False, False], 
        ['Bishop',7,5,'red'],['Knight',7,6,'red'],['Rook',7,7,'red',False],
        ['Pawn',6,0,'red'],['Pawn',6,1,'red'], ['Pawn',6,2,'red'], 
        ['Pawn',6,3,'red'],['Pawn',6,4,'red'], ['Pawn',6,5,'red'], 
        ['Pawn',6,6,'red'], ['Pawn',6,7,'red']
                ]
    
    data.cols = 8
    data.rows = 8
    data.margin = 10
    data.gridWidth = (data.width - data.margin/2)
    data.gridHeight = (data.height - data.margin/2)
    data.cellSize = data.gridWidth/data.cols
    data.selectedRow = -1
    data.selectedCol = -1
    data.highlightColor = None
    data.currentPiece = None
    data.currentPlayer = 1
    data.moveList = []
    data.piece = None
    data.previousRow = -1
    data.previousCol = -1
    data.prevIndex1 = None
    data.prevIndex2 = None
    data.curIndex = None
    data.tempR1 = data.player1[4][1]
    data.tempC1 = data.player1[4][2] 
    data.tempR2 = data.player2[4][1]
    data.tempC2 = data.player2[4][2] 
    data.possiblePos = []
    data.temporaryMOVEHOLDER = []
    data.p1DefensiveMoves = []
    data.p2DefensiveMoves = []
    data.acceptablePieces = []
    data.checkMoveList = []
    data.putInCheck1 = []
    data.putInCheck2 = []
    data.count = 0
    data.lol = 0
    data.holdRAI = -1
    data.holdCAI = -1
    data.alpha = -999999999999
    data.beta = 999999999999
    data.v = None
    data.here = False
    


    
####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "startScreen"): startScreenMousePressed(event, data)
    elif(data.mode == "2P"):       mousePressed2P(event, data)
    elif (data.mode == "PvAIE"):   PvAIEMousePressed(event, data)
    elif (data.mode == "PvAIH"):   PvAIHMousePressed(event, data)
    elif (data.mode == "PvAIMenu"):   PvAIMenuMousePressed(event, data)
    elif(data.mode == "checkMate"):       mousePressedCheckMate(event, data)



    

def keyPressed(event, data):
    if (data.mode == "startScreen"): startScreenKeyPressed(event, data)
    elif (data.mode == "2P"):       keyPressed2P(event, data)
    elif (data.mode == "PvAIE"):   PvAIEKeyPressed(event, data)
    elif (data.mode == "PvAIH"):   PvAIHKeyPressed(event, data)
    elif (data.mode == "PvAIMenu"):   PvAIMenuKeyPressed(event, data)
    elif (data.mode == "checkMate"):       keyPressedCheckMate(event, data)


    

def timerFired(data):
    if (data.mode == "startScreen"): startScreenTimerFired(data)
    elif (data.mode == "2P"):       timerFired2P(data)
    elif (data.mode == "PvAIE"):   PvAIETimerFired(data)
    elif (data.mode == "PvAIH"):   PvAIHTimerFired(data)
    elif (data.mode == "PvAIMenu"):   PvAIMenuTimerFired(data)
    elif (data.mode == "checkMate"):       timerFiredCheckMate(data)
    

def redrawAll(canvas, data):
    if (data.mode == "startScreen"): startScreenRedrawAll(canvas, data)
    elif (data.mode == "2P"):       redrawAll2P(canvas, data)
    elif (data.mode == "PvAIE"):   PvAIERedrawAll(canvas, data)
    elif (data.mode == "PvAIH"):   PvAIHRedrawAll(canvas, data)
    elif (data.mode == "PvAIMenu"):   PvAIMenuRedrawAll(canvas, data)
    elif (data.mode == "checkMate"):       redrawAllCheckMate(canvas, data)

    

####################################
# startScreen mode
####################################

def startScreenMousePressed(event, data):
    if((event.x >= data.width/2-125 and event.x <= data.width/2+125)):
        if(event.y >= data.height/3+50 and event.y <= data.height/3+100):
            data.mode = '2P'
        elif(event.y >= data.height/2+75 and event.y <= data.height/2+125):
            data.mode = 'PvAIMenu'
    pass

def startScreenKeyPressed(event, data):
    pass

def startScreenTimerFired(data):
    pass

def startScreenRedrawAll(canvas, data):
    #BACKGROUND
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")

    #TITLE
    canvas.create_text(data.width/2, data.height/5+25,
                       text="C H E S S", font="Arial 60 bold", fill = "white")

    #PLAYER VS PLAYER
    canvas.create_rectangle(data.width/2-125, data.height/3+50,data.width/2+125, 
        data.height/3+100, fill = "white")
    canvas.create_text(data.width/2, data.height/3+75, 
        text='PLAYER VS PLAYER', font="Arial 20 bold", width = 250)

    #PLAYER VS AI
    canvas.create_rectangle(data.width/2-125, data.height/2+75,data.width/2+125, 
        data.height/2+125, fill = "white")
    canvas.create_text(data.width/2, data.height/2+100, 
        text='PLAYER VS AI', font="Arial 20 bold", width = 300)



####################################
# 2PLAYER mode
####################################

def mousePressed2P(event, data):
    getRowCol(event.x, event.y, data)
    movePiece(data)
    highlightMoves(data)

    

def keyPressed2P(event, data):
    if(event.keysym == "r"):
        init(data)

def timerFired2P(data):
    checkKing(data)
    changePawn(data)
    pass

def redrawAll2P(canvas, data):
    drawBoard(canvas, data)
    drawPieces(canvas,data)
    if(data.player1[4][6] == True):
        data.mode = 'checkMate'
        canvas.create_text(data.width/2, data.height/2, text = 'PLAYER 2 WINS')
    if(data.player2[4][6] == True):
        canvas.create_text(data.width/2, data.height/2, text = 'PLAYER 1 WINS')
        data.mode = 'checkMate'


####################################
# customize these functions
####################################


def changePawn(data):
    for i in range(len(data.player1)):
        if(data.player1[i][1] == 7 and data.player1[i][0] == 'Pawn'):
            data.player1[i][0] = 'Queen'

        if(data.player2[i][1] == 0 and data.player2[i][0] == 'Pawn'):
            data.player2[i][0] = 'Queen'




def drawBoard(canvas, data):
    margin = data.margin

    #DRAWS THE BOARD
    for row in range(data.rows):
        for col in range(data.cols):
            bounds = getCellBounds(row, col, data)
            if((row+col) % 2 == 0):
                canvas.create_rectangle(bounds[0], bounds[1], bounds[2], 
                    bounds[3], fill = "brown")
            else:
                canvas.create_rectangle(bounds[0], bounds[1], 
                    bounds[2], bounds[3], fill = "tan")
    
    #DRAWS THE BOX HIGHLIGHT
    bounds = getCellBounds(data.selectedRow, data.selectedCol, data)
    canvas.create_rectangle(bounds[0], bounds[1],bounds[2], 
        bounds[3], fill = data.highlightColor)
    



    #DRAWS MOVES HIGHLIGHT

    if(data.moveList != []):
        if(not isinstance(data.moveList[0][0],list)):
            for i in range(len(data.moveList)):
                bounds = getCellBounds(data.moveList[i][0], data.moveList[i][1], data)
                canvas.create_rectangle(bounds[0], bounds[1],bounds[2], 
                bounds[3], fill = "yellow")
        else:
            for i in range(len(data.moveList)):
                for j in range(len(data.moveList[i])):
                    bounds = getCellBounds(data.moveList[i][j][0], data.moveList[i][j][1], data)
                    canvas.create_rectangle(bounds[0], bounds[1],bounds[2], 
                    bounds[3], fill = "yellow")


    else:
        for i in range(len(data.moveList)):
            for j in range(len(data.moveList[i])):
                bounds = getCellBounds(data.moveList[i][j][0], data.moveList[i][j][1], data)
                canvas.create_rectangle(bounds[0], bounds[1],bounds[2], 
                bounds[3], fill = "yellow")



    #BOX FOR CHECK

    if(data.player1[4][5] == True):
        checkBox1 = getCellBounds(data.player1[4][1], data.player1[4][2],data)
        canvas.create_rectangle(checkBox1[0], checkBox1[1],checkBox1[2], 
        checkBox1[3], fill = "red")

    if(data.player2[4][5] == True):
        checkBox2 = getCellBounds(data.player2[4][1], data.player2[4][2],data)
        canvas.create_rectangle(checkBox2[0], checkBox2[1],checkBox2[2], 
        checkBox2[3], fill = "red")




def drawPieces(canvas, data):
    img = None
    margin = data.margin
    for i in range(len(data.player1)):
        bounds1 = getCellBounds(data.player1[i][1], data.player1[i][2], data)
        cX1 = (bounds1[0]+bounds1[2])/2
        cY1 = (bounds1[1]+bounds1[3])/2
        if(data.player1[i][0] == "Knight"): img = data.whiteKnightR
        elif(data.player1[i][0] == "Pawn"): img = data.whitePawnR
        elif(data.player1[i][0] == "King"): img = data.whiteKingR
        elif(data.player1[i][0] == "Queen"): img = data.whiteQueenR
        elif(data.player1[i][0] == "Rook"): img = data.whiteRookR
        elif(data.player1[i][0] == "Bishop"): img = data.whiteBishopR

        canvas.create_image(cX1, cY1-40, anchor=N, image=img)

    for j in range(len(data.player2)):
            bounds2 = getCellBounds(data.player2[j][1], data.player2[j][2], data)
            cX2 = (bounds2[0]+bounds2[2])/2
            cY2 = (bounds2[1]+bounds2[3])/2
            if(data.player2[j][0] == "Knight"): img = data.blackKnightR
            elif(data.player2[j][0] == "Pawn"): img = data.blackPawnR
            elif(data.player2[j][0] == "King"): img = data.blackKingR
            elif(data.player2[j][0] == "Queen"): img = data.blackQueenR
            elif(data.player2[j][0] == "Rook"): img = data.blackRookR
            elif(data.player2[j][0] == "Bishop"): img = data.blackBishopR
            canvas.create_image(cX2, cY2-40, anchor=N, image=img)

def getCellBounds(row, col, data):
    x0 = int((col * data.cellSize) + data.margin/2)
    y0 = int((row * data.cellSize) + data.margin/2)
    x1 = int(((col + 1) * data.cellSize) + data.margin/2)
    y1 = int(((row + 1) * data.cellSize) + data.margin/2)
    return (x0, y0, x1, y1)

def getRowCol(x, y, data):
    new = False
    data.selectedCol = x//data.cellSize
    data.selectedRow = y//data.cellSize

    #GETS CURRENT PIECE
    for i in range(len(data.player1)):
        if(data.player1[i][1] == data.selectedRow and 
            data.player1[i][2] == data.selectedCol and 
            data.currentPlayer == 1 and data.player1[i][0] != None):
                data.highlightColor = 'pink'
                data.currentPiece = data.player1[i][0]
                data.curIndex = i
                new = True

        elif(data.player2[i][1] == data.selectedRow and 
            data.player2[i][2] == data.selectedCol and 
            data.currentPlayer == 2 and  data.player2[i][0] != None):
                data.highlightColor = 'orange'
                data.currentPiece = data.player2[i][0]
                data.curIndex = i
                new = True
    if(new == False):
        data.highlightColor = None
        data.currentPiece = None

def getPawnMoves(data):
    data.moves[1] = [[1,0],[2,0]]
    if(data.selectedRow != 1 and data.selectedRow != 6):
        data.moves[1].remove([2,0])

    #takes care of double move from start if player is in front
    for k in range(len(data.player1)):
        if(data.currentPlayer == 1):
            if(((data.player1[k][1] == data.selectedRow+1 and 
                data.player1[k][2] == data.selectedCol) or 
            (data.player1[k][1] == data.selectedRow+2 and 
                data.player1[k][2] == data.selectedCol)) and 
            ([2,0] in data.moves[1])):
                    data.moves[1].remove([2,0])


            if(((data.player2[k][1] == data.selectedRow+1 and 
                data.player2[k][2] == data.selectedCol) or 
            (data.player2[k][1] == data.selectedRow+2 and 
                data.player2[k][2] == data.selectedCol)) and 
                ([2,0] in data.moves[1])):
                    data.moves[1].remove([2,0])
        else:
            if(((data.player1[k][1] == data.selectedRow-1 and 
                data.player1[k][2] == data.selectedCol) or 
            (data.player1[k][1] == data.selectedRow-2 and 
                data.player1[k][2] == data.selectedCol)) and 
            ([2,0] in data.moves[1])):
                    data.moves[1].remove([2,0])


            if(((data.player2[k][1] == data.selectedRow-1 and 
                data.player2[k][2] == data.selectedCol) or 
            (data.player2[k][1] == data.selectedRow-2 and 
                data.player2[k][2] == data.selectedCol)) and 
                ([2,0] in data.moves[1])):
                    data.moves[1].remove([2,0])


    if(data.currentPlayer == 1):
        for i in range(len(data.player2)):
            if(data.selectedRow+1 == data.player2[i][1] and 
                data.selectedCol == data.player2[i][2] and 
                data.player2[i][0] != None):
                    if([1,0] in data.moves[1]):
                        data.moves[1].remove([1,0])
            if(data.selectedRow+1 == data.player2[i][1] and 
                data.selectedCol+1 == data.player2[i][2] and 
                data.player2[i][0] != None):
                    if([1,1] not in data.moves[1]):
                        data.moves[1].append([1,1])
            if(data.selectedRow+1 == data.player2[i][1] and 
                data.selectedCol-1 == data.player2[i][2] and 
                data.player2[i][0] != None):
                    if([1,-1] not in data.moves[1]):
                        data.moves[1].append([1,-1])
    else:
        for j in range(len(data.player1)):
            if(data.selectedRow-1 == data.player1[j][1] and 
                data.selectedCol == data.player1[j][2] 
                and data.player1[j][0] != None):
                    if([1,0] in data.moves[1]):
                        data.moves[1].remove([1,0])
            if(data.selectedRow-1 == data.player1[j][1] and 
                data.selectedCol+1 == data.player1[j][2] and 
                data.player1[j][0] != None):
                    if([1,1] not in data.moves[1]):
                        data.moves[1].append([1,1])
            if(data.selectedRow-1 == data.player1[j][1] and 
                data.selectedCol-1 == data.player1[j][2] and 
                data.player1[j][0] != None):
                    if([1,-1] not in data.moves[1]):
                        data.moves[1].append([1,-1])



def highlightMoves(data):
    if(data.player1[4][5] == True):

        
        s = set()
        for x in range(len(data.checkMoveList)):
            s.add(tuple(data.checkMoveList[x]))
            #get rid of duplicates

        data.checkMoveList = list(s)
        #change set back to list
        for y in range(len(data.checkMoveList)):
            data.checkMoveList[y] = list(data.checkMoveList[y])
            #change elements back to lists from tuples
        data.moveList = []
        


        if(data.currentPiece != None):
            if(data.checkMoveList != [] or data.possiblePos != []):
                if(data.currentPiece == "Knight"): data.piece = 0
                elif(data.currentPiece == "Pawn"): data.piece = 1
                elif(data.currentPiece == "King"): data.piece = 2
                elif(data.currentPiece == "Queen"): data.piece = 3
                elif(data.currentPiece == "Rook"): data.piece = 4
                elif(data.currentPiece == "Bishop"): data.piece = 5

                
                for r in range(len(data.possiblePos)):
                    if(data.possiblePos[r] in data.checkMoveList and (data.possiblePos[r] != [data.player2[data.prevIndex1][1],data.player2[data.prevIndex1][2]])):
                        data.checkMoveList.remove(data.possiblePos[r])

                for p in data.acceptablePieces:
                    if(data.curIndex == p):
                        if(data.player1[p][0] == 'King'):
                            data.moveList = data.possiblePos


                        elif(data.player1[p][0] != "Bishop" and data.player1[p][0] != "Queen" and data.player1[p][0] != "Rook"):
                            for m in range(len(data.moves[data.piece])):
                                if([data.player1[p][1] + data.moves[data.piece][m][0], data.player1[p][2] + data.moves[data.piece][m][1]] in data.checkMoveList):
                                    if(isLegalMove(data.player1[p][1] + data.moves[data.piece][m][0], data.player1[p][2] + data.moves[data.piece][m][1], data)):
                                        data.moveList.append([data.player1[p][1] + data.moves[data.piece][m][0], data.player1[p][2] + data.moves[data.piece][m][1]])
                        else:
                            for m in range(len(data.moves[data.piece])):
                                for n in range(len(data.moves[data.piece][m])):
                                    if([data.player1[p][1] + data.moves[data.piece][m][n][0], data.player1[p][2] + data.moves[data.piece][m][n][1]] in data.checkMoveList):
                                        if(isLegalMove(data.player1[p][1] + data.moves[data.piece][m][n][0], data.player1[p][2] + data.moves[data.piece][m][n][1], data)):
                                            if([data.player1[p][1] + data.moves[data.piece][m][n][0], data.player1[p][2] + data.moves[data.piece][m][n][1]] in getMoves(data,data.player1[p][0],data.player1[p][1],data.player1[p][2])):
                                                data.moveList.append([data.player1[p][1] + data.moves[data.piece][m][n][0], data.player1[p][2] + data.moves[data.piece][m][n][1]])

        
            if(data.possiblePos == [] and data.checkMoveList == []):
                data.player1[4][6] = True

    ###########################################################
    ###########################################################
    #PLAYER 2
    ###########################################################
    ###########################################################


    elif(data.player2[4][5] == True):
        s = set()
        for x in range(len(data.checkMoveList)):
            s.add(tuple(data.checkMoveList[x]))
            #get rid of duplicates

        data.checkMoveList = list(s)
        #change set back to list
        for y in range(len(data.checkMoveList)):
            data.checkMoveList[y] = list(data.checkMoveList[y])
            #change elements back to lists from tuples
        data.moveList = []

        
        if(data.currentPiece != None):
            if(data.checkMoveList != [] or data.possiblePos != []):
                if(data.currentPiece == "Knight"): data.piece = 0
                elif(data.currentPiece == "Pawn"): data.piece = 1
                elif(data.currentPiece == "King"): data.piece = 2
                elif(data.currentPiece == "Queen"): data.piece = 3
                elif(data.currentPiece == "Rook"): data.piece = 4
                elif(data.currentPiece == "Bishop"): data.piece = 5
                
                for r in range(len(data.possiblePos)):
                    if(data.possiblePos[r] in data.checkMoveList and (data.possiblePos[r] != [data.player1[data.prevIndex2][1],data.player1[data.prevIndex2][2]])):
                        data.checkMoveList.remove(data.possiblePos[r])

                for p in data.acceptablePieces:
                    if(data.curIndex == p):
                        if(data.player2[p][0] == 'King'):
                            data.moveList = data.possiblePos

                        elif(data.player2[p][0] == 'Pawn'):
                            for m in range(len(data.moves[data.piece])):
                                if([data.player2[p][1] - data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1]] in data.checkMoveList):
                                    data.moveList.append([data.player2[p][1] - data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1]])


                        elif(data.player2[p][0] != "Bishop" and data.player2[p][0] != "Queen" and data.player2[p][0] != "Rook"):
                            for m in range(len(data.moves[data.piece])):
                                if([data.player2[p][1] + data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1]] in data.checkMoveList):
                                    if(isLegalMove(data.player2[p][1] + data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1], data)):
                                        data.moveList.append([data.player2[p][1] + data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1]])
                        else:
                            for m in range(len(data.moves[data.piece])):
                                for n in range(len(data.moves[data.piece][m])):
                                    if([data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1]] in data.checkMoveList):
                                        if(isLegalMove(data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1], data)):
                                            if([data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1]] in getMoves(data,data.player2[p][0],data.player2[p][1],data.player2[p][2])):
                                                data.moveList.append([data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1]])
                            


        if(data.possiblePos == [] and data.checkMoveList == []):
            data.player2[4][6] = True


    #IF NEITHER KING IS IN CHECK DO THIS
    else:
        data.acceptablePieces = [e for e in range(len(data.player1))]
        data.p1DefensiveMoves = []
        data.p2DefensiveMoves = []
        if(data.currentPiece == None): 
            data.moveList = []
            return
        elif(data.currentPiece == "Knight"): data.piece = 0
        elif(data.currentPiece == "Pawn"): data.piece = 1
        elif(data.currentPiece == "King"): data.piece = 2
        elif(data.currentPiece == "Queen"): data.piece = 3
        elif(data.currentPiece == "Rook"): data.piece = 4
        elif(data.currentPiece == "Bishop"): data.piece = 5
        

        l = 0 #FOR THE KNIGHT AND KINGS MOVES
        setL = 0 #FOR BISHOP, ROOK, QUEEN
        moveL = 0 #FOR BISHOP, ROOK, QUEEN

        #moves for Bishop, Rook, Queen
        if(data.currentPiece == 'Bishop' or data.currentPiece == 'Rook' or 
            data.currentPiece == 'Queen'):
            while setL < len(data.moves[data.piece]):
                b = False
                while moveL < len(data.moves[data.piece][setL]):
                    mRow = data.selectedRow+data.moves[data.piece][setL][moveL][0]
                    mCol = data.selectedCol+data.moves[data.piece][setL][moveL][1]
                    if(isLegalMove(mRow, mCol, data)):
                        data.moveList.append([mRow, mCol])

                        #checks if player1 hits player2's piece
                        if(data.currentPlayer == 1):
                            for x in range(len(data.player2)):
                                if(data.player2[x][1] == mRow and 
                                    data.player2[x][2] == mCol and 
                                    data.player2[x][0] != None):
                                        b = True         

                        #checks if player2 hits player1s piece
                        else:
                            for y in range(len(data.player1)):
                                if(data.player1[y][1] == mRow and 
                                    data.player1[y][2] == mCol and 
                                    data.player1[y][0] != None):
                                        b = True   
                    #hit own piece
                    else:
                        setL += 0
                        moveL = 0
                        break

                    #hit other players piece
                    if(b == True):
                            setL += 1
                            moveL = 0                        
                            break
                    moveL += 1

                if(b != True):
                    setL += 1
                    moveL = 0


        #moves for Knights
        elif(data.currentPiece == 'Knight'):
            while l < len(data.moves[data.piece]):
                kRow = data.selectedRow+data.moves[data.piece][l][0]
                kCol = data.selectedCol+data.moves[data.piece][l][1]
                if(isLegalMove(kRow, kCol, data)):
                    data.moveList.append([kRow, kCol])
                l += 1

        #moves for Kings
        elif(data.currentPiece == 'King'):
            kingCastle(data)
            #possiblePos = []
            checkKing(data)
            data.possiblePos = checkKing(data)



            for i in range(len(data.possiblePos)):
                if(data.currentPlayer == 1):
                    if([data.possiblePos[i][0]-data.player1[4][1],data.possiblePos[i][1]-data.player1[4][2]] in data.moves[2]):
                        data.moveList.append([data.possiblePos[i][0],data.possiblePos[i][1]])

                else:
                    if([data.possiblePos[i][0]-data.player2[4][1],data.possiblePos[i][1]-data.player2[4][2]] in data.moves[2]):
                        data.moveList.append([data.possiblePos[i][0],data.possiblePos[i][1]])  
            

            #MAKES IT SO YOU CAN'T CASTLE THROUGH CHECK
            if(data.currentPlayer == 1):
                if([0,5] not in data.moveList and [data.player1[4][1]+0,data.player1[4][1]+1] == [0,5]):
                    if([0,6] in data.moveList):
                        data.moveList.remove([0,6])
                if([0,3] not in data.moveList and [data.player1[4][1]+0,data.player1[4][1]-1] == [0,3]):
                    if([0,2] in data.moveList):
                        data.moveList.remove([0,2])
            else:
                if([7,5] not in data.moveList and [data.player2[4][1]+0,data.player2[4][1]+1] == [7,5]):
                    if([7,6] in data.moveList):
                        data.moveList.remove([7,6])
                if([7,3] not in data.moveList and [data.player2[4][1]+0,data.player2[4][1]-1] == [7,3]):
                    if([7,2] in data.moveList):
                        data.moveList.remove([7,2])


        #PAWN MOVESET
        else:
            getPawnMoves(data)
            pawnL = []
            for m in data.moves[1]:
                if(data.currentPlayer == 1):
                    if(isLegalMove(data.selectedRow+m[0], data.selectedCol+m[1], data)):
                        data.moveList.append([data.selectedRow+m[0], data.selectedCol+m[1]])
                else:
                    if(isLegalMove(data.selectedRow-m[0], data.selectedCol+m[1], data)):
                        data.moveList.append([data.selectedRow-m[0], data.selectedCol+m[1]])


        #MAKES SURE YOU CANT MOVE A PIECE THAT TAKES YOU OUT OF CHECK
        hahList = []
        tracker = 0
        word = 0
        for z in range(len(data.moveList)):
            if(data.currentPlayer == 1):
                for o in range(len(data.moveList)):
                    if([data.moveList[z][0],data.moveList[z][1]] == data.putInCheck1):
                        word += 1

                if(intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player1[data.curIndex]) and word == 0):
                    if(data.curIndex in data.acceptablePieces):
                        data.acceptablePieces.remove(data.curIndex)

                if(not intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player1[data.curIndex]) or [data.moveList[z][0],data.moveList[z][1]] == data.putInCheck1):
                    hahList.append(data.moveList[z])
                    if(data.curIndex not in data.acceptablePieces):
                        data.acceptablePieces.append(data.curIndex)
                else:
                    tracker += 1

            elif(data.currentPlayer == 2):
                for o in range(len(data.moveList)):
                    if([data.moveList[z][0],data.moveList[z][1]] == data.putInCheck2):
                        word += 1

                if(intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player2[data.curIndex]) and word  == 0):
                    if(data.curIndex in data.acceptablePieces):
                        data.acceptablePieces.remove(data.curIndex)

                if(not intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player2[data.curIndex]) or [data.moveList[z][0],data.moveList[z][1]] == data.putInCheck2):
                    hahList.append(data.moveList[z])
                    if(data.curIndex not in data.acceptablePieces):
                        data.acceptablePieces.append(data.curIndex)
                else:
                    tracker += 1


            if(data.currentPlayer == 1 and tracker > 0):
                if(data.moveList[z] == data.putInCheck1):
                    hahList.append(data.moveList[z])

            elif(data.currentPlayer == 2 and tracker > 0):
                if(data.moveList[z] == data.putInCheck2):
                    hahList.append(data.moveList[z])


        if(hahList != [] and data.curIndex in data.acceptablePieces):
            data.moveList = hahList
        else:
            data.moveList = []


def isLegalMove(row, col, data):

    data.player1[4][0] = "King"

    if((row < 0 or row > 7) or (col < 0 or col > 7)):
        return False

    if(data.currentPlayer == 1):
        for i in range(len(data.player1)):
            if(data.player1[i][1] == row and data.player1[i][2] == col and 
                data.player1[i][0] != None):
                return False
    elif(data.currentPlayer == 2):
        for j in range(len(data.player2)):
            if(data.player2[j][1] == row and data.player2[j][2] == col and 
                data.player2[j][0] != None):
                return False
    return True



def movePiece(data):
    previousRow = data.selectedRow
    previousCol = data.selectedCol
    for i in range(len(data.moveList)):
        #MAKES SURE THAT THE MOVE SELECTED IS ONE THAT THE PIECE CAN MOVE INTO
        if(data.selectedRow == data.moveList[i][0] and 
            data.selectedCol == data.moveList[i][1]):
            if(data.currentPlayer == 1):
                data.prevIndex2 = data.curIndex
                data.player1[data.curIndex][1] = data.moveList[i][0]
                data.player1[data.curIndex][2] = data.moveList[i][1]

                if(data.curIndex == 4):
                    if(data.player1[data.curIndex][2] == 2 and data.player1[data.curIndex][1] == 0 and data.player1[4][4] == False):
                        data.player1[0][2] = 3
                    elif(data.player1[data.curIndex][2] == 6 and data.player1[data.curIndex][1] == 0 and data.player1[4][4] == False):
                        data.player1[7][2] = 5

                data.currentPlayer = 2

                
                for j in range(len(data.player2)):
                    if(data.player2[j][1] == data.player1[data.curIndex][1] and 
                        data.player2[j][2] == data.player1[data.curIndex][2]):
                        data.player2[j][0] = None
                        data.player2[j][1] = -1
                        data.player2[j][2] = -1
            else:
                data.prevIndex1 = data.curIndex
                data.player2[data.curIndex][1] = data.moveList[i][0]
                data.player2[data.curIndex][2] = data.moveList[i][1]
                data.currentPlayer = 1

                if(data.curIndex == 4):
                    if(data.player2[data.curIndex][2] == 2 and data.player2[data.curIndex][1] == 7 and data.player2[4][4] == False):
                        data.player2[0][2] = 3
                    elif(data.player2[data.curIndex][2] == 6 and data.player2[data.curIndex][1] == 7 and data.player2[4][4] == False):
                        data.player2[7][2] = 5

                for k in range(len(data.player1)):
                    if(data.player1[k][1] == data.player2[data.curIndex][1] and 
                        data.player1[k][2] == data.player2[data.curIndex][2]):
                        data.player1[k][0] = None
                        data.player1[k][1] = -1
                        data.player1[k][2] = -1

    if(data.moveList != []):
        data.moveList = []
    
    data.tempR1 = data.player1[4][1]
    data.tempC1 = data.player1[4][2]

    data.tempR2 = data.player2[4][1]
    data.tempC2 = data.player2[4][2]

    data.player1[4][5] = inCheck(data.player1[4][1], data.player1[4][2],1,data,1)
    data.player2[4][5] = inCheck(data.player2[4][1], data.player2[4][2],2,data,1)

    if(data.player1[4][5] == True or data.player2[4][5] == True):
        findMoves(data)
        data.moves = data.temporaryMOVEHOLDER

    if(data.player1[4][5] == False and data.player2[4][5] == False):
        data.checkMoveList = []



def getMoves(data, piece, row, col):
    moveList = []
    if(piece == "Knight"): pieceInd = 0
    elif(piece == "Pawn"): pieceInd = 1
    elif(piece == "King"): pieceInd = 2
    elif(piece == "Queen"): pieceInd = 3
    elif(piece == "Rook"): pieceInd = 4
    elif(piece == "Bishop"): pieceInd = 5
    

    l = 0 #FOR THE KNIGHT AND KINGS MOVES
    setL = 0 #FOR BISHOP, ROOK, QUEEN
    moveL = 0 #FOR BISHOP, ROOK, QUEEN

    #moves for Bishop, Rook, Queen
    if(piece == 'Bishop' or piece == 'Rook' or 
        piece == 'Queen'):
        while setL < len(data.moves[pieceInd]):
            b = False
            while moveL < len(data.moves[pieceInd][setL]):
                mRow = row+data.moves[pieceInd][setL][moveL][0]
                mCol = col+data.moves[pieceInd][setL][moveL][1]

                if(data.currentPlayer == 1):
                    if(mRow == data.player1[4][1] and mCol == data.player1[4][2]):
                        moveList.append([mRow, mCol]) 
                else:
                    if(mRow == data.player2[4][1] and mCol == data.player2[4][2]):
                        moveList.append([mRow, mCol]) 

                if(isLegalMove(mRow, mCol, data)):
                    moveList.append([mRow, mCol])

                    #checks if player1 hits player2's piece
                    if(data.currentPlayer == 1):
                        for x in range(len(data.player2)):
                            if(data.player2[x][1] == mRow and 
                                data.player2[x][2] == mCol and 
                                data.player2[x][0] != None):
                                    b = True 



                    #checks if player2 hits player1s piece
                    else:
                        for y in range(len(data.player1)):
                            if(data.player1[y][1] == mRow and 
                                data.player1[y][2] == mCol and 
                                data.player1[y][0] != None):
                                    b = True
                #hit own piece
                else:

                    setL += 0
                    moveL = 0
                    break

                #hit other players piece
                if(b == True):
                        setL += 1
                        moveL = 0                        
                        break
                moveL += 1

            if(b != True):
                setL += 1
                moveL = 0


    #moves for Kings and Knights
    elif(piece == 'Knight'):
        while l < len(data.moves[pieceInd]):
            kRow = row+data.moves[pieceInd][l][0]
            kCol = col+data.moves[pieceInd][l][1]

            if(data.currentPlayer == 1):
                if(kRow == data.player1[4][1] and kCol == data.player1[4][2]):
                    moveList.append([kRow, kCol]) 
            else:
                if(kRow == data.player2[4][1] and kCol == data.player2[4][2]):
                    moveList.append([kRow, kCol]) 

            if(isLegalMove(kRow, kCol, data)):
                moveList.append([kRow, kCol])
            l += 1
        


    elif(piece == 'King'):
        kingCastle(data)
        
        for i in range(len(data.moves[pieceInd])):
            kRow = row+data.moves[pieceInd][i][0]
            kCol = col+data.moves[pieceInd][i][1]
            
            if(isLegalMove(kRow, kCol, data)):
                moveList.append([kRow,kCol])
        


    #PAWN MOVESET
    else:
        getPawnMoves(data)
        pawnL = [[1,-1],[1,1]]
        for m in pawnL:
            #if(data.mode == '2P'):
            if(data.currentPlayer == 1):
                pRow = row+m[0]
                pCol = col+m[1]
                if(pRow == data.player1[4][1] and pCol == data.player1[4][2]):
                    moveList.append([pRow, pCol])
                if(isLegalMove(pRow, pCol, data)):
                    moveList.append([pRow, pCol])
            else:
                pRow = row-m[0]
                pCol = col+m[1]
                if(pRow == data.player2[4][1] and pCol == data.player2[4][2]):
                    moveList.append([pRow, pCol])
                if(isLegalMove(pRow, pCol, data)):
                    moveList.append([pRow, pCol])

    
    data.player1[4][1] = data.tempR1
    data.player1[4][2] = data.tempC1

    data.player2[4][1] = data.tempR2
    data.player2[4][2] = data.tempC2

    return moveList


###################################
#EXPERIMENT FOR CHECK FOR KING
###################################
#ROW AND COL ARE THE KINGS POSITION PLAYER IS CURRENT PLAYER
#FOR PAWN MAKE IT SO YOU LOOK FOR A PAWN AT CHECK POSITIONS OF KING
def inCheck(row, col, player, data, default = 0):
    if(player == 1):
        for i in range(len(data.player2)):
            #DOES CHECK FOR PAWNS
            if(data.player2[i][0] == "Pawn"):
                if(((data.player2[i][1] == row+1 and data.player2[i][2]==col+1) 
                    or(data.player2[i][1]==row+1 and data.player2[i][2]==col-1)) 
                and default == 1):
                    return True
            else:
                #DOES CHECK FOR REST OF PLAYERS
                moveList = getMoves(data, data.player2[i][0], data.player2[i][1], data.player2[i][2])
                if([row,col] in moveList):
                    data.putInCheck1 = [data.player2[i][1],data.player2[i][2]]
                    return True
    else:
        for j in range(len(data.player1)):
            if(data.player1[j][0] == "Pawn"):
                if(((data.player1[j][1] == row-1 and data.player1[j][2] == col+1) or (data.player1[j][1] == row-1 and data.player1[j][2] == col-1)) and default == 1):
                    return True
            else:
                moveList = getMoves(data, data.player1[j][0], data.player1[j][1], data.player1[j][2])
                if([row,col] in moveList):
                    data.putInCheck2 = [data.player1[j][1],data.player1[j][2]]
                    return True
    return False




###################################
#EXPERIMENT FOR CHECK FOR KING
###################################

#DETERMINES WHICH MOVES A KING CAN'T MAKE
def checkKing(data):

    pawnMove = [[1,1],[1,-1]]
    removeList = []
    finalKingList = []
    tKingMove = []

    if(data.currentPlayer == 1):
        kingMoves = getMoves(data, "King",data.player1[4][1],data.player1[4][2])
        
        for i in range(len(data.player2)):

            piece = data.player2[i][0]
            row  = data.player2[i][1]
            col = data.player2[i][2]

            data.tempR1 = data.player1[4][1]
            data.tempC1 = data.player1[4][2]



            data.player1[4][0] = None

            data.player1[4][1] = -1
            data.player1[4][2] = -1

            #ALL OF THE POSSIBLE MOVES OF ALL OF THE OTHER PIECES FOR PLAYER 2
            moveList = getMoves(data, piece, row, col)


            data.player1[4][0] = "King"
            data.player1[4][1] = data.tempR1
            data.player1[4][2] = data.tempC1

            #PAWNS ARE DIFF CAUSE THEY GO DIAGONAL TO TAKE PIECES NOT FORWARD
            if(piece == "Pawn"):
                moveList = []
                for b in range(len(pawnMove)):
                    moveList.append([row - pawnMove[b][0], col + pawnMove[b][1]])
            


            
            for j in range(len(kingMoves)):
                if(kingMoves[j] not in moveList):
                    if(kingMoves[j] not in tKingMove):
                        tKingMove.append(kingMoves[j])
                else:
                    if(kingMoves[j] not in removeList):
                        removeList.append(kingMoves[j])
            kingMoves = tKingMove

        for k in range(len(kingMoves)):
            if(kingMoves[k] not in removeList):
                finalKingList.append(kingMoves[k])
        return finalKingList


                ###############     PLAYER 2    ###############

    else:
        kingMoves = getMoves(data, "King",data.player2[4][1],data.player2[4][2])


        for i in range(len(data.player1)):

            piece = data.player1[i][0]
            row  = data.player1[i][1]
            col = data.player1[i][2]

            data.tempR2 = data.player2[4][1]
            data.tempC2 = data.player2[4][2]

            data.player2[4][0] = None
            data.player2[4][1] = -1
            data.player2[4][2] = -1

            moveList = getMoves(data, piece, row, col)

            data.player2[4][0] = "King"
            data.player2[4][1] = data.tempR2
            data.player2[4][2] = data.tempC2
            #moveList is all of the possible moves of the other team
            
            if([data.player2[4][1],data.player2[4][2]] in moveList):
                data.player2[4][5] = True


            if(piece == "Pawn"):
                moveList = []
                for b in range(len(pawnMove)):
                    moveList.append([row + pawnMove[b][0], col + pawnMove[b][1]])



            for j in range(len(kingMoves)):
                if(kingMoves[j] not in moveList):
                    if(kingMoves[j] not in tKingMove):
                        tKingMove.append(kingMoves[j])
                else:
                    if(kingMoves[j] not in removeList):
                        removeList.append(kingMoves[j])
            kingMoves = tKingMove


        for k in range(len(kingMoves)):
            if(kingMoves[k] not in removeList):
                finalKingList.append(kingMoves[k])

        return finalKingList






def kingCastle(data):
    
    #ALWAYS ADD IN CASTLING MOVES INITIALLY --> REMOVE LATER BY CONDITIONS
    if([0,-2] not in data.moves[2]):
        data.moves[2].append([0,-2])
    if([0,2] not in data.moves[2]):
        data.moves[2].append([0,2])



    #######     PLAYER 1   ###########
    if(data.currentPlayer == 1):

        data.player1[4][0] = 'King'
        data.player1[4][1] = data.tempR1
        data.player1[4][2] = data.tempC1

        #checks if in check
        if(data.player1[4][5] == True): 
            if([0,-2] in data.moves[2]):
                data.moves[2].remove([0,-2])
            if([0,2] in data.moves[2]):
                data.moves[2].remove([0,2])

        if(data.player1[4][1] != 0 or data.player1[4][2] != 4): #KING
            data.player1[4][4] = True

        if(data.player1[0][1] != 0 or data.player1[0][2] != 0): #LEFT ROOK
            data.player1[0][4] = True
            if([0,-2] in data.moves[2]):
                data.moves[2].remove([0,-2])

        if(data.player1[7][1] != 0 or data.player1[7][2] != 7): #RIGHT ROOK
            data.player1[7][4] = True
            if([0,2] in data.moves[2]):
                data.moves[2].remove([0,2])


        #IF KING HAS BEEN MOVED
        if(data.player1[4][4] == True): 
            if([0,-2] in data.moves[2]):
                data.moves[2].remove([0,-2])
            if([0,2] in data.moves[2]):
                data.moves[2].remove([0,2])
            return
            #KING
            
        #IF LEFT ROOK HASN'T BEEN MOVED CHECKS IF PIECES ARE BETWEEN
        if(data.player1[0][4] == False):
            for i in range(len(data.player1)):
                if((data.player1[i][1] == 0 and data.player1[i][2] == 1) or 
                    (data.player1[i][1] == 0 and data.player1[i][2] == 2) or 
                    (data.player1[i][1] == 0 and data.player1[i][2] == 3) or 
                    (data.player2[i][1] == 0 and data.player2[i][2] == 1) or 
                    (data.player2[i][1] == 0 and data.player2[i][2] == 2) or 
                    (data.player2[i][1] == 0 and data.player2[i][2] == 3)):
                    if([0,-2] in data.moves[2]):
                        data.moves[2].remove([0,-2])


        #IF RIGHT ROOK HASN'T BEEN MOVED CHECKS IF PIECES ARE BETWEEN
        if(data.player1[7][4] == False):   
            for a in range(len(data.player1)):
                if((data.player1[a][1] == 0 and data.player1[a][2] == 5) or 
                    (data.player1[a][1] == 0 and data.player1[a][2] == 6) or 
                    (data.player2[a][1] == 0 and data.player2[a][2] == 5) or 
                    (data.player2[a][1] == 0 and data.player2[a][2] == 6)):
                    if([0,2] in data.moves[2]):
                        data.moves[2].remove([0,2])
        

        data.player1[4][0] = None
        data.player1[4][1] = -1
        data.player1[4][2] = -1



        #########   PLAYER 2   #########
    else:

        data.player2[4][0] = 'King'
        data.player2[4][1] = data.tempR2
        data.player2[4][2] = data.tempC2

        #checks for if in check
        if(data.player2[4][5] == True): 
            if([0,-2] in data.moves[2]):
                data.moves[2].remove([0,-2])
            if([0,2] not in data.moves[2]):
                data.moves[2].remove([0,2])

        if(data.player2[4][1] != 7 or data.player2[4][2] != 4): #KING
            data.player2[4][4] = True

        if(data.player2[0][1] != 7 or data.player2[0][2] != 0): #LEFT ROOK
            data.player2[0][4] = True
            if([0,-2] in data.moves[2]):
                data.moves[2].remove([0,-2])

        
        if(data.player2[7][1] != 7 or data.player2[7][2] != 7): #RIGHT ROOK
            data.player2[7][4] = True
            if([0,2] in data.moves[2]):
                data.moves[2].remove([0,2])


        #IF KING HAS BEEN MOVED
        if(data.player2[4][4] == True): 
            if([0,-2] in data.moves[2]):
                data.moves[2].remove([0,-2])
            if([0,2] in data.moves[2]):
                data.moves[2].remove([0,2])
            return
            #KING


        #IF LEFT ROOK HASN'T BEEN MOVED CHECKS IF PIECES ARE BETWEEN
        if(data.player2[0][4] == False):
            for j in range(len(data.player1)):
                if((data.player1[j][1] == 7 and data.player1[j][2] == 1) or 
                    (data.player1[j][1] == 7 and data.player1[j][2] == 2) or 
                    (data.player1[j][1] == 7 and data.player1[j][2] == 3) or 
                    (data.player2[j][1] == 7 and data.player2[j][2] == 1) or 
                    (data.player2[j][1] == 7 and data.player2[j][2] == 2) or 
                    (data.player2[j][1] == 7 and data.player2[j][2] == 3)):
                    if([0,-2] in data.moves[2]):
                        data.moves[2].remove([0,-2])
        else: 
            if([0,-2] in data.moves[2]):
                data.moves[2].remove([0,-2])


        #IF RIGHT ROOK HASN'T BEEN MOVED CHECKS IF PIECES ARE BETWEEN
        if(data.player2[7][4] == False):           
            for b in range(len(data.player1)):
                if((data.player1[b][1] == 7 and data.player1[b][2] == 5) or 
                    (data.player1[b][1] == 7 and data.player1[b][2] == 6) or 
                    (data.player2[b][1] == 7 and data.player2[b][2] == 5) or 
                    (data.player2[b][1] == 7 and data.player2[b][2] == 6)):
                    if([0,2] in data.moves[2]):
                        data.moves[2].remove([0,2])
        else:
            if([0,2] in data.moves[2]):
                data.moves[2].remove([0,2])



def findMoves(data):
    
    data.temporaryMOVEHOLDER = data.moves
    
    data.possiblePos = checkKing(data)

    if(data.possiblePos != []):
        if(4 not in data.acceptablePieces):
            data.acceptablePieces.append(4)


    if(data.player1[4][5] == True):
        legalCheckMoves = []
        for i in range(len(data.player1)):
            posMoves = getMoves(data, data.player1[i][0], data.player1[i][1], data.player1[i][2])
            if(data.player1[i][0] == 'Pawn'):
                posMoves = []
                pawnMoves = [[1,0],[2,0]]
                for x in range(len(pawnMoves)):
                    posMoves.append([data.player1[i][1] + pawnMoves[x][0], data.player1[i][2] + pawnMoves[x][1]])

            if(data.player1[i][0] == "Knight"): piece = 0
            elif(data.player1[i][0] == "Pawn"): piece = 1
            elif(data.player1[i][0] == "King"): piece = 2
            elif(data.player1[i][0] == "Queen"): piece = 3
            elif(data.player1[i][0] == "Rook"): piece = 4
            elif(data.player1[i][0] == "Bishop"): piece = 5


            
            for j in range(len(posMoves)):
                if(outOfCheck(data, posMoves[j][0], posMoves[j][1], data.player1[i])):
                    if(posMoves[j] not in legalCheckMoves):
                        legalCheckMoves.append(posMoves[j])
            if(piece != None):
                modifyMoves(data, legalCheckMoves, i, piece)

            legalCheckMoves = []


    if(data.player2[4][5] == True):
        legalCheckMoves = []
        for i in range(len(data.player2)):
            posMoves = getMoves(data, data.player2[i][0], data.player2[i][1], data.player2[i][2])
            if(data.player2[i][0] == 'Pawn'):
                posMoves = []
                pawnMoves = [[1,0],[2,0]]
                for x in range(len(pawnMoves)):
                    posMoves.append([data.player2[i][1] - pawnMoves[x][0], data.player2[i][2] + pawnMoves[x][1]])

            if(data.player2[i][0] == "Knight"): piece = 0
            elif(data.player2[i][0] == "Pawn"): piece = 1
            elif(data.player2[i][0] == "King"): piece = 2
            elif(data.player2[i][0] == "Queen"): piece = 3
            elif(data.player2[i][0] == "Rook"): piece = 4
            elif(data.player2[i][0] == "Bishop"): piece = 5
            else: piece = None


            
            if(piece != None):
                for j in range(len(posMoves)):
                    if(outOfCheck(data, posMoves[j][0], posMoves[j][1], data.player2[i])):
                        if(posMoves[j] not in legalCheckMoves):
                            legalCheckMoves.append(posMoves[j])
            modifyMoves(data, legalCheckMoves, i, piece)

            legalCheckMoves = []


def outOfCheck(data, row, col, curP):
    if(data.player1[4][5] == True):
        holdR = curP[1]
        holdC = curP[2]

        curP[1] = row
        curP[2] = col
        if(inCheck(data.player1[4][1], data.player1[4][2], 1, data) == False and ([curP[1],curP[2]] != [data.player1[4][1],data.player1[4][2]]) or ([curP[1],curP[2]] == [data.player2[data.prevIndex1][1],data.player2[data.prevIndex1][2]]) and curP[0] != "Pawn"):
            curP[1] = holdR
            curP[2] = holdC
            return True

        else:
            curP[1] = holdR
            curP[2] = holdC
            return False

    if(data.player2[4][5] == True):
        holdR = curP[1]
        holdC = curP[2]

        curP[1] = row
        curP[2] = col
        if(inCheck(data.player2[4][1], data.player2[4][2], 2, data) == False and ([curP[1],curP[2]] != [data.player2[4][1],data.player2[4][2]]) or ([curP[1],curP[2]] == [data.player1[data.prevIndex2][1],data.player1[data.prevIndex2][2]] and curP[0] != "Pawn")):
            curP[1] = holdR
            curP[2] = holdC
            return True

        else:
            curP[1] = holdR
            curP[2] = holdC
            return False



def intoCheck(data,row, col, curP):
    #intoCheckDef
    if(data.currentPlayer == 1):
        if(data.player1[4][5] == False):
            holdR = curP[1]
            holdC = curP[2]

            curP[1] = row
            curP[2] = col
            if(inCheck(data.player1[4][1], data.player1[4][2], 1, data) == True and ([curP[1],curP[2]] != [data.player1[4][1],data.player1[4][2]])):
                curP[1] = holdR
                curP[2] = holdC
                return True
                #THIS MEANS YOUR THIS MOVE PUT THE KING IN CHECK

            else:
                curP[1] = holdR
                curP[2] = holdC
                return False
                #THE MOVE DIDN'T BUT THE KING IN CHECK

    if(data.currentPlayer == 2):
        if(data.player2[4][5] == False):
            holdR = curP[1]
            holdC = curP[2]

            curP[1] = row
            curP[2] = col

            if(inCheck(data.player2[4][1], data.player2[4][2], 2, data) == True and ([curP[1],curP[2]] != [data.player2[4][1],data.player2[4][2]]) and [curP[1],curP[2]] != data.putInCheck2):
                curP[1] = holdR
                curP[2] = holdC
                return True
                #THIS MEANS YOUR THIS MOVE PUT THE KING IN CHECK

            else:
                curP[1] = holdR
                curP[2] = holdC
                return False
                #THE MOVE DIDN'T BUT THE KING IN CHECK



def modifyMoves(data, moves, pieceNum, pType):

    #data.acceptablePieces = []
    data.p1DefensiveMoves = []
    data.p2DefensiveMoves = []

    #THIS IS WHERE I NEED TO FIX THINGS
    if(data.player1[4][5] == True):
        if(pType != None):
            tempMoves = data.moves[pType] 

            if(data.player1[pieceNum][0] == 'Pawn'):
                data.p1DefensiveMoves =  pawnsOutOfCheck(data,data.player1[pieceNum][1],data.player1[pieceNum][2],data.player1[pieceNum])
                if(pieceNum not in data.acceptablePieces):
                    data.acceptablePieces.append(pieceNum)

            elif(data.player1[pieceNum][0] != "Bishop" and data.player1[pieceNum][0] != "Queen" and data.player1[pieceNum][0] != "Rook"):
                for i in range(len(moves)):
                    for j in range(len(tempMoves)):   
                        if(([data.player1[pieceNum][1]+tempMoves[j][0], data.player1[pieceNum][2]+tempMoves[j][1]] in moves) or ([data.player1[pieceNum][1]+tempMoves[j][0], data.player1[pieceNum][2]+tempMoves[j][1]] == [data.player2[data.prevIndex1][1],data.player2[data.prevIndex1][2]])):
                            if(pieceNum not in data.acceptablePieces and ([data.player1[pieceNum][1]+tempMoves[j][0], data.player1[pieceNum][2]+tempMoves[j][1]] in data.p1DefensiveMoves)):
                                    data.acceptablePieces.append(pieceNum)
                            if([data.player1[pieceNum][1]+tempMoves[j][0], data.player1[pieceNum][2]+tempMoves[j][1]] not in data.p1DefensiveMoves):
                                data.p1DefensiveMoves.append([data.player1[pieceNum][1]+tempMoves[j][0], data.player1[pieceNum][2]+tempMoves[j][1]])
                

            else:
                for i in range(len(moves)):
                    for j in range(len(tempMoves)):
                        for k in range(len(tempMoves[j])): 
                            if([data.player1[pieceNum][1]+tempMoves[j][k][0], data.player1[pieceNum][2]+tempMoves[j][k][1]] in moves or ([data.player1[pieceNum][1]+tempMoves[j][k][0], data.player1[pieceNum][2]+tempMoves[j][k][1]] == [data.player2[data.prevIndex1][1],data.player2[data.prevIndex1][2]])):
                                if(pieceNum not in data.acceptablePieces and ([data.player1[pieceNum][1]+tempMoves[j][k][0], data.player1[pieceNum][2]+tempMoves[j][k][1]] in data.p1DefensiveMoves)):
                                    data.acceptablePieces.append(pieceNum)
                                if([[data.player1[pieceNum][1]+tempMoves[j][k][0], data.player1[pieceNum][2]+tempMoves[j][k][1]]] not in data.p1DefensiveMoves):
                                    data.p1DefensiveMoves.append([[data.player1[pieceNum][1]+tempMoves[j][k][0], data.player1[pieceNum][2]+tempMoves[j][k][1]]])
                                    if(pieceNum not in data.acceptablePieces):
                                        data.acceptablePieces.append(pieceNum)
                                    
                
            inCheckMoves(data,pieceNum, pType)
            if(data.moveList != []):
                for z in range(len(data.moveList)):
                    for a in range(len(data.moveList)):
                        if(data.moveList[a] not in data.checkMoveList):
                            data.checkMoveList.append(data.moveList[z])




##########################################
##########################################
##########################################
##########################################
#PLAYER 2
##########################################
##########################################
##########################################
##########################################
    
    if(data.player2[4][5] == True):
        if(pType == None): return
        tempMoves = data.moves[pType] 
        if(data.player2[pieceNum][0] == 'Pawn'):
            data.p2DefensiveMoves =  pawnsOutOfCheck(data,data.player2[pieceNum][1],data.player2[pieceNum][2],data.player2[pieceNum])
            if(pieceNum not in data.acceptablePieces):
                data.acceptablePieces.append(pieceNum)

        elif(data.player2[pieceNum][0] != "Bishop" and data.player2[pieceNum][0] != "Queen" and data.player2[pieceNum][0] != "Rook"):
            for i in range(len(moves)):
                for j in range(len(tempMoves)):   
                    if(([data.player2[pieceNum][1]+tempMoves[j][0], data.player2[pieceNum][2]+tempMoves[j][1]] in moves) or ([data.player2[pieceNum][1]+tempMoves[j][0], data.player2[pieceNum][2]+tempMoves[j][1]] == [data.player1[data.prevIndex2][1],data.player1[data.prevIndex2][2]])):
                        if(pieceNum not in data.acceptablePieces and ([data.player2[pieceNum][1]+tempMoves[j][0], data.player2[pieceNum][2]+tempMoves[j][1]] in data.p2DefensiveMoves)):
                            data.acceptablePieces.append(pieceNum)
                        if([data.player2[pieceNum][1]+tempMoves[j][0], data.player2[pieceNum][2]+tempMoves[j][1]] not in data.p2DefensiveMoves):
                            data.p2DefensiveMoves.append([data.player2[pieceNum][1]+tempMoves[j][0], data.player2[pieceNum][2]+tempMoves[j][1]])
            

        else:
            for i in range(len(moves)):
                for j in range(len(tempMoves)):
                    for k in range(len(tempMoves[j])):    
                        if([data.player2[pieceNum][1]+tempMoves[j][k][0], data.player2[pieceNum][2]+tempMoves[j][k][1]] in moves or ([data.player2[pieceNum][1]+tempMoves[j][k][0], data.player2[pieceNum][2]+tempMoves[j][k][1]] == [data.player1[data.prevIndex2][1],data.player1[data.prevIndex2][2]])):
                            if(pieceNum not in data.acceptablePieces and ([data.player2[pieceNum][1]+tempMoves[j][k][0], data.player2[pieceNum][2]+tempMoves[j][k][1]] in data.p2DefensiveMoves)):
                                data.acceptablePieces.append(pieceNum)
                            if([[data.player2[pieceNum][1]+tempMoves[j][k][0], data.player2[pieceNum][2]+tempMoves[j][k][1]]] not in data.p2DefensiveMoves):
                                data.p2DefensiveMoves.append([[data.player2[pieceNum][1]+tempMoves[j][k][0], data.player2[pieceNum][2]+tempMoves[j][k][1]]])
                                if(pieceNum not in data.acceptablePieces):
                                    data.acceptablePieces.append(pieceNum)
                                
            
        inCheckMoves(data,pieceNum, pType)
        if(data.moveList != []):
            for z in range(len(data.moveList)):
                if(data.moveList[z] not in data.checkMoveList):
                    data.checkMoveList.append(data.moveList[z])




def inCheckMoves(data,pieceNum, pType):
    data.moveList = []
    row = data.selectedRow
    col = data.selectedCol
    tempR = row
    tempC = col
    lol = 0

    if(data.p1DefensiveMoves != []):
        for i in range(len(data.moves[pType])):
            if(data.player1[pieceNum][0] == "King"):
                data.moveList = checkKing(data)

            elif(data.player1[pieceNum][0] == 'Pawn'):
                data.moveList = pawnsOutOfCheck(data,data.player1[pieceNum][1],data.player1[pieceNum][2],data.player1[pieceNum])

            elif(data.player1[pieceNum][0] != "Bishop" and data.player1[pieceNum][0] != "Queen" and data.player1[pieceNum][0] != "Rook" and data.player1[pieceNum][0] != None):
                if([data.player1[pieceNum][1]+data.moves[pType][i][0],data.player1[pieceNum][2]+data.moves[pType][i][1]] in data.p1DefensiveMoves or ([data.player1[pieceNum][1]+data.moves[pType][i][0], data.player1[pieceNum][2]+data.moves[pType][i][1]] == [data.player2[data.prevIndex1][1],data.player2[data.prevIndex1][2]])):
                    data.moveList.append([data.player1[pieceNum][1]+data.moves[pType][i][0],data.player1[pieceNum][2]+data.moves[pType][i][1]])

            elif(data.player1[pieceNum][0] != None):
                for j in range(len(data.moves[pType][i])):
                    for k in range(len(data.player1)):
                        if(([data.player1[pieceNum][1]+data.moves[pType][i][j][0],data.player1[pieceNum][2]+data.moves[pType][i][j][1]] == [data.player1[k][1],data.player1[k][2]]) or ([data.player1[pieceNum][1]+data.moves[pType][i][j][0],data.player1[pieceNum][2]+data.moves[pType][i][j][1]] == [data.player2[k][1],data.player2[k][2]] and [data.player2[k][1],data.player2[k][2]] != [data.player2[data.prevIndex1][1],data.player2[data.prevIndex1][2]])):
                            lol += 1
                            break
                    if(lol > 0):
                        break
                    if([data.player1[pieceNum][1]+data.moves[pType][i][j][0],data.player1[pieceNum][2]+data.moves[pType][i][j][1]] in data.p1DefensiveMoves or ([data.player1[pieceNum][1]+data.moves[pType][i][j][0], data.player1[pieceNum][2]+data.moves[pType][i][j][1]] == [data.player2[data.prevIndex1][1],data.player2[data.prevIndex1][2]])):
                        data.moveList.append([data.player1[pieceNum][1]+data.moves[pType][i][j][0],data.player1[pieceNum][2]+data.moves[pType][i][j][1]])

                    
            row = tempR
            col = tempC

    ##############################
    #PLAYER 2
    ##############################

    if(data.p2DefensiveMoves != []):
        for i in range(len(data.moves[pType])):
            if(data.player2[pieceNum][0] == "King"):
                data.moveList = checkKing(data)

            elif(data.player2[pieceNum][0] == 'Pawn'):
                data.moveList = pawnsOutOfCheck(data,data.player2[pieceNum][1],data.player2[pieceNum][2],data.player2[pieceNum])

            elif(data.player2[pieceNum][0] != "Bishop" and data.player2[pieceNum][0] != "Queen" and data.player2[pieceNum][0] != "Rook" and data.player2[pieceNum][0] != None):
                if([data.player2[pieceNum][1]+data.moves[pType][i][0],data.player2[pieceNum][2]+data.moves[pType][i][1]] in data.p2DefensiveMoves or ([data.player2[pieceNum][1]+data.moves[pType][i][0], data.player2[pieceNum][2]+data.moves[pType][i][1]] == [data.player1[data.prevIndex2][1],data.player1[data.prevIndex2][2]])):
                    data.moveList.append([data.player2[pieceNum][1]+data.moves[pType][i][0],data.player2[pieceNum][2]+data.moves[pType][i][1]])

            elif(data.player2[pieceNum][0] != None):
                for j in range(len(data.moves[pType][i])):
                    for k in range(len(data.player1)):
                        if(([data.player2[pieceNum][1]+data.moves[pType][i][j][0],data.player2[pieceNum][2]+data.moves[pType][i][j][1]] == [data.player2[k][1],data.player2[k][2]]) or ([data.player2[pieceNum][1]+data.moves[pType][i][j][0],data.player2[pieceNum][2]+data.moves[pType][i][j][1]] == [data.player1[k][1],data.player1[k][2]] and [data.player1[k][1],data.player1[k][2]] != [data.player1[data.prevIndex2][1],data.player1[data.prevIndex2][2]])):
                            lol += 1
                            break
                    if(lol > 0):
                        break
                    if([data.player2[pieceNum][1]+data.moves[pType][i][j][0],data.player2[pieceNum][2]+data.moves[pType][i][j][1]] in data.p2DefensiveMoves or ([data.player2[pieceNum][1]+data.moves[pType][i][j][0], data.player2[pieceNum][2]+data.moves[pType][i][j][1]] == [data.player1[data.prevIndex2][1],data.player1[data.prevIndex2][2]])):
                        data.moveList.append([data.player2[pieceNum][1]+data.moves[pType][i][j][0],data.player2[pieceNum][2]+data.moves[pType][i][j][1]])
            row = tempR
            col = tempC


    return data.moveList



def pawnsOutOfCheck(data, pRow, pCol,curPawn):
    pawnMove = []
    if(data.currentPlayer == 1):
        row = data.player2[data.prevIndex1][1]
        col = data.player2[data.prevIndex1][2]

        if(pRow + 1 == row and pCol + 1 == col):
            pawnMove.append([pRow + 1,pCol+1])
        if(pRow + 1 == row and pCol - 1 == col):
            pawnMove.append([pRow + 1, pCol-1])
        if(outOfCheck(data,pRow+1,pCol, curPawn)):
            pawnMove.append([pRow + 1,pCol + 0])
        if(outOfCheck(data,pRow+2,pCol, curPawn)):
            pawnMove.append([pRow + 2,pCol + 0])


    if(data.currentPlayer == 2):
        row = data.player1[data.prevIndex2][1]
        col = data.player1[data.prevIndex2][2]

        if(pRow - 1 == row and pCol + 1 == col):
            pawnMove.append([pRow - 1,pCol + 1])
        if(pRow - 1 == row and pCol - 1 == col):
            pawnMove.append([pRow-1,pCol-1])
        if(outOfCheck(data,pRow-1,pCol, curPawn)):
            pawnMove.append([pRow-1,pCol+0])
        if(outOfCheck(data,pRow-2,pCol, curPawn)):
            pawnMove.append([pRow-2,pCol+0])

    return pawnMove


####################################
# PvAIMenu mode
####################################




def PvAIMenuMousePressed(event, data):
    if((event.x >= data.width/2-125 and event.x <= data.width/2+125)):
        if(event.y >= data.height/2-100 and event.y <= data.height/2-50):
            data.mode = 'PvAIE'
        elif(event.y >= data.height/2 + data.height/6-100 and event.y <= data.height/2-50 + data.height/6):
            data.mode = 'PvAIH'
        
    pass

def PvAIMenuKeyPressed(event, data):
    if(event.keysym == "r"):
        init(data)

def PvAIMenuTimerFired(data):
    pass
        


def PvAIMenuRedrawAll(canvas, data):
    #BACKGROUND
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")

    #TITLE
    canvas.create_text(data.width/2, data.height/5,
                       text="L E V E L      D I F F I C U L T Y", font="Arial 30 bold", fill = "white")

    #EASY MODE
    canvas.create_rectangle(data.width/2-125, data.height/2-100,data.width/2+125, 
        data.height/2-50, fill = "white")
    canvas.create_text(data.width/2, data.height/2-75, 
        text='E A S Y', font="Arial 20 bold", width = 300)

    #HARD MODE
    canvas.create_rectangle(data.width/2-125, data.height/2 + data.height/6-100,
        data.width/2+125, data.height/2-50 + data.height/6, fill = "white")
    canvas.create_text(data.width/2, data.height/2-75+data.height/6, 
        text='H A R D', font="Arial 20 bold", width = 300)
    





####################################
# PvAIE mode
####################################

def PvAIEMousePressed(event, data):
    if(data.currentPlayer == 1):
        getRowColAI1E(event.x, event.y, data)
        movePiece(data)
        data.lol = 0
        highlightMoves(data)
    

def PvAIEKeyPressed(event, data):
    if(event.keysym == "r"):
        init(data)

def PvAIETimerFired(data):
    checkKing(data)
    changePawn(data)
    if(data.currentPlayer == 2 and data.lol < 1):
        getRowColAI2E(data)
        movePieceAI(data)
        


def PvAIERedrawAll(canvas, data):
    drawBoard(canvas, data)
    drawPieces(canvas,data)
    if(data.player1[4][6] == True):
        data.mode = 'checkMate'
        canvas.create_text(data.width/2, data.height/2, text = 'PLAYER 2 WINS')
    if(data.player2[4][6] == True):
        data.mode = 'checkMate'
        canvas.create_text(data.width/2, data.height/2, text = 'PLAYER 1 WINS')
    







####################################
# PvAI Functionss
####################################


def getRowColAI1E(x,y,data):
    new = False
    data.selectedCol = x//data.cellSize
    data.selectedRow = y//data.cellSize

    for i in range(len(data.player1)):
        if(data.player1[i][1] == data.selectedRow and 
            data.player1[i][2] == data.selectedCol and 
            data.currentPlayer == 1 and data.player1[i][0] != None):
                data.highlightColor = 'pink'
                data.currentPiece = data.player1[i][0]
                data.curIndex = i
                new = True

    if(new == False):
        data.highlightColor = None
        data.currentPiece = None


def getRowColAI2E(data):
    new = False
    randPiece = random.randint(0,len(data.player2)-1)


    data.selectedRow = data.player2[randPiece][1]
    data.selectedCol = data.player2[randPiece][2]
    data.highlightColor = 'orange'
    data.currentPiece = data.player2[randPiece][0]
    data.curIndex = randPiece
    new = True


    if(new == False):
        data.highlightColor = None
        data.currentPiece = None
    data.lol += 1 




def movePieceAI(data):
    previousRow = data.selectedRow
    previousCol = data.selectedCol
    move = []
    allPosibilities = []
    points = []
    allPoints = []


    #RANDOM MOVE GENERATION
    if(move == []):
        while(move == []):
            piece = random.randint(0,len(data.player2)-1)
            data.currentPiece = data.player2[piece][0]
            data.selectedRow = data.player2[piece][1]
            data.selectedCol = data.player2[piece][2]
            data.curIndex = piece
            highlightMovesAIE(data)
            move = data.moveList
        randMove = random.randint(0, len(move)-1)

        mRow = move[randMove][0]
        mCol = move[randMove][1]



    data.prevIndex1 = data.curIndex
    data.player2[data.curIndex][1] = mRow 
    data.player2[data.curIndex][2] = mCol 
    data.currentPlayer = 1

    if(data.curIndex == 4):
        if(data.player2[data.curIndex][2] == 2 and data.player2[data.curIndex][1] == 7 and data.player2[4][4] == False):
            data.player2[0][2] = 3
            data.player2[0][1] = 7
        elif(data.player2[data.curIndex][2] == 6 and data.player2[data.curIndex][1] == 7 and data.player2[4][4] == False):
            data.player2[7][2] = 5
            data.player2[0][1] = 7

    for k in range(len(data.player1)):
        if(data.player1[k][1] == data.player2[data.curIndex][1] and 
            data.player1[k][2] == data.player2[data.curIndex][2]):
            data.player1[k][0] = None
            data.player1[k][1] = -1
            data.player1[k][2] = -1

    if(data.moveList != []):
        data.moveList = []
    

    data.tempR2 = data.player2[4][1]
    data.tempC2 = data.player2[4][2]

    data.player1[4][5] = inCheck(data.player1[4][1], data.player1[4][2],1,data,1)
    data.player2[4][5] = inCheck(data.player2[4][1], data.player2[4][2],2,data,1)

    if(data.player1[4][5] == True or data.player2[4][5] == True):
        findMoves(data)
        data.moves = data.temporaryMOVEHOLDER



def highlightMovesAIE(data):
    if(data.player2[4][5] == True):
        s = set()
        for x in range(len(data.checkMoveList)):
            s.add(tuple(data.checkMoveList[x]))
            #get rid of duplicates

        data.checkMoveList = list(s)
        #change set back to list
        for y in range(len(data.checkMoveList)):
            data.checkMoveList[y] = list(data.checkMoveList[y])
            #change elements back to lists from tuples
        data.moveList = []

        
        if(data.currentPiece != None):
            if(data.checkMoveList != [] or data.possiblePos != []):
                if(data.currentPiece == "Knight"): data.piece = 0
                elif(data.currentPiece == "Pawn"): data.piece = 1
                elif(data.currentPiece == "King"): data.piece = 2
                elif(data.currentPiece == "Queen"): data.piece = 3
                elif(data.currentPiece == "Rook"): data.piece = 4
                elif(data.currentPiece == "Bishop"): data.piece = 5
                
                for r in range(len(data.possiblePos)):
                    if(data.possiblePos[r] in data.checkMoveList and (data.possiblePos[r] != [data.player1[data.prevIndex2][1],data.player1[data.prevIndex2][2]])):
                        data.checkMoveList.remove(data.possiblePos[r])

                for p in data.acceptablePieces:
                    if(data.curIndex == p):
                        if(data.player2[p][0] == 'King'):
                            data.moveList = data.possiblePos

                        elif(data.player2[p][0] == 'Pawn'):
                            for m in range(len(data.moves[data.piece])):
                                if([data.player2[p][1] - 1, data.player2[p][2] + 1] in data.checkMoveList):
                                    data.moveList.append([data.player2[p][1] - 1, data.player2[p][2] + 1])
                                if([data.player2[p][1] - 1, data.player2[p][2] - 1] in data.checkMoveList):
                                    data.moveList.append([data.player2[p][1] - 1, data.player2[p][2] - 1])


                        elif(data.player2[p][0] != "Bishop" and data.player2[p][0] != "Queen" and data.player2[p][0] != "Rook"):
                            for m in range(len(data.moves[data.piece])):
                                if([data.player2[p][1] + data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1]] in data.checkMoveList):
                                    if(isLegalMove(data.player2[p][1] + data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1], data)):
                                        data.moveList.append([data.player2[p][1] + data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1]])
                        else:
                            for m in range(len(data.moves[data.piece])):
                                for n in range(len(data.moves[data.piece][m])):
                                    if([data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1]] in data.checkMoveList):
                                        if(isLegalMove(data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1], data)):
                                            if([data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1]] in getMoves(data,data.player2[p][0],data.player2[p][1],data.player2[p][2])):
                                                data.moveList.append([data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1]])
                            


        if(data.possiblePos == [] and data.checkMoveList == []):
            data.player2[4][6] = True


    #IF NEITHER KING IS IN CHECK DO THIS
    else:
        data.acceptablePieces = [e for e in range(len(data.player1))]
        data.p1DefensiveMoves = []
        data.p2DefensiveMoves = []
        if(data.currentPiece == None): 
            data.moveList = []
            return
        elif(data.currentPiece == "Knight"): data.piece = 0
        elif(data.currentPiece == "Pawn"): data.piece = 1
        elif(data.currentPiece == "King"): data.piece = 2
        elif(data.currentPiece == "Queen"): data.piece = 3
        elif(data.currentPiece == "Rook"): data.piece = 4
        elif(data.currentPiece == "Bishop"): data.piece = 5
        

        l = 0 #FOR THE KNIGHT AND KINGS MOVES
        setL = 0 #FOR BISHOP, ROOK, QUEEN
        moveL = 0 #FOR BISHOP, ROOK, QUEEN

        #moves for Bishop, Rook, Queen
        if(data.currentPiece == 'Bishop' or data.currentPiece == 'Rook' or 
            data.currentPiece == 'Queen'):
            while setL < len(data.moves[data.piece]):
                b = False
                while moveL < len(data.moves[data.piece][setL]):
                    mRow = data.selectedRow+data.moves[data.piece][setL][moveL][0]
                    mCol = data.selectedCol+data.moves[data.piece][setL][moveL][1]
                    if(isLegalMove(mRow, mCol, data)):
                        data.moveList.append([mRow, mCol])

                        #checks if player1 hits player2's piece
                        if(data.currentPlayer == 1):
                            for x in range(len(data.player2)):
                                if(data.player2[x][1] == mRow and 
                                    data.player2[x][2] == mCol and 
                                    data.player2[x][0] != None):
                                        b = True         

                        #checks if player2 hits player1s piece
                        else:
                            for y in range(len(data.player1)):
                                if(data.player1[y][1] == mRow and 
                                    data.player1[y][2] == mCol and 
                                    data.player1[y][0] != None):
                                        b = True   
                    #hit own piece
                    else:
                        setL += 0
                        moveL = 0
                        break

                    #hit other players piece
                    if(b == True):
                            setL += 1
                            moveL = 0                        
                            break
                    moveL += 1

                if(b != True):
                    setL += 1
                    moveL = 0


        #moves for Knights
        elif(data.currentPiece == 'Knight'):
            while l < len(data.moves[data.piece]):
                kRow = data.selectedRow+data.moves[data.piece][l][0]
                kCol = data.selectedCol+data.moves[data.piece][l][1]
                if(isLegalMove(kRow, kCol, data)):
                    data.moveList.append([kRow, kCol])
                l += 1

        #moves for Kings
        elif(data.currentPiece == 'King'):
            kingCastle(data)
            #possiblePos = []
            checkKing(data)
            data.possiblePos = checkKing(data)


            for i in range(len(data.possiblePos)):
                if(data.currentPlayer == 1):
                    if([data.possiblePos[i][0]-data.player1[4][1],data.possiblePos[i][1]-data.player1[4][2]] in data.moves[2]):
                        data.moveList.append([data.possiblePos[i][0],data.possiblePos[i][1]])

                else:
                    if([data.possiblePos[i][0]-data.player2[4][1],data.possiblePos[i][1]-data.player2[4][2]] in data.moves[2]):
                        data.moveList.append([data.possiblePos[i][0],data.possiblePos[i][1]])  
            

            #MAKES IT SO YOU CAN'T CASTLE THROUGH CHECK
            if(data.currentPlayer == 1):
                if([0,5] not in data.moveList):
                    if([0,6] in data.moveList):
                        data.moveList.remove([0,6])
                if([0,3] not in data.moveList):
                    if([0,2] in data.moveList):
                        data.moveList.remove([0,2])
            else:
                if([7,5] not in data.moveList):
                    if([7,6] in data.moveList):
                        data.moveList.remove([7,6])
                if([7,3] not in data.moveList):
                    if([7,2] in data.moveList):
                        data.moveList.remove([7,2])


        #PAWN MOVESET
        else:
            getPawnMoves(data)
            pawnL = []
            for m in data.moves[1]:
                if(data.currentPlayer == 1):
                    if(isLegalMove(data.selectedRow+m[0], data.selectedCol+m[1], data)):
                        data.moveList.append([data.selectedRow+m[0], data.selectedCol+m[1]])
                else:
                    if(isLegalMove(data.selectedRow-m[0], data.selectedCol+m[1], data)):
                        data.moveList.append([data.selectedRow-m[0], data.selectedCol+m[1]])


        #MAKES SURE YOU CANT MOVE A PIECE THAT TAKES YOU OUT OF CHECK
        hahList = []
        tracker = 0
        word = 0
        for z in range(len(data.moveList)):
            if(data.currentPlayer == 1):
                for o in range(len(data.moveList)):
                    if([data.moveList[z][0],data.moveList[z][1]] == data.putInCheck1):
                        word += 1

                if(intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player1[data.curIndex]) and word == 0):
                    if(data.curIndex in data.acceptablePieces):
                        data.acceptablePieces.remove(data.curIndex)

                if(not intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player1[data.curIndex]) or [data.moveList[z][0],data.moveList[z][1]] == data.putInCheck1):
                    hahList.append(data.moveList[z])
                    if(data.curIndex not in data.acceptablePieces):
                        data.acceptablePieces.append(data.curIndex)
                else:
                    tracker += 1

            elif(data.currentPlayer == 2):
                for o in range(len(data.moveList)):
                    if([data.moveList[z][0],data.moveList[z][1]] == data.putInCheck2):
                        word += 1

                if(intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player2[data.curIndex]) and word  == 0):
                    if(data.curIndex in data.acceptablePieces):
                        data.acceptablePieces.remove(data.curIndex)

                if(not intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player2[data.curIndex]) or [data.moveList[z][0],data.moveList[z][1]] == data.putInCheck2):
                    hahList.append(data.moveList[z])
                    if(data.curIndex not in data.acceptablePieces):
                        data.acceptablePieces.append(data.curIndex)
                else:
                    tracker += 1


            if(data.currentPlayer == 1 and tracker > 0):
                if(data.moveList[z] == data.putInCheck1):
                    hahList.append(data.moveList[z])

            elif(data.currentPlayer == 2 and tracker > 0):
                if(data.moveList[z] == data.putInCheck2):
                    hahList.append(data.moveList[z])


        if(hahList != [] and data.curIndex in data.acceptablePieces):
            data.moveList = hahList
        else:
            data.moveList = []













####################################
# PvAIH mode
####################################

def PvAIHMousePressed(event, data):
    if(data.currentPlayer == 1):
        getRowColAI1E(event.x, event.y, data)
        movePiece(data)
        data.lol = 0
        highlightMoves(data)
    
def PvAIHKeyPressed(event, data):
    if(event.keysym == "r"):
        init(data)

def PvAIHTimerFired(data):
    checkKing(data)
    changePawn(data)
    if(data.currentPlayer == 2 and data.lol < 1):
        getRowColAI2H(data)
        movePieceAIH(data)
        

def PvAIHRedrawAll(canvas, data):
    drawBoard(canvas, data)
    drawPieces(canvas,data)
    if(data.player1[4][6] == True):
        data.mode = 'checkMate'
        canvas.create_text(data.width/2, data.height/2, text = 'PLAYER 2 WINS')
    if(data.player2[4][6] == True):
        data.mode = 'checkMate'
        canvas.create_text(data.width/2, data.height/2, text = 'PLAYER 1 WINS')
    







####################################
# PvAI Functionss
####################################


def getRowColAI1H(x,y,data):
    new = False
    data.selectedCol = x//data.cellSize
    data.selectedRow = y//data.cellSize

    for i in range(len(data.player1)):
        if(data.player1[i][1] == data.selectedRow and 
            data.player1[i][2] == data.selectedCol and 
            data.currentPlayer == 1 and data.player1[i][0] != None):
                data.highlightColor = 'pink'
                data.currentPiece = data.player1[i][0]
                data.curIndex = i
                new = True

    if(new == False):
        data.highlightColor = None
        data.currentPiece = None


def getRowColAI2H(data):
    new = False
    randPiece = random.randint(0,len(data.player2)-1)


    data.selectedRow = data.player2[randPiece][1]
    data.selectedCol = data.player2[randPiece][2]
    data.highlightColor = 'orange'
    data.currentPiece = data.player2[randPiece][0]
    data.curIndex = randPiece
    new = True


    if(new == False):
        data.highlightColor = None
        data.currentPiece = None
    data.lol += 1 


def scorePiece(piece):
    if(piece == 'Pawn'):
        return 1
        
    elif(piece == 'Knight'):
        return 3
    
    elif(piece == 'Bishop'):
        return 3
    
    elif(piece == 'Rook'):
        return 5
    
    elif(piece == 'Queen'):
        return 9



#TAKES A PIECE,FINDS ALL ITS MOVES-->DETERMINES WHICH PIECES/WHERE CAN BE TAKEN
def canTake(data,piece):
    takes = []
    moves = getMoves(data, piece[0], piece[1], piece[2])
    for i in range(len(data.player1)):
        pieceD = data.player1[i]
        if([pieceD[1],pieceD[2]] in moves):
            takes.append([pieceD[0], [pieceD[1],pieceD[2]]])
    return takes
    #returns [pieceName, [PieceRow, PieceCol]]


#TAKES PIECE AND DETERMINES IF IT CAN BE TAKEN AT EACH MOVE
def canLose(data,piece):
    for i in range(len(data.player1)):
        #PIECEO IS A PIECE OF PLAYER 1 TO SEE IF PIECE (PLAYER2) CAN BE TAKEN
        pieceO = data.player1[i]
        moves = getMoves(data, data.player1[i][0], data.player1[i][1], data.player1[i][2])
        if([piece[1],piece[2]] in moves):
            return True
    return False





def movePieceAIH(data):
    previousRow = data.selectedRow
    previousCol = data.selectedCol
    #returh to AI
    move = []
    allPosibilities = []
    points = []
    allPoints = []


    #DEFENSIVE MOVEMENT
    if(move == []):
        loses = []
        points = []
        #creates a list of all players you can lose
        for i in range(len(data.player2)):
            if(canLose(data,data.player2[i])):
                loses.append((data.player2[i],i))
        #creates a list that scores every piece you can lose
        for j in range(len(loses)):
            if(loses[j][0] == 'Pawn'):
                points.append(1)
        
            elif(loses[j][0] == 'Knight'):
                points.append(3)
            
            elif(loses[j][0] == 'Bishop'):
                points.append(3)
            
            elif(loses[j][0] == 'Rook'):
                points.append(5)
            
            elif(loses[j][0] == 'Queen'):
                points.append(9)
        if(points != []):
            index = points.index(max(points))

            #the most valuable piece you can lose
            piece = loses[index][0]
            data.curIndex = loses[index][1]

            potentialMoves = getMoves(data,piece[0],piece[1],piece[2])
            holdRD = piece[1]
            holdCD = piece[2]
            for k in range(len(potentialMoves)):
                piece[1] = potentialMoves[k][0]
                piece[2] = potentialMoves[k][1]
                if(canLose(data, piece) == False):
                    move = [potentialMoves[k][0],potentialMoves[k][1]]
                    piece[1] = holdRD
                    piece[2] = holdCD
                    break  
        if(move != []):
            mRow = move[0]
            mCol = move[1]
            data.curIndex = r


    #makes better by adjusting points by using can lose if it can lose it add
    #draws orange box based off of selected row/col
    #OFFENSIVE MOVEMENT
    #PICKS THE PIECE TO MOVE AND MAKES SURE IT HAS A VALID MOVE TO USE
    if(move == []):
        maxScore = 0
        points = []
        for r in range(len(data.player2)):
            takes = canTake(data,data.player2[r])
            #list of [pieceName, [pieceRow, pieceCol]]
            for s in range(len(takes)):
                if(takes[s][0] == 'Pawn'):
                    points.append(1)
                    dummy = [None, takes[s][1][0],takes[s][1][1]]
                    if(data.player2[r][0] != None):
                        if(canLose(data,dummy)):
                            if(points != []):
                                points[-1] = points[-1]-scorePiece(data.player2[r][0])

            
                elif(takes[s][0] == 'Knight'):
                    points.append(3)
                    dummy = [None, takes[s][1][0],takes[s][1][1]]
                    if(data.player2[r][0] != None):
                        if(canLose(data,dummy)):
                            if(points != []):
                                points[-1] = points[-1]-scorePiece(data.player2[r][0])
                
                elif(takes[s][0] == 'Bishop'):
                    points.append(3)
                    dummy = [None, takes[s][1][0],takes[s][1][1]]
                    if(data.player2[r][0] != None):
                        if(canLose(data,dummy)):
                            if(points != []):
                                points[-1] = points[-1]-scorePiece(data.player2[r][0])
                
                elif(takes[s][0] == 'Rook'):
                    points.append(5)
                    dummy = [None, takes[s][1][0],takes[s][1][1]]
                    if(data.player2[r][0] != None):
                        if(canLose(data,dummy)):
                            if(points != []):
                                points[-1] = points[-1]-scorePiece(data.player2[r][0])
                
                elif(takes[s][0] == 'Queen'):
                    points.append(9)
                    dummy = [None, takes[s][1][0],takes[s][1][1]]
                    if(data.player2[r][0] != None):
                        if(canLose(data,dummy)):
                            if(points != []):
                                points[-1] = points[-1]-scorePiece(data.player2[r][0])
                
                if(points[-1] >= maxScore):
                    data.selectedRow = data.player2[r][1]
                    data.selectedCol = data.player2[r][2]
                    maxScore = points[-1]
                    move = takes[s][1]
                    pInd = r
        if(move != []):
            data.curIndex = pInd
            mRow = move[0]
            mCol = move[1]




    #RANDOM MOVE GENERATION
    if(move == []):
        while(move == []):
            piece = random.randint(0,len(data.player2)-1)
            data.currentPiece = data.player2[piece][0]
            data.selectedRow = data.player2[piece][1]
            data.selectedCol = data.player2[piece][2]
            data.curIndex = piece
            highlightMovesAIE(data)
            move = data.moveList
        randMove = random.randint(0, len(move)-1)

        mRow = move[randMove][0]
        mCol = move[randMove][1]



    data.prevIndex1 = data.curIndex
    data.player2[data.curIndex][1] = mRow 
    data.player2[data.curIndex][2] = mCol 
    data.currentPlayer = 1

    if(data.curIndex == 4):
        if(data.player2[data.curIndex][2] == 2 and data.player2[data.curIndex][1] == 7 and data.player2[4][4] == False):
            data.player2[0][2] = 3
            data.player2[0][1] = 7
        elif(data.player2[data.curIndex][2] == 6 and data.player2[data.curIndex][1] == 7 and data.player2[4][4] == False):
            data.player2[7][2] = 5
            data.player2[0][1] = 7

    for k in range(len(data.player1)):
        if(data.player1[k][1] == data.player2[data.curIndex][1] and 
            data.player1[k][2] == data.player2[data.curIndex][2]):
            data.player1[k][0] = None
            data.player1[k][1] = -1
            data.player1[k][2] = -1

    if(data.moveList != []):
        data.moveList = []
    

    data.tempR2 = data.player2[4][1]
    data.tempC2 = data.player2[4][2]

    data.player1[4][5] = inCheck(data.player1[4][1], data.player1[4][2],1,data,1)
    data.player2[4][5] = inCheck(data.player2[4][1], data.player2[4][2],2,data,1)

    if(data.player1[4][5] == True or data.player2[4][5] == True):
        findMoves(data)
        data.moves = data.temporaryMOVEHOLDER



def highlightMovesAIH(data):
    
    if(data.player2[4][5] == True):
        s = set()
        for x in range(len(data.checkMoveList)):
            s.add(tuple(data.checkMoveList[x]))
            #get rid of duplicates

        data.checkMoveList = list(s)
        #change set back to list
        for y in range(len(data.checkMoveList)):
            data.checkMoveList[y] = list(data.checkMoveList[y])
            #change elements back to lists from tuples
        data.moveList = []

        
        if(data.currentPiece != None):
            if(data.checkMoveList != [] or data.possiblePos != []):
                if(data.currentPiece == "Knight"): data.piece = 0
                elif(data.currentPiece == "Pawn"): data.piece = 1
                elif(data.currentPiece == "King"): data.piece = 2
                elif(data.currentPiece == "Queen"): data.piece = 3
                elif(data.currentPiece == "Rook"): data.piece = 4
                elif(data.currentPiece == "Bishop"): data.piece = 5
                
                for r in range(len(data.possiblePos)):
                    if(data.possiblePos[r] in data.checkMoveList and (data.possiblePos[r] != [data.player1[data.prevIndex2][1],data.player1[data.prevIndex2][2]])):
                        data.checkMoveList.remove(data.possiblePos[r])

                for p in data.acceptablePieces:
                    if(data.curIndex == p):
                        if(data.player2[p][0] == 'King'):
                            data.moveList = data.possiblePos

                        elif(data.player2[p][0] == 'Pawn'):
                            for m in range(len(data.moves[data.piece])):
                                if([data.player2[p][1] - 1, data.player2[p][2] + 1] in data.checkMoveList):
                                    data.moveList.append([data.player2[p][1] - 1, data.player2[p][2] + 1])
                                if([data.player2[p][1] - 1, data.player2[p][2] - 1] in data.checkMoveList):
                                    data.moveList.append([data.player2[p][1] - 1, data.player2[p][2] - 1])


                        elif(data.player2[p][0] != "Bishop" and data.player2[p][0] != "Queen" and data.player2[p][0] != "Rook"):
                            for m in range(len(data.moves[data.piece])):
                                if([data.player2[p][1] + data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1]] in data.checkMoveList):
                                    if(isLegalMove(data.player2[p][1] + data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1], data)):
                                        data.moveList.append([data.player2[p][1] + data.moves[data.piece][m][0], data.player2[p][2] + data.moves[data.piece][m][1]])
                        else:
                            for m in range(len(data.moves[data.piece])):
                                for n in range(len(data.moves[data.piece][m])):
                                    if([data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1]] in data.checkMoveList):
                                        if(isLegalMove(data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1], data)):
                                            if([data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1]] in getMoves(data,data.player2[p][0],data.player2[p][1],data.player2[p][2])):
                                                data.moveList.append([data.player2[p][1] + data.moves[data.piece][m][n][0], data.player2[p][2] + data.moves[data.piece][m][n][1]])
                            


        if(data.possiblePos == [] and data.checkMoveList == []):
            data.player2[4][6] = True


    #IF NEITHER KING IS IN CHECK DO THIS
    else:
        data.acceptablePieces = [e for e in range(len(data.player1))]
        data.p1DefensiveMoves = []
        data.p2DefensiveMoves = []
        if(data.currentPiece == None): 
            data.moveList = []
            return
        elif(data.currentPiece == "Knight"): data.piece = 0
        elif(data.currentPiece == "Pawn"): data.piece = 1
        elif(data.currentPiece == "King"): data.piece = 2
        elif(data.currentPiece == "Queen"): data.piece = 3
        elif(data.currentPiece == "Rook"): data.piece = 4
        elif(data.currentPiece == "Bishop"): data.piece = 5
        

        l = 0 #FOR THE KNIGHT AND KINGS MOVES
        setL = 0 #FOR BISHOP, ROOK, QUEEN
        moveL = 0 #FOR BISHOP, ROOK, QUEEN

        #moves for Bishop, Rook, Queen
        if(data.currentPiece == 'Bishop' or data.currentPiece == 'Rook' or 
            data.currentPiece == 'Queen'):
            while setL < len(data.moves[data.piece]):
                b = False
                while moveL < len(data.moves[data.piece][setL]):
                    mRow = data.selectedRow+data.moves[data.piece][setL][moveL][0]
                    mCol = data.selectedCol+data.moves[data.piece][setL][moveL][1]
                    if(isLegalMove(mRow, mCol, data)):
                        data.moveList.append([mRow, mCol])

                        #checks if player1 hits player2's piece
                        if(data.currentPlayer == 1):
                            for x in range(len(data.player2)):
                                if(data.player2[x][1] == mRow and 
                                    data.player2[x][2] == mCol and 
                                    data.player2[x][0] != None):
                                        b = True         

                        #checks if player2 hits player1s piece
                        else:
                            for y in range(len(data.player1)):
                                if(data.player1[y][1] == mRow and 
                                    data.player1[y][2] == mCol and 
                                    data.player1[y][0] != None):
                                        b = True   
                    #hit own piece
                    else:
                        setL += 0
                        moveL = 0
                        break

                    #hit other players piece
                    if(b == True):
                            setL += 1
                            moveL = 0                        
                            break
                    moveL += 1

                if(b != True):
                    setL += 1
                    moveL = 0


        #moves for Knights
        elif(data.currentPiece == 'Knight'):
            while l < len(data.moves[data.piece]):
                kRow = data.selectedRow+data.moves[data.piece][l][0]
                kCol = data.selectedCol+data.moves[data.piece][l][1]
                if(isLegalMove(kRow, kCol, data)):
                    data.moveList.append([kRow, kCol])
                l += 1

        #moves for Kings
        elif(data.currentPiece == 'King'):
            kingCastle(data)
            checkKing(data)
            data.possiblePos = checkKing(data)


            for i in range(len(data.possiblePos)):
                if(data.currentPlayer == 1):
                    if([data.possiblePos[i][0]-data.player1[4][1],data.possiblePos[i][1]-data.player1[4][2]] in data.moves[2]):
                        data.moveList.append([data.possiblePos[i][0],data.possiblePos[i][1]])

                else:
                    if([data.possiblePos[i][0]-data.player2[4][1],data.possiblePos[i][1]-data.player2[4][2]] in data.moves[2]):
                        data.moveList.append([data.possiblePos[i][0],data.possiblePos[i][1]])  

            

            #MAKES IT SO YOU CAN'T CASTLE THROUGH CHECK
            if(data.currentPlayer == 1):
                if([0,5] not in data.moveList):
                    if([0,6] in data.moveList):
                        data.moveList.remove([0,6])
                if([0,3] not in data.moveList):
                    if([0,2] in data.moveList):
                        data.moveList.remove([0,2])
            else:
                if([7,5] not in data.moveList):
                    if([7,6] in data.moveList):
                        data.moveList.remove([7,6])
                if([7,3] not in data.moveList):
                    if([7,2] in data.moveList):
                        data.moveList.remove([7,2])


        #PAWN MOVESET
        else:
            getPawnMoves(data)
            pawnL = []
            for m in data.moves[1]:
                if(data.currentPlayer == 1):
                    if(isLegalMove(data.selectedRow+m[0], data.selectedCol+m[1], data)):
                        data.moveList.append([data.selectedRow+m[0], data.selectedCol+m[1]])
                else:
                    if(isLegalMove(data.selectedRow-m[0], data.selectedCol+m[1], data)):
                        data.moveList.append([data.selectedRow-m[0], data.selectedCol+m[1]])


        #MAKES SURE YOU CANT MOVE A PIECE THAT TAKES YOU OUT OF CHECK
        hahList = []
        tracker = 0
        word = 0
        for z in range(len(data.moveList)):
            if(data.currentPlayer == 1):
                for o in range(len(data.moveList)):
                    if([data.moveList[z][0],data.moveList[z][1]] == data.putInCheck1):
                        word += 1

                if(intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player1[data.curIndex]) and word == 0):
                    if(data.curIndex in data.acceptablePieces):
                        data.acceptablePieces.remove(data.curIndex)

                if(not intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player1[data.curIndex]) or [data.moveList[z][0],data.moveList[z][1]] == data.putInCheck1):
                    hahList.append(data.moveList[z])
                    if(data.curIndex not in data.acceptablePieces):
                        data.acceptablePieces.append(data.curIndex)
                else:
                    tracker += 1

            elif(data.currentPlayer == 2):
                for o in range(len(data.moveList)):
                    if([data.moveList[z][0],data.moveList[z][1]] == data.putInCheck2):
                        word += 1

                if(intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player2[data.curIndex]) and word  == 0):
                    if(data.curIndex in data.acceptablePieces):
                        data.acceptablePieces.remove(data.curIndex)

                if(not intoCheck(data, data.moveList[z][0], data.moveList[z][1], data.player2[data.curIndex]) or [data.moveList[z][0],data.moveList[z][1]] == data.putInCheck2):
                    hahList.append(data.moveList[z])
                    if(data.curIndex not in data.acceptablePieces):
                        data.acceptablePieces.append(data.curIndex)
                else:
                    tracker += 1


            if(data.currentPlayer == 1 and tracker > 0):
                if(data.moveList[z] == data.putInCheck1):
                    hahList.append(data.moveList[z])

            elif(data.currentPlayer == 2 and tracker > 0):
                if(data.moveList[z] == data.putInCheck2):
                    hahList.append(data.moveList[z])


        if(hahList != [] and data.curIndex in data.acceptablePieces):
            data.moveList = hahList
        else:
            data.moveList = []









################################
#CHECKMATE MODE
################################
    
def mousePressedCheckMate(event, data):
    pass

def keyPressedCheckMate(event, data):
    if(event.keysym == 'r'):
        init(data)
    
def timerFiredCheckMate(data):
    pass

def redrawAllCheckMate(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill = 'black')
    if(data.player1[4][6] == True):
        canvas.create_text(data.width/2, data.height/2, 
            text = "CHECKMATE!      PLAYER 2 WINS", font="Arial 40 bold", fill = 'white')
    if(data.player2[4][6] == True):
        canvas.create_text(data.width/2, data.height/2, 
            text = "CHECKMATE!      PLAYER 1 WINS", font="Arial 40 bold", fill = 'white')
    canvas.create_text(data.width/2, 3*data.height/4, 
        text = "PRESS 'R' TO RETURN TO HOME SCREEN", font="Arial 20 bold", fill = 'white')







####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds

    
    # create the root and the canvas
    root = Tk()

    data.root = root
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(680, 680)