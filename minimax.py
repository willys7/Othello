import numpy as np
from prueba import *
from random import randint
from constants import *
from copy import deepcopy

def init(board, color, constants):
    depth = constants.Depth
    maxi = constants.Max
    mini = constants.Min
    return minimax(board, color, color,0,maxi,mini,constants)


def minimax (board, myColor, currentColor, depth, maxi, mini,constants):
    value = 0
    move = None
    if depth >= constants.Depth or 0 not in board:
        value = board.count(currentColor)
        return value, move
    #mi tablero y posiciones de mis fichas
    new_board, myPositions = parseBoard(board, currentColor)
    #movimientos validos
    valid_moves = []
    changes = []
    for position in myPositions:
        moves, changes = get_possible_moves(new_board, int(position[1]), int(position[0]), currentColor, changes)
        for move in moves:
            if move not in valid_moves:
                valid_moves.append(move)
    if len(valid_moves) <= 0:
        value = board.count(currentColor)
        move = None
        return value, move
    #get all possible states from legal moves
    newBoards = []
    for change in changes:
        nBoard, va = applyMoves(deepcopy(new_board), change, currentColor)
        nextBoard = {'next':None, 'move':None}
        nextBoard['next'] = nBoard
        nextBoard['move'] = va[-1]
        newBoards.append(nextBoard)
    
    nextColor = 0
    if currentColor == constants.Black:
        nextColor = constants.White
    else:
        nextColor = constants.Black

    #maximize 
    if myColor == currentColor:
        a, b = maxValue(newBoards, myColor, nextColor, depth, maxi, mini,constants)
        return a,b
    else:
         a, b = minValue(newBoards, myColor, nextColor, depth, maxi, mini, constants)
         return a,b

def maxValue(newBoards, myColor, currentColor, depth, maxi, mini, constants):
    v = float('-Inf')
    move = None
    for board in newBoards:
        nValue,move = minimax(primateBoard(deepcopy(board['next'])), myColor, currentColor, depth+1, maxi, mini, constants)
        v = max(v, nValue)
        maxi = max(maxi,v)
        if mini <= maxi:
            return v, board['move']
    finl = newBoards[0]
    move = finl['move']
    return v, move

def minValue(newBoards, myColor, currentColor, depth, maxi, mini, constants):
    v = float('Inf')
    move = None
    for board in newBoards:
        nValue,move = minimax(primateBoard(deepcopy(board['next'])), myColor, currentColor, depth+1, maxi, mini, constants)
        v = min(v, nValue)
        mini = min(mini, v)
        if mini <= maxi:
            return v, board['move']
    finl = newBoards[0]
    move = finl['move']
    return v, move

def applyMoves(board, values, color):
    for change in values:
        board[change[0]][change[1]] = color
    return board,values

def primateBoard(board):
    nB = []
    for valu in board:
        for va in valu:
            nB.append(va)
    return nB