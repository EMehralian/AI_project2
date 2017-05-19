from random import randint
from random import random
import math

class sim_Anl:
    def search(self, problem):
        current = problem.state_initialization()
        neighbors = []
        threshold = 10
        # counter = 1
        T = 1
        T_min = .001
        while True:
            T = sim_Anl.schedule(self, T)
            if T < T_min:
                return current
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neighbors.append(neighbor)
            index = randint(0, len(neighbors) - 1)
            nextState = neighbors[index]
            ap = sim_Anl.acceptance_probability(self, current, nextState, T)
            if ap > random():
                current = nextState
            # counter += 1

    def schedule(self, T):
        alpha = .8
        T *= alpha
        return T

    def acceptance_probability(self, current, nextState, T):

        if current.cost > nextState.cost:
            return 1
        else:
            return math.e ^ ((nextState.cost - current.cost) / T)


class Hill:
    def standard_search(self, problem):
        current = problem.state_initialization()
        best_cost = current.cost
        best_node = current
        while not problem.goal_test(current):
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neighbor_cost = neighbor.cost
                if neighbor_cost < best_cost:
                    best_cost = neighbor_cost
                    best_node = neighbor
            current = best_node
        return current

    def random_search(self, problem):
        current = problem.state_initialization()
        best_cost = current.cost
        while not problem.goal_test(current):
            increase_list = []
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neighbor_cost = neighbor.cost
                if neighbor_cost < best_cost:
                    increase_list.append(neighbor)
            index = randint(0, len(increase_list) - 1)
            print("index", index)
            current = increase_list[index]
        return current

    def first_choise_search(self, problem):
        current = problem.state_initialization()
        while not problem.goal_test(current):
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neighbor_cost = neighbor.cost
                if neighbor_cost < current.cost:
                    current = neighbor
                    break
        return current

    def random_reset_search(self, problem):
        h = Hill()
        best = 0
        result = []
        for i in range(0, 5):
            result.append(h.standard_search(problem))
        temp = 0
        for i in range(0, 5):
            pcost = problem.path_cost(result[i], result[i])
            if pcost > temp:
                temp = pcost
                best = result[i]

        return best

