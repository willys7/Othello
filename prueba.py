import numpy as np
def get_possible_moves(board, row, column, color, change):
    moves = []

    if color == 1:
        other = 2
    else:
        other = 1

    if row < 0 or row > 7 or column < 0 or column > 7:
        return moves

    # north
    i = row - 1
    temp = []
    if i >= 0 and board[i][column] == other:
        temp.append((i, column))
        i = i - 1
        while i >= 0 and board[i][column] == other:
            temp.append((i, column))
            i = i - 1
        if i >= 0 and board[i][column] == 0:
            temp.append((i, column))
            if [(i, column)] not in moves:
                moves = moves + [(i, column)]
                change = mergeChanges(change, temp)

    # northeast
    i = row - 1
    j = column + 1
    temp = []
    if i >= 0 and j < 8 and board[i][j] == other:
        temp.append((i, j))
        i = i - 1
        j = j + 1
        
        while i >= 0 and j < 8 and board[i][j] == other:
            temp.append((i, j))
            i = i - 1
            j = j + 1
            
        if i >= 0 and j < 8 and board[i][j] == 0:
            temp.append((i, j))
            if [(i, j)] not in moves:
                moves = moves + [(i, j)]
                change = mergeChanges(change, temp)

    # east
    j = column + 1
    temp = []
    if j < 8 and board[row][j] == other:
        temp.append((row, j))
        j = j + 1
        
        while j < 8 and board[row][j] == other:
            temp.append((row, j))
            j = j + 1
            
        if j < 8 and board[row][j] == 0:
            temp.append((row, j))
            if [(row, j)] not in moves:
                moves = moves + [(row, j)]
                change = mergeChanges(change, temp)

    # southeast
    i = row + 1
    j = column + 1
    temp = []
    if i < 8 and j < 8 and board[i][j] == other:
        temp.append((i, j))
        i = i + 1
        j = j + 1
        
        while i < 8 and j < 8 and board[i][j] == other:
            temp.append((i, j))
            i = i + 1
            j = j + 1
            
        if i < 8 and j < 8 and board[i][j] == 0:
            temp.append((i, j))
            if [(i, j)] not in moves:
                moves = moves + [(i, j)]
                change = mergeChanges(change, temp)

    # south
    i = row + 1
    temp = []
    if i < 8 and board[i][column] == other:
        temp.append((i, column))
        i = i + 1
        
        while i < 8 and board[i][column] == other:
            temp.append((i, column))
            i = i + 1
            
        if i < 8 and board[i][column] == 0:
            temp.append((i, column))
            if [(i, column)] not in moves:
                moves = moves + [(i, column)]
                change = mergeChanges(change, temp)

    # southwest
    i = row + 1
    j = column - 1
    temp = []
    if i < 8 and j >= 0 and board[i][j] == other:
        temp.append((i, j))
        i = i + 1
        j = j - 1
        
        while i < 8 and j >= 0 and board[i][j] == other:
            temp.append((i, j))
            i = i + 1
            j = j - 1
            
        if i < 8 and j >= 0 and board[i][j] == 0:
            temp.append((i, j))
            if [(i, j)] not in moves:
                moves = moves + [(i, j)]
                change = mergeChanges(change, temp)

    # west
    j = column - 1
    temp = []
    if j >= 0 and board[row][j] == other:
        temp.append((row, j))
        j = j - 1
        
        while j >= 0 and board[row][j] == other:
            temp.append((row, j))
            j = j - 1
            
        if j >= 0 and board[row][j] == 0:
            temp.append((row, j))
            if [(row, j)] not in moves:
                moves = moves + [(row, j)]
                change = mergeChanges(change, temp)

    # northwest
    i = row - 1
    j = column - 1
    temp = []
    if i >= 0 and j >= 0 and board[i][j] == other:
        temp.append((i, j))
        i = i - 1
        j = j - 1
        
        while i >= 0 and j >= 0 and board[i][j] == other:
            temp.append((i, j))
            i = i - 1
            j = j - 1
            
        if i >= 0 and j >= 0 and board[i][j] == 0:
            temp.append((i, j))
            if [(i, j)] not in moves:
                moves = moves + [(i, j)]
                change = mergeChanges(change, temp)

    return moves, change

def parseBoard(board, color):
    new_board = np.zeros((8, 8), dtype=np.integer)
    positions = []
    cont_x = 0
    cont_y = 0
    cont = 0
    for x in range(0,64):
        if cont_x < 8:
            new_board[cont_y][cont_x] = board[x]
            if board[x] == color:
                positions = positions + [(cont_x, cont_y)]
            cont_x = cont_x + 1
        else:
            cont_x = 0
            cont_y = cont_y + 1
            new_board[cont_y][cont_x] = board[x]
            if board[x] == color:
                positions = positions + [(cont_x, cont_y)]
            cont_x = cont_x + 1

    return new_board, positions
                
def mergeChanges(changes, newChange):
    for change in changes:
        last = change.pop(-1)
        last2 = newChange.pop(-1)
        if last == last2:
            for temp in newChange:
                change.append(temp)
            change.append(last)
            return changes
        else:
            change.append(last)
            newChange.append(last2)
    changes.append(newChange)
    return changes

