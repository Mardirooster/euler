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