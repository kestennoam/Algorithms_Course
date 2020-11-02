def task_scheduler(tasks):
    """
    This algorithm is for scheduling tasks.
    the goal is to check what is the largest subset of tasks that can be
    handled while there is a condition that 2 tasks cannot be handled
    simultaneity.

    Time Complexity: O(nlog(n))
    Space Complexity: O(1) except ans list
    :param tasks: list of lists of2 integers,
                  represent the start and end time of taksk
    :return: List[[st,end]] - largest subset of tasks
    """
    tasks.sort(key=lambda x: (x[1], x[0]))
    ans = []
    for st, end in tasks:
        if not ans or ans[-1][1] <= st:
            ans.append([st, end])
    return ans


if __name__ == '__main__':
    # test 1: expected : [[0, 2], [2, 3], [3, 4]]
    tasks = [[0, 2], [2, 3], [1, 4], [1, 2], [3, 4]]
    print(task_scheduler(tasks))
    # test 2: expected : [[3, 4], [4, 5]]
    tasks = [[4, 5], [0, 8], [3, 4]]
    print(task_scheduler(tasks))
    # test 3: expected : []
    tasks = []
    print(task_scheduler(tasks))
    # test 4: expected : [[1,1]]
    tasks = [[1, 1]]
    print(task_scheduler(tasks))
