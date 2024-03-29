from random import randint
from random import random
import math


class sim_Anl:
    def search(self, problem):
        visited = 0
        expanded = 0
        current = problem.state_initialization()
        neighbors = []
        threshold = 10
        # counter = 1
        T = 1
        T_min = .001
        while True:
            T = sim_Anl.schedule(self, T)
            if T < T_min:
                print("visited", visited)
                print("expanded", expanded)
                return current
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                visited += 1
                neighbors.append(neighbor)
            index = randint(0, len(neighbors) - 1)
            nextState = neighbors[index]
            ap = sim_Anl.acceptance_probability(self, current, nextState, T)
            if ap > random():
                current = nextState
                # counter += 1
            expanded += 1

    def schedule(self, T):
        alpha = .8
        T *= alpha
        return T

    def acceptance_probability(self, current, nextState, T):

        if current.cost > nextState.cost:
            return 1
        else:
            return math.e ** ((current.cost - nextState.cost) / T)


class Hill:
    visited = 0
    expanded = 0

    def standard_search(self, problem):
        current = problem.state_initialization()
        best_cost = current.cost
        best_node = current
        while not problem.goal_test(current):
            Hill.expanded += 1
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                Hill.visited += 1
                neighbor_cost = neighbor.cost
                if neighbor_cost < best_cost:
                    best_cost = neighbor_cost
                    best_node = neighbor
            current = best_node
        return current

    def random_search(self, problem):
        Hill.expanded = 0
        Hill.visited = 0
        current = problem.state_initialization()
        best_cost = current.cost
        while not problem.goal_test(current):
            Hill.expanded += 1
            increase_list = []
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neighbor_cost = neighbor.cost
                Hill.visited += 1
                if neighbor_cost < best_cost:
                    increase_list.append(neighbor)
            index = randint(0, len(increase_list) - 1)
            print("index", index)
            current = increase_list[index]

        return current

    def first_choise_search(self, problem):
        Hill.expanded = 0
        Hill.visited = 0
        current = problem.state_initialization()
        while not problem.goal_test(current):
            Hill.expanded += 1
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neighbor_cost = neighbor.cost
                Hill.visited += 1
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


class Genetic:
    N = 200

    def search(self, problem):
        generationNum = 1
        population = []
        populationFitness = []
        for i in range(0, Genetic.N):
            population.append(problem.state_initialization())
        while True:
            best_possible = problem.best_value()
            for indiv in population:
                populationFitness.append(problem.fitness(indiv))
                if problem.fitness(indiv) > .9 * best_possible:
                    print("generationNum", generationNum)
                    return indiv
            populationFitness.sort()
            print("generationNum", generationNum)
            print("average", sum(populationFitness) / max(len(populationFitness), 1))
            print("best", populationFitness.pop())
            print("worst", populationFitness.pop(0))
            newPopulation = []
            for i in range(0, Genetic.N):
                x = Genetic.randomSelection(self, population)
                y = Genetic.randomSelection(self, population)
                child = Genetic.produce(self, x, y)
                if (1 / (len(newPopulation) + 1)*2) > random():
                    child = Genetic.mutate(self, child)
                newPopulation.append(child)
            population = newPopulation
            generationNum += 1

    def randomSelection(self, population):
        index = randint(0, len(population) - 1)
        return population[index]

    def produce(self, x, y):
        child = []
        c = randint(0, len(x) - 1)
        for i in range(0, len(x)):
            if i < c:
                child.append(x[i])
            else:
                child.append(y[i])
        return child

    def mutate(self, child):
        n = randint(0, len(child) - 1)
        if child[n] == 0:
            child[n] = 1
        else:
            child[n] = 0
        return child
