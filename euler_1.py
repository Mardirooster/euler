# the largest multiple of x under y = (y - 1 // x) * x
# any sum of sequential multiples of x can be expressed as follows:
# 3 + 6 + 9 + ... = 3 * (1 + 2 + 3 + ...)
# 1 + 2 + 3 + ... n is a triangular number and can be expressed as n*(n+1)/2
def sum_of_multiples(number,max=100):
    n = (max-1) // number
    print("Largest multiple of " + str(number) + " is " + str(n*number))
    return triangular_number(n) * number

def triangular_number(n):
    return int((n*(n+1)) / 2)



# mistake: 15 is a multiple of both 3 and 5, and so will be counted twice in my formula
# a simple solution should be to just subtract the sum of all multiples of 15
if __name__ == '__main__':
    test_total = sum_of_multiples(3,10) + sum_of_multiples(5,10) - sum_of_multiples(15,20)
    real_total = sum_of_multiples(3,1000) + sum_of_multiples(5,1000) - sum_of_multiples(15,1000)
    print("Euler 1:")
    print("Sum of multiples of 3 and 5 under 10 is: " + str(test_total))
    print("Sum of multiples of 3 and 5 under 1000 is: " + str(real_total))
