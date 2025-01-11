#!/usr/bin/python3
''' who wins '''


def isWinner(x, nums):
    ''' who wins prime game '''
    if x < 1 or not nums:
        return None

    maria, ben = 0, 0

    n = max(nums)
    prime = [True for _ in range(1, n + 1, 1)]
    prime[0] = False
    for i, isprime in enumerate(prime, 1):
        if i == 1 or not isprime:
            continue
        for j in range(i + i, n + 1, i):
            prime[j - 1] = False

    for j, n in zip(range(x), nums):
        count = len(list(filter(lambda x: x, prime[0: n])))
        ben += count % 2 == 0
        maria += count % 2 == 1
    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'
