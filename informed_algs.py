from random import randint


class sim_Anl:
    def search(self, problem):
        maxQ = 0


class Hill:
    def standard_search(self, problem):
        current = problem.state_initialization()
        best_cost = problem.path_cost(0, current)
        while not problem.goal_test(current):
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neighbor_cost = problem.path_cost(0, neighbor)
                if neighbor_cost > best_cost:
                    best_cost = neighbor_cost
                    current = neighbor
        return current

    def random_search(self, problem):
        current = problem.state_initialization()
        best_cost = problem.path_cost(0, current)
        while not problem.goal_test(current):
            increase_list = []
            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neighbor_cost = problem.path_cost(0, neighbor)
                if neighbor_cost > best_cost:
                    increase_list.append(neighbor)
            index = randint(0, len(increase_list))
            current = increase_list[index]
        return current

    def first_choise_search(self, problem):
        current = problem.state_initialization()
        best_cost = problem.path_cost(0, current)
        while not problem.goal_test(current):

            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neighbor_cost = problem.path_cost(0, neighbor)
                if neighbor_cost > best_cost:
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
            if (problem.path_cost(result[i]) > temp):
                temp = problem.path_cost(result[i])
                best = result[i]

        return best
