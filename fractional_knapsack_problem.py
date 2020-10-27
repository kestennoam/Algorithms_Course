def fractional_knapsack_problem(pairs: "list[(int, int)]", W: int):
    """
    This function is one of the most popular Greedy's algorithms.

    :param W: Max weight the thief can carry inside his backpack
    :param pairs: list of tuples represent the first cell is the value of the
    item and the second cell represent it's weight
    :return: list[(float, int)] represent the fractional part of the item, and
    it's value that the thief could still
    """
    pairs.sort(key=lambda x: -(x[0] / x[1]))
    sigma_w, ans = 0, []
    for v, w in pairs:
        x = min((W - sigma_w) / w, 1)
        if x > 0:
            ans.append((x, v))
        sigma_w += (x * w)

    return ans


if __name__ == '__main__':
    lst = [[120, 30], [100, 20], [60, 10]]
    W = 50.0
    res = fractional_knapsack_problem(lst, W)
    print(res)
