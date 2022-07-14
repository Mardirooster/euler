# the largest multiple of x under y = (y - 1 // x) * x
# any sum of sequential multiples of x can be expressed as follows:
# 3 + 6 + 9 + ... = 3 * (1 + 2 + 3 + ...)
# 1 + 2 + 3 + ... n is a triangular number and can be expressed as n*(n+1)/2
def sum_of_multiples(number,max=100):
    n = (max-1) // number
    return triangular_number(n) * number

def triangular_number(n):
    return int((n*(n+1)) / 2)


if __name__ == '__main__':
    test_total = sum_of_multiples(3,10) + sum_of_multiples(5,10)
    print("Euler 1:")
    print("Sum of multiples of 3 and 5 under 10 is: " + str(test_total))