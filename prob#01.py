def sum_multiple(multiple, num):
	n = (num - 1) / multiple
	return n * (n + 1) / 2 * multiple

T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	print sum_multiple(3, N) + sum_multiple(5, N) - sum_multiple(15, N)