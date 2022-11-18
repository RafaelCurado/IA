
# Module: tree_search
# 
# This module provides a set o classes for automated
# problem solving through tree search:
#    SearchDomain  - problem domains
#    SearchProblem - concrete problems to be solved
#    SearchNode    - search tree nodes
#    SearchTree    - search tree with the necessary methods for searhing
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2019,
#  Inteligência Artificial, 2014-2019

from abc import ABC, abstractmethod
import copy

# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    @abstractmethod
    def satisfies(self):
        pass


# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self,state):
        return self.domain.satisfies(state)

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self,state,parent, action=None): 
        self.state = state
        self.parent = parent
        self.action = action
    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth'): 
        self.problem = problem
        root = SearchNode(problem.initial, None)
        self.open_nodes = [root]
        self.strategy = strategy
        self.solution = None

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.action]
        path = self.get_path(node.parent)
        path += [node.action]
        return(path)

    # procurar a solucao
    def search(self):
        while self.open_nodes != []:
            #print(self.open_nodes)
            node = self.open_nodes.pop(0)
            #print(node.state)
            if self.problem.goal_test(node.state):
                print("golo")
                self.solution = node
                return self.get_path(node)
            lnewnodes = []
            #print(self.problem.domain.actions(node.state))
            for a in self.problem.domain.actions(node.state):
                auxstate = copy.deepcopy(node.state)
                newstate = self.problem.domain.result(auxstate,a)
                if newstate not in self.get_path(node):
                    newnode = SearchNode(newstate,node,a)
                    lnewnodes.append(newnode)
                    #print("adicionou")
                    #print(lnewnodes)
            self.add_to_open(lnewnodes)
            print()
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':
            pass