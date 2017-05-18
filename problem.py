import abc


class Problem(object):

    __metaclass__ = abc.ABCMeta
    """The abstract class for a formal problem."""

    @abc.abstractmethod
    def state_initialization(self):
        return

    # Return the actions that can be executed in the given state
    @abc.abstractmethod
    def actions(self, state):
        return

    # Return the state that results from executing the given action in the given state
    @abc.abstractmethod
    def result(self, state, action):
        return

    # checks that if the state is goal
    @abc.abstractmethod
    def goal_test(self, state):
        return

    # Return the cost of a solution
    @abc.abstractmethod
    def path_cost(self, father, action):
        return
