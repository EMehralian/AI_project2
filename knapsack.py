import DS
import problem
from random import randint


class Knapsack(problem.Problem):
    initializedState = []
    weight = []
    worth = []
    maxWeight = 0
    goal = None
    start = None
    N = 0

    def __init__(self):
        print("Enter board:")
        Knapsack.weight = (input().split())
        Knapsack.worth = (input().split())
        if len(Knapsack.weight) != len(Knapsack.worth):
            print("Wrong input")
            return
        Knapsack.maxWeight = int(input())
        Knapsack.N = len(Knapsack.weight)

    def fitness(self, individual):
        indiv_value = 0
        indiv_weight = 0
        for i in range(0, Knapsack.N):
            if individual[i] == 1:
                indiv_value += int(Knapsack.worth[i])
                indiv_weight += int(Knapsack.weight[i])
        if indiv_weight > int(Knapsack.maxWeight):
            return 0
        return indiv_value

    def best_value(self):
        density = []
        for i in range(0, Knapsack.N):
            density.append([int(Knapsack.worth[i]) / int(Knapsack.weight[i]), i])
        density.sort(reverse=True)
        remain = Knapsack.maxWeight
        j = 0
        best = 0
        while remain > 0:
            if remain > int(Knapsack.weight[density[j][1]]):
                best += int(Knapsack.worth[density[j][1]])
                remain -= int(Knapsack.weight[density[j][1]])
            else:
                best += int(Knapsack.worth[density[j][1]]) * (remain / int(Knapsack.weight[density[j][1]]))
                remain =0
            j+=1
        return best

    def state_initialization(self):
        position = []
        for i in range(0, Knapsack.N):
            position.append(randint(0, 1))
        # sample_indiv = KSState(None, None, Knapsack.fitness(self, position), position)
        return position

    def actions(self, state):
        print(" ")
        # actions = []
        # for i in range(TSP.N - 1):
        #     for j in range(i + 1, TSP.N):
        #         actions.append([i, j])
        # return actions

    def result(self, state, action):
        print(" ")
        # board = []
        # for i in range(0, TSP.N):
        #     board.append(state.position[i])
        # temp = board[action[0]]
        # board[action[0]] = board[action[1]]
        # board[action[1]] = temp
        # for tspState in TSP.initializedState:
        #     if board == tspState.position:
        #         return tspState

        # newState = TSPState(state, action, 0, board)
        # newState.cost = TSP.path_cost(self, newState, newState)
        # TSP.initializedState.append(newState)
        # return newState

    def path_cost(self, father, state):
        print(" ")
        # cost = 0
        # for i in range(0, TSP.N - 1):
        #     cost += int(TSP.mapp[state.position[i]][state.position[i + 1]])
        # cost += int(TSP.mapp[state.position[TSP.N - 1]][state.position[0]])
        # return cost

    def goal_test(self, state):
        print(" ")
        # for action in TSP.actions(self, state):
        #     nstate = TSP.result(self, state, action)
        #     if nstate.cost < state.cost:
        #         return False
        # return True


class KSState(DS.Node):
    # board = [[0 for x in range(3)] for y in range(3)]
    counter = 0

    def __init__(self, parent, action, cost, position):
        # global counter
        super().__init__(parent, action, cost)
        self.position = position
        self.stateNumber = KSState.counter
        KSState.counter += 1


if __name__ == "__main__":
    Knapsack().state_initialization()
