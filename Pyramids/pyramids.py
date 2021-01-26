# Name: Simon Liu, Date: 12/08/2020

import sys

def build_pyramid(num_stacks, heights):
	# initialize DP arrays
	# DP arrays left, right: maintains the maximum permissible height up to the
	# ith stack at index i, looking from the left and right
	left = [0 for _ in range(num_stacks)]
	right = [0 for _ in range(num_stacks)]
	res = [0 for _ in range(num_stacks)]

	# initialize with the height 1 at each end, 0 if
	# stack height is empty at the ends
	left[0] = 0 if heights[0] == 0 else 1
	right[-1] = 0 if heights[-1] == 0 else 1

	# DP recurrence relation: height can be no greater than any of:
		# 1. height of previous highest + 1 (only add 1 per index)
		# 2. prev height + 1 (otherwise it would be too wide)
		# 3. height of stack at index i
	for i in range(1, num_stacks):
		r_i = num_stacks - 1 - i

		left[i] = min(left[i-1]+1,i+1,heights[i])
		right[r_i] = min(right[r_i+1]+1,num_stacks-r_i,heights[r_i])
	# populate result array with the minimum looking from left and right
	for i in range(num_stacks):
		res[i] = min(left[i],right[i])
	height = max(res)
	index = res.index(height)
	# output height, index
	return str(height), str(index)

# read inputs
N = int(sys.stdin.readline().rstrip())
str_2 = sys.stdin.readline().rstrip().split(' ')
H = [int(i) for i in str_2 if i != ' ']

height, index = build_pyramid(N, H)
# print result
print(height + ' ' + index)
