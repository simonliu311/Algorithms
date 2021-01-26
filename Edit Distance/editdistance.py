# Name: Simon Liu, Date: 11/03/2020

import sys


class Solution:
    # read in two strings as input
    def read_input(self):
        str_1 = sys.stdin.readline().rstrip()
        str_2 = sys.stdin.readline().rstrip()
        self.compute_edit_distance(str_1, str_2)

    """
    computing edit distance using recurrence relation
    from textbook 6.16
    With gap penalty, mismatch penalty as specified in
    the problem statement.
    """

    def compute_edit_distance(self, X, Y):
        m = len(X)
        n = len(Y)
        # initialize DP array to maintain optimal sub-solutions
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        # initialize the first row and first column
        # of 2-d DP array, trivially
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        # iterative DP
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                #use recurrence 6.16
                #OPT(i,j) = min[OPT(i-1,j-1)+mismatch cost,1+OPT(i-1,j),1+OPT(i,j-1)
                # where gap penalty = 1 for all i,j
                # mismatch penalty = 0 if last char of X = last char of Y
                # otherwise, mismatch penalty = 1
                mismatch = 0 if X[i - 1] == Y[j - 1] else 1
                dp[i][j] = min(dp[i - 1][j - 1] + mismatch, dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1)

        # last element of DP array contains the solution for edit distance
        self.edit_distance = dp[-1][-1]
        self.backtrack(dp, X, Y)
        self.sol()

    """
    Use backtracking technique to generate the unique
    strings, given the optimal edit distance as
    computed above
    """

    def backtrack(self, dp, X, Y):
        # use temp to keep track of last seen pair of indices
        m = len(X)
        n = len(Y)

        res_X = ''
        res_Y = ''
        while True:
            # continue until we reach element at dp[0][0]
            if m == n == 0:
                break

            # the min adjacent/diagonal index, from which our current
            # dp pointer is built, encodes information about the
            # operation needed to get to current dp[m][n]
            min_index = min(dp[m - 1][n - 1], dp[m - 1][n], dp[m][n - 1])

            # if edit distance taken from dp[m-1][n-1], then
            # there is a matching pair of characters in X, Y
            # append this character to both X and Y
            if min_index == dp[m - 1][n - 1]:
                m, n = m - 1, n - 1
                res_X += X[m]
                res_Y += Y[n]

            # if edit distance taken from dp[m][n-1],
            # then X is missing that character, so add
            # a space. Append the character to Y
            elif min_index == dp[m][n - 1]:
                n -= 1
                res_X += ' '
                res_Y += Y[n]

            # if edit distance taken from dp[m-1][n],
            # then Y is missing that character, so add
            # a space. Append the character to X
            elif min_index == dp[m - 1][n]:
                m -= 1
                res_X += X[m]
                res_Y += ' '

        self.res_X = res_X[::-1]
        self.res_Y = res_Y[::-1]

    # output solution
    def sol(self):
        print(self.edit_distance)
        print(self.res_X)
        print(self.res_Y)


my_solution = Solution()
my_solution.read_input()
