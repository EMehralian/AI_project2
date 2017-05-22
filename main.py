import TSP
import informed_algs
import knapsack


def main():
    # sim_anl = informed_algs.sim_Anl()
    # sim_anl_answer = sim_anl.search(TSP.TSP())
    # print("sim_anl", sim_anl_answer.position, sim_anl_answer.cost)

    hill = informed_algs.Hill()
    # standard_answer = hill.standard_search(TSP.TSP())
    # print("standard:", standard_answer.position, standard_answer.cost)
    # print("visited", hill.visited)
    # print("expanded", hill.expanded)
    # random_answer = hill.random_search(TSP.TSP())
    # print("random_search:", random_answer.position, random_answer.cost)
    # print("visited", hill.visited)
    # print("expanded", hill.expanded)
    # first_choise_answer = hill.first_choise_search(TSP.TSP())
    # print("first_choise_search:", first_choise_answer.position, first_choise_answer.cost)
    # print("visited", hill.visited)
    # print("expanded", hill.expanded)
    # random_reset_answer = hill.random_reset_search(TSP.TSP())
    # print("random_reset_search:", random_reset_answer.position, random_reset_answer.cost)
    # print("visited", hill.visited)
    # print("expanded", hill.expanded)
    genetic = informed_algs.Genetic()
    answer = genetic.search(knapsack.Knapsack())
    print(answer)


if __name__ == "__main__":
    print("hi")
    main()
