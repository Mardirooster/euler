# the largest multiple of x under y = (y // x) * x
# any sum of sequential multiples of x can be expressed as follows:
# 3 + 6 + 9 + ... = 3 * (1 + 2 + 3 + ...)
# 1 + 2 + 3 + ... n is a triangular number and can be expressed as n*(n+1)/2
def sum_of_multiples(number,max=100):
		n = max // number
		return ((n*(n+1)) / 2 ) * number