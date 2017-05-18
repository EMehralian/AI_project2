import abc


class Node:
    __metaclass__ = abc.ABCMeta

    def __init__(self, parent, action, cost):
        self.parent = parent
        self.action = action
        self.cost = cost
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

    def path(self):
        """Create a list of nodes from the root to this node."""
        x, result = self, [self]
        while x.parent:
            result.append(x.parent)
            x = x.parent
        return result
