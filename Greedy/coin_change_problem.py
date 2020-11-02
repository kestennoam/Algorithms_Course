def coin_change_problem(k: int, C: list) -> list:
    """
    Given a value k, we have an infinite supply of each of the
    denominations in C.
    what is the minimum number of coins and/or notes needed to make the change?
    Note: greedy solution is not optimal (as example 2)
    :param k: value that we want to change
    :param C: List of the denominations
    :return: list with the minimal coins to return
    """
    C.sort(reverse=True)  # if it's not sorted
    ans = []
    i = 0
    while i < len(C):
        if C[i] <= k:
            # don't have to increase i
            k -= C[i]
            ans.append(C[i])
        else:
            i += 1
    return ans


if __name__ == '__main__':
    C = [1, 2, 5, 10]
    k = 23
    print(coin_change_problem(k, C))
    # solution that is not optimal with greedy solution
    C = [1, 3, 4, 10]
    k = 6
    print(coin_change_problem(k, C))
