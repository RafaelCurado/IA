from common import *
from tree_search import SearchDomain

class RushHour(SearchDomain):
    def __init__(self, map):
        self.map = map

    def actions(self, state):
        action_list = []
        pieces = []

        #print(self.map.coordinates)

        for x in self.map.coordinates:
            if (x[2] != 'x'):
                pieces.append(x[2]) 

        pieces = list(set(pieces))
        #print(pieces)
        
        for piece in pieces:
            orientation = get_car_orientation(state, piece)
            piece_coords: list[Coordinates] = state.piece_coordinates(piece)
            
            if orientation == 'h': 
                extremo_esquerda = piece_coords[0]
                extremo_direita = piece_coords[-1]
                try:
                    extremo_esquerda.x = extremo_esquerda.x - 1
                    a_esquerda = state.get(extremo_esquerda)
                    if a_esquerda == 'o' and extremo_esquerda.x>=0 :
                        action_list.append((piece,'a'))
                except:
                    pass
                try:
                    extremo_direita.x = extremo_direita.x + 1
                    a_direita = state.get(extremo_direita)
                    if a_direita == 'o' and extremo_direita.x < 6:
                        action_list.append((piece,'d'))
                except:
                    pass
            else:
                extremo_cima = piece_coords[0]
                extremo_baixo = piece_coords[-1]
                try:
                    extremo_cima.y = extremo_cima.y - 1
                    a_cima = state.get(extremo_cima)
                    if a_cima == 'o' and extremo_cima.y >= 0:
                        action_list.append((piece,'w'))
                except:
                    pass
                try:
                    extremo_baixo.y = extremo_baixo.y + 1
                    a_baixo = state.get(extremo_baixo)
                    if a_baixo == 'o' and extremo_baixo.y < 6:
                        action_list.append((piece,'s'))
                except:
                    pass
            
        return action_list

    def result(self, state, action):    # deve retornar uma action ou todas as actions()
        newstate = state
        piece = action[0]
        direction = action[1]
        if direction == 'w':
            direction_coord = Coordinates(0,1)
        if direction == 'a':
            direction_coord = Coordinates(-1,0)
        if direction == 's':
            direction_coord = Coordinates(0,-1)
        if direction == 'd':
            direction_coord = Coordinates(1,0)
        newstate.move(piece,direction_coord)
        return newstate
        
    def cost(self):
        return 1

    def heuristic(self):
        pass

    def satisfies(self, state):
        return state.test_win()
        
    

def get_car_orientation(map: Map, piece: str):
        coords = map.piece_coordinates(piece)
        print(coords)
        print(map)
        if coords[0].y == coords[1].y:
            return "h"
        return "v"


