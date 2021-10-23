def factorize(number):
    import math
    d = dict()

    count = 0  # To count the power of the index number(number is 2 here)

    while number % 2 == 0:  # We have to divide the number by 2 until number%2 is 0
        number = number // 2
        count += 1  # Increment the count

    if count > 0:
        d[2] = count  # If 2 is on of the prime factor the

    # check for all the possible
    # numbers that can divide it
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        count = 0

        while number % i == 0:
            count += 1
            number = number // i

        if count > 0:
            d[i] = count

    # if n at the end is a prime number.
    if number > 2:
        d[number] = 1
    return d