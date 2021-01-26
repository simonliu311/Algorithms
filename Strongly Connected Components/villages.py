# Name: Simon Liu, Date: 10/13/2020

import sys


class Solution:
    # read input from stdin
    def read_in(self):
        # take first line as number of villages, number of roads
        first_line = sys.stdin.readline().rstrip().split(' ')
        self.num_villages, self.num_roads = int(
            first_line[0]), int(first_line[1])

        # number of components in the graph. Initialize as equal to
        # number of villages.
        self.components = self.num_villages

        self.graph = [i for i in range(self.num_villages)]

        for i in range(self.num_roads):
            # keep taking in a number of lines, describing roads, equal to the
            # number of roads specified in first line
            # read in edge tuples
            curr_line = sys.stdin.readline().rstrip().split(' ')
            node_u, node_v = int(curr_line[0]), int(curr_line[1])
            # compute and store ancestor of the two inputs
            root_u = self.find_ancestor(self.graph, node_u)
            root_v = self.find_ancestor(self.graph, node_v)
            # see if node_u, node_v, share a common ancestor/root/are connected
            # if they are not connnected: add 1 to number of connected components
            if root_u != root_v:
                # node_u and node_v must share an ancestor since they are given
                # as connected villages. Reduce the number of components by 1.
                self.components -= 1
                # perform this update so that
                self.graph[root_v] = root_u
            # self.node_edges[num_1]
        # the number of new roads needed is equal to the number of components - 1
        print(self.components - 1)

    # merges nodes to be represented as the same number in parameter nodes (called
    # with variable self.graph)
    # nodes are 'merged' by giving them the same number if they share an ancestor
    def find_ancestor(self, nodes, u):
        while True:
            if nodes[u] == u:
                return u
            else:
                nodes[u] = nodes[nodes[u]]
                u = nodes[u]

sol = Solution()
sol.read_in()
