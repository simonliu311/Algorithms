# Name: Simon Liu, Date: 09/24/2020

import sys
from collections import defaultdict
import resource


class Solution:
    def dfs(self):
        self.num_nodes = 0
        self.num_edges = 0
        # node_edges will keep track of all the edges coming out of every node
        # each key node points to a list of all nodes that the key node points towards
        # use a dict to store output in order they were first seen (input order)
        self.node_edges = defaultdict(list)
        self.output_dict = {}
        first_line = sys.stdin.readline().rstrip().split(' ')
        self.num_nodes, self.num_edges = int(first_line[0]), int(first_line[1])
        num_iter = 0

        while True:
            # keep taking new inputs until our  current number of edges reaches
            # the initial input for desired number of edges
            if num_iter >= self.num_edges:
                break

            # read in edge tuples until reaching num edges
            curr_line = sys.stdin.readline().rstrip().split(' ')
            num_1 = int(curr_line[0])
            num_2 = int(curr_line[1])
            self.node_edges[num_1].append(num_2)
            self.output_dict[(num_1, num_2)] = ''

            # increment count of number of edges added
            num_iter += 1

        # create variables to keep track of dfs
        # list ofnodes in initial  visit order
        self.output = []
        self.nodes = [i for i in range(self.num_nodes)]
        self.visited = [False] * self.num_nodes

        # preorder: when a node is visited, assign preorder[node] the current
        # pre_number. preorder[node] thus gives the rank at which a node was
        # visited in preorder
        self.preorder = [-1] * self.num_nodes
        self.pre_number = 0

        # postorder: when a node is visited, assign postorder[node] the current
        # post_number. postorder[node] thus gives the rank at which a node was
        # visited in the postorder.
        self.postorder = [-1] * self.num_nodes
        self.post_number = 0

        for n in self.nodes:
            self.dfs_walk(n)

        print(' '.join(self.output))

        # iterate through the output dictionary and for each key, value pair
        # print the two nodes and their label
        for key, value in self.output_dict.items():
            print('{} {} {}'.format(key[0], key[1], value[0]))

    def dfs_walk(self, node):
        if not self.visited[node]:
            # mark node as visited and add to output
            self.visited[node] = True
            self.output.append(str(node))

            # add this node to the preorder
            self.preorder[node] = self.pre_number
            self.pre_number += 1

            if node in self.node_edges:
                # if node connects to other nodes, explore all of the neighbors
                for next_node in self.node_edges[node]:
                    if not self.visited[next_node]:
                        # index of next_node in the dictionary
                        # corresponding to the position of next_node in the
                        # list at key node
                        index = self.node_edges[node].index(next_node)
                        # label the edge as a tree edge
                        self.node_edges[node][index] = '{}t'.format(
                            str(next_node))
                        # update output_dict
                        self.output_dict[(node, next_node)] = 't'
                        self.dfs_walk(next_node)
                    else:
                        # if coming 'back' up the call stack through the graph,
                        # check preorders as specified in H2release
                        # specifically, if edges go to nodes with a higher
                        # preorder
                        if self.preorder[next_node] > self.preorder[node]:
                            # update with forward edge, as above
                            index = self.node_edges[node].index(next_node)
                            self.node_edges[node][index] = '{}f'.format(
                                str(next_node))
                            self.output_dict[(node, next_node)] = 'f'
                        # b, c edges go to nodes that have a lower preorder number
                        else:
                            # if next_node does not have a postorder number yet,
                            # assign as back edge
                            if self.postorder[next_node] == -1:
                                index = self.node_edges[node].index(next_node)
                                self.node_edges[node][index] = '{}b'.format(
                                    str(next_node))
                                self.output_dict[(node, next_node)] = 'b'
                            # else if next_node has a postorder number, assign
                            # as a cross edge
                            else:
                                self.node_edges[(node, next_node)] = 'c'
                                index = self.node_edges[node].index(next_node)
                                self.node_edges[node][index] = '{}c'.format(
                                    str(next_node))
                                self.output_dict[(node, next_node)] = 'c'

            # after recursively traversing the graph, assign a postorder number
            # to this node
            self.postorder[node] = self.post_number
            self.post_number += 1


sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (100000000, 100000000))

sol = Solution()
sol.dfs()
