def even_fibo(number):
	sum = 0
	a, b = 0, 1
	c = b
	while c < number:
		if c % 2 == 0:
			sum += c
		c = a + b
		a, b = b, c
	print sum

T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	even_fibo(N)