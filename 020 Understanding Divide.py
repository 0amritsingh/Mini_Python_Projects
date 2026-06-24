def divide_info(n):
    divisors = []
    dividends = []
    remainders = []
    quotients = []
    factors = []
    for i in range(1, n+1):
        divisors.append(i)
        dividends.append(n)
        remainders.append(n%i)
        quotients.append(n/i)
        if n%i ==0:
            factors.append(i)
    print('dividends:\t', dividends)
    print('divisors:\t', divisors)
    print('quotients:\t', quotients)
    print('remainders:\t', remainders)
    print('factors:\t', factors)

divide_info(8)