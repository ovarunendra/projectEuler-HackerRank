def larget_prime(number):
	larget_prime = 0
	counter = 2
	while counter * counter <= number:
		if number % counter == 0:
			number = number / counter
			larget_prime = counter
		else:
			counter += 1
	if number > larget_prime:
		larget_prime = number
	print larget_prime

T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	larget_prime(N)