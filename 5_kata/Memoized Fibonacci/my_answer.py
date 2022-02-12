def fibonacci(n, already_found={0: 0, 1: 1}):
    if n in already_found.keys():
        return already_found[n]
    result_1 = fibonacci(n - 2, already_found)
    already_found[n - 2] = result_1
    result_2 = fibonacci(n - 1, already_found)
    already_found[n - 1] = result_2
    return result_1 + result_2