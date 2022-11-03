def GCD(x, y):
    while y:
        x, y = y, x % y

    return abs(x)


def poly(x, n):
    return (x * x + 1) % n


def rho(n, start = 2):
    d = 1
    fast = slow = start
    while d == 1:
        slow = poly(slow, n)
        fast = poly(poly(fast, n), n)
        d = GCD(abs(slow - fast), n)

    if d == n:
        return 'failure'
    else:
        return f"{n} has a factor of {d}"



print(rho(30585774636547 * 1238926361552897))
