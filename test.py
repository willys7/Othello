import socketIO_client
from random import randint
from prueba import *
from minimax import *
from constants import *

#s = socketIO_client.SocketIO('192.168.1.111', 3000)
s = socketIO_client.SocketIO('localhost', 3000)
s.connect()
constants = None
s.emit('signin', {'user_name': "Edwin Chota", 'tournament_id': 12, 'user_role': 'player'})

def onok():
    print 'exito en el signin'

def elready(data):
    tiro = 0
    valid_moves = []
    test = []
    board = data["board"]
    color = data["player_turn_id"]
    constants = Constants(4)
    constants.setColor(color)
    valu, test = init(board, color, constants)
    test2 = test
    tiro = test[1] +(8*test[0])
    print tiro
    s.emit('play', {'tournament_id': 12, 'player_turn_id': data['player_turn_id'], 'game_id': data['game_id'], 'movement': tiro})
    

def elfinish(data):
    s.emit('player_ready', {'tournament_id': 12, 'player_turn_id': data['player_turn_id'], 'game_id': data['game_id']})
    print data
    print 'terminado'

s.on('ok_signin', onok)
s.on('ready', elready)
s.on('finish', elfinish)
s.wait()

