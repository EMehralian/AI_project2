import DS
import problem
import random
import numpy as np
import math


class TSP(problem.Problem):
    initializedState = []
    goal = None
    start = None
    mapp = []
    N = 0

    def __init__(self):
        print("Enter board:")
        TSP.mapp.append(input().split())
        TSP.N = len(TSP.mapp[0])
        for x in range(len(TSP.mapp[0]) - 1):
            TSP.mapp.append(input().split())

        print(TSP.mapp)

    def state_initialization(self):
        startArr = random.sample(range(0, TSP.N), TSP.N)
        start = TSPState(None, None, 0, startArr)
        start.cost = TSP.path_cost(self, start, start)
        TSP.initializedState.append(start)
        return start

    def actions(self, state):
        actions = []
        for i in range(TSP.N - 1):
            for j in range(i + 1, TSP.N):
                actions.append([i, j])
        return actions

    def result(self, state, action):
        board = []
        for i in range(0, TSP.N):
            board.append(state.position[i])
        temp = board[action[0]]
        board[action[0]] = board[action[1]]
        board[action[1]] = temp
        for tspState in TSP.initializedState:
            if board == tspState.position:
                return tspState

        newState = TSPState(state, action, 0, board)
        newState.cost = TSP.path_cost(self, newState, newState)
        TSP.initializedState.append(newState)
        return newState

    def path_cost(self, father, state):
        cost = 0
        for i in range(0, TSP.N - 1):

            cost += int(TSP.mapp[state.position[i]][state.position[i + 1]])
        cost += int(TSP.mapp[state.position[TSP.N - 1]][state.position[0]])
        return cost

    def goal_test(self, state):
        for action in TSP.actions(self, state):
            nstate = TSP.result(self, state, action)
            if nstate.cost < state.cost:
                return False
        return True


class TSPState(DS.Node):
    # board = [[0 for x in range(3)] for y in range(3)]
    counter = 0

    def __init__(self, parent, action, cost, position):
        # global counter
        super().__init__(parent, action, cost)
        self.position = position
        self.stateNumber = TSPState.counter
        TSPState.counter += 1


if __name__ == "__main__":
    TSP().state_initialization()
