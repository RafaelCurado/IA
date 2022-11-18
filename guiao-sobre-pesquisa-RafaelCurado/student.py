"""Example client."""
import asyncio
import getpass
import json
import os

# Next 4 lines are not needed for AI agents, please remove them from your code!
import pygame
import websockets

# mine imports
from search import *
from common import *
from tree_search import *

pygame.init()
program_icon = pygame.image.load("data/icon2.png")
pygame.display.set_icon(program_icon)


async def agent_loop(server_address="localhost:8000", agent_name="103199"):
    """Example client loop."""
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))

        # Next 3 lines are not needed for AI agent
        SCREEN = pygame.display.set_mode((299, 123))
        SPRITES = pygame.image.load("data/pad.png").convert_alpha()
        SCREEN.blit(SPRITES, (0, 0))

        goal = Coordinates(5,2) # always the same goal
        initial_lvl1 = Map("01 ooooooooooooAAoooooooooooooooooooooo 5")

        while True:
            try:
                state = json.loads(
                    await websocket.recv()
                )  # receive game update, this must be called timely or your game will get out of sync with the server

                key = ""

                map = Map(state.get("grid"))
                cursor = state.get("cursor")
                sel = state.get("selected")

                print(map)
                print("cabouse")
                domain = RushHour(map)
                p = SearchProblem(domain,initial_lvl1,goal)
                t = SearchTree(p,'breadth')

                full_search_solution = t.search()
                search_solution = full_search_solution[1:]

                # print(t.search())
                # print(search_solution[0])
                # print(search_solution[1])
                # print(search_solution[2])
                # print(search_solution[3])
                # print(search_solution[4])

                for action in search_solution:
                    key = do_action(map, action, cursor, sel)
                    # print(action)
                    # print(type(action))

                await websocket.send(
                    json.dumps({"cmd": "key", "key": key})
                )  # send key command to server - you must implement this send in the AI agent
                
            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return  

            # Next line is not needed for AI agent
            pygame.display.flip()



# auxiliary functions


def do_action(map, action, cursor, sel):
    piece = action[0]
    act = action[1]
    if not same_coords(map, piece, cursor):
        return move_cursor_to_car(map, piece, cursor)
    if same_coords(map, piece, cursor) and sel != piece:
        return ' '
    if same_coords(map, piece, cursor) and sel == piece:
        return act



def same_coords(map, piece: str, cursor):
        piece_x = map.piece_coordinates(piece)[1].x
        cursor_x = cursor[0]
        piece_y = map.piece_coordinates(piece)[1].y
        cursor_y = cursor[1]
        return piece_x == cursor_x and piece_y == cursor_y

def move_cursor_to_car(map, piece:str, cursor):
        key = ""
        x_diff = cursor[0]-map.piece_coordinates(piece)[1].x
        if(x_diff>0):
            key = "a"
        elif(x_diff<0):
            key = "d"
        else:
            y_diff = cursor[1]-map.piece_coordinates(piece)[1].y
            if(y_diff>0):
                key = "w"
            elif(y_diff<0):
                key = "s"
        return key



# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='arrumador' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = os.environ.get("NAME", getpass.getuser())
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))