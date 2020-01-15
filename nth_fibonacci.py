###############################################################################
#                                                                             #
#                           nth fibonacci number                              #
#                                                                             #
###############################################################################

# Apart from below two, there are other optimized way also. Will add those.


# Recursive
def get_nth_fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return get_nth_fib(n-1) + get_nth_fib(n-2)


# Caching
def get_nth_fib_by_caching(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = get_nth_fib_by_caching(n - 1) + get_nth_fib_by_caching(
                n - 2)
        return cache[n]


cache = {1: 0, 2: 1}


if __name__ == '__main__':
    print(get_nth_fib(6))
    print(get_nth_fib_by_caching(10))
