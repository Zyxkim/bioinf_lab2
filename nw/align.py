import copy
import itertools


def sigma(a, b):
    return 5 if a == b else -4


def score_nomatrix(a, b, gap=-5):
    n = len(a)
    m = len(b)

    D_one = [(gap * i) for i in range(m + 1)]

    for i in range(1, n + 1):
        tmp = copy.deepcopy(D_one)
        D_one[0] = gap * i
        for j in range(1, m + 1):
            delete = D_one[j] + gap
            insert = D_one[j - 1] + gap
            match = tmp[j - 1] + sigma(a[i - 1], b[j - 1])

            score_max = max(delete, insert, match)
            D_one[j] = score_max

    print('Score:', D_one[m])
    return D_one[m]


def init_D(m, n, gap, k):
    D = [[0] * (m + 1) for _ in range(n + 1)]

    if n > 0:
        if k <= n:
            for j in range(1, k + 1):
                D[j][0] = gap * j
        else:
            for j in range(1, k):
                D[j][0] = gap * j
    if m > 0:
        if k <= m:
            for i in range(1, k + 1):
                D[0][i] = gap * i
        else:
            for i in range(1, k):
                D[0][i] = gap * i

    return D


def score_k(a, b, gap=-5, k=1):
    if len(a) < len(b):
        a, b = b, a
    assert len(b) + 1 + k + 1 >= len(a) + 1, 'Incorrect diagonale!'

    n = len(a)
    m = len(b)

    D = init_D(m, n, gap, k)

    for i, j in itertools.product(range(1, n + 1), range(1, m + 1)):
        if abs(j - i) <= k:
            delete = D[i - 1][j] + gap
            insert = D[i][j - 1] + gap
            match = D[i - 1][j - 1] + sigma(a[i - 1], b[j - 1])

            score_max = max(match, insert, delete)
            D[i][j] = score_max

    print('Score k:', D[n][m])

    return D[n][m]


def check(a, b, gap=-5, k=3):
    res_k = score_k(a, b, gap, k)
    return False if res_k != score_k(a, b, gap, k + 1) else res_k
