# Realizado por: Rafael Curado, 103199
# Comentado com:
# - Bernardo Marçal, 103236
# - Guilherme Alves, 103185
# - João Ferreira, 103625

from tree_search import *
from cidades import *
from blocksworld import *


def func_branching(connections,coordinates):    # ex 1
    #IMPLEMENT HERE
    neighbor_cities = []
    
    for C in coordinates:
        neighbor_cities.append(len(func_actions(connections,C)))

    # return average number of neighbor cities computed over all cities, substracting 1
    return (sum(neighbor_cities)/len(neighbor_cities))-1
    

class MyCities(Cidades):
    def __init__(self,connections,coordinates):
        super().__init__(connections,coordinates)
        # ADD CODE HERE IF NEEDED

class MySTRIPS(STRIPS):
    def __init__(self,optimize=False):
        super().__init__(optimize)

    def simulate_plan(self,state,plan):
        #IMPLEMENT HERE
        for strip in plan:
            state = self.result(state, strip)
        return state

 
class MyNode(SearchNode):
    def __init__(self,state,parent,cost,heuristic,depth):
        super().__init__(state,parent)
        #ADD HERE ANY CODE YOU NEED
        self.cost = cost                #
        self.heuristic = heuristic      #  parte do ex 2
        self.depth = depth              #


class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',optimize=0,keep=0.25): 
        super().__init__(problem,strategy)
        #ADD HERE ANY CODE YOU NEED
        self.optimize = optimize
        self.keep = keep 

        if(optimize == 0):
            root = MyNode(problem.initial, None, 0, problem.domain.heuristic(problem.initial, problem.goal), 0)  
            self.all_nodes = [root]
            self.open_nodes = [0]   
        elif(optimize == 1):
            root = (problem.initial, None, 0, problem.domain.heuristic(problem.initial, problem.goal), 0)
            self.all_nodes = [root]
            self.open_nodes = [0]   
        elif(optimize == 2):
            root = (problem[1], None, 0, problem[0][3](problem[1],problem[2]) , 0)
            self.all_nodes = [root]
            self.open_nodes = [0]  
        elif(optimize == 4):
            root = (problem[1], None, 0, problem[0][3](problem[1],problem[2]) , 0)
            self.all_nodes = [root]
            self.open_nodes = [0]


            
    def astar_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        self.open_nodes.extend(lnewnodes)
        if (self.optimize == 0):
            return self.open_nodes.sort(key = lambda index : self.all_nodes[index].cost + self.all_nodes[index].heuristic)
        #elif (self.optimize == 4):
            #return self.open_nodes.sort(key = lambda index : self.all_nodes[index][2] + self.all_nodes[index][3])


    # remove a fraction of open (terminal) nodes
    # with lowest evaluation function
    # (used in Incrementally Bounded A*)
    def forget_worst_terminals(self):
        #IMPLEMENT HERE
        pass

    # procurar a solucao
    def search2(self):
        #IMPLEMENT HERE
        while self.open_nodes != []:
            nodeID = self.open_nodes.pop(0)
            node = self.all_nodes[nodeID]

            if(self.optimize == 0):                     
                if self.problem.goal_test(node.state):
                    self.solution = node
                    self.terminals = len(self.open_nodes)+1
                    return self.get_path(node)
                lnewnodes = []
                self.non_terminals += 1
                for a in self.problem.domain.actions(node.state):
                    newstate = self.problem.domain.result(node.state,a)
                    if newstate not in self.get_path(node):
                        newnode = MyNode(newstate,nodeID, node.cost + self.problem.domain.cost(node.state, a), self.problem.domain.heuristic(newstate, self.problem.goal), node.depth + 1)
                        lnewnodes.append(len(self.all_nodes))
                        self.all_nodes.append(newnode)
                self.add_to_open(lnewnodes)
            

            elif(self.optimize == 1):                   # ex 3, using tuples to represent nodes
                if self.problem.goal_test(node[0]):
                    self.solution = node
                    self.terminals = len(self.open_nodes)+1
                    return self.get_path_as_tuple(node)
                lnewnodes = []
                self.non_terminals += 1
                for a in self.problem.domain.actions(node[0]):
                    newstate = self.problem.domain.result(node[0],a)
                    if newstate not in self.get_path_as_tuple(node):
                        newnode = (newstate,nodeID, node[2] + self.problem.domain.cost(node[0], a), self.problem.domain.heuristic(newstate, self.problem.goal), node[4] + 1)
                        lnewnodes.append(len(self.all_nodes))
                        self.all_nodes.append(newnode)
                self.add_to_open(lnewnodes)


            elif(self.optimize == 2):                   # ex 4, problems represented by tuples
                if self.problem[0][4](node[0],self.problem[2]):
                    self.solution = node
                    self.terminals = len(self.open_nodes)+1
                    return self.get_path_as_tuple(node)
                lnewnodes = []
                self.non_terminals += 1
                for a in self.problem[0][0](node[0]):
                    newstate = self.problem[0][1](node[0],a)
                    if newstate not in self.get_path_as_tuple(node):
                        newnode = (newstate,nodeID, node[2] + self.problem[0][2](node[0], a), self.problem[0][3](newstate, self.problem[2]), node[4] + 1)
                        lnewnodes.append(len(self.all_nodes))
                        self.all_nodes.append(newnode)
                self.add_to_open(lnewnodes)


            elif(self.optimize == 4):                   # ex 5, graph search algorithm
                if self.problem[0][4](node[0],self.problem[2]):
                    self.solution = node
                    self.terminals = len(self.open_nodes)+1
                    return self.get_path_as_tuple(node)
                lnewnodes = []
                self.non_terminals += 1
                for a in self.problem[0][0](node[0]):
                    newstate = self.problem[0][1](node[0],a)
                    if newstate not in self.get_path_as_tuple(node):
                        newnode = (newstate,nodeID, node[2] + self.problem[0][2](node[0], a), self.problem[0][3](newstate, self.problem[2]), node[4] + 1)
                        lnewnodes.append(len(self.all_nodes))
                        exists = False
                        for n in self.all_nodes:
                            if (n[0] == newstate):
                                exists = True 
                                if(newnode[2] + newnode[3] < n[2]):
                                    n = (newstate, newnode[1], newnode[2], newnode[3], newnode[4])
                        if not exists:
                            self.all_nodes.append(newnode)
                self.add_to_open(lnewnodes)
        return None



# If needed, auxiliary functions can be added

    def get_path_as_tuple(self,node):      # ex 3 auxiliary function 
        if node[1] == None:
            return [node[0]]
        path = self.get_path_as_tuple(self.all_nodes[node[1]])
        path += [node[0]]
        return(path)