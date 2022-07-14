# calculate the sum of all even fibonacci terms
# [1,2,3,5,8,13,21,34,]


# return a list of the fibonacci sequence up to a max
def fibonacci(max):
	sequence = [1,2]
	next_number = sequence[-1] + sequence [-2]
	while next_number <= max:
		sequence.append(next_number)
		next_number = sequence[-1] + sequence [-2]
	return sequence


# a simple solution based on the properties of the fibonacci sequence:
# the fibonacci numbers will, starting on 2, be even every three numbers
# proof:
# let f[k] = the kth number of the fibonacci sequence
# f[k], f[k+1], f[k+2], f[k+3], f[k+4]
# assume f[k] is even, and f[k+1] is odd
# from this, f[k+2] is odd (f[k] + f[k+1] -> even + odd = odd)
# and f[k+3] is even (f[k+1] + f[k+2] -> odd + odd = even)
# hence, assuming that we start with an even and an odd number, the sequence will repeat:
# ... even, odd, odd, even, odd, odd, even, odd, odd ...
# as the fibonacci sequence starts with 1 and 2, we see this holds for the base case!




if __name__ == '__main__':
		fibonacci_sequence = fibonacci(4000000)
		fibonacci_even = fibonacci_sequence[1::3] #cut the first element and then return every 3rd
		print(str(sum(fibonacci_even)))