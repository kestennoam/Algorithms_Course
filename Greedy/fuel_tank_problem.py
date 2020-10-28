def fuel_tank_problem(lst: list, N: int) -> list:
    """
    Given a number N which represents the total distance in km to be covered
    by a car on a single road. There are N petrol pumps at a distance of 1 km
    each(1, 2, 3, ..N). The capacity of the fuel tank of the car is such that
    at full tank it goes till a distance of K km. The car has to compulsorily
    stop at M petrol tanks whose distance from the starting position is given
    as M integers. The task is to find the number of times, the car has to
    refill its tank including the compulsory stops
    to complete its journey of N km.
    :param lst:
    :param N:
    :return:
    """
    # lst.sort() # just if it's not sorted
    ans = [lst[0]]  # start point always will be part of the journey
    for i in range(1, len(lst) - 1):
        # check if the next stop is too far from last stop
        if lst[i + 1] - ans[-1] > N:
            ans.append(lst[i])

    return ans + [lst[-1]]


if __name__ == '__main__':
    lst = [0, 1, 7, 9, 16, 17, 20]
    N = 10
    print(fuel_tank_problem(lst, N))
