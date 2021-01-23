def retrieve_second_largest_integer(x): # X, a variable for list. 
    max_n = max(x)
    min_n = min(x)
    sort_n  = max_n - min_n + 1 # Determines the second largest integer.
    holes = [0] * sort_n
    while True:
        for i in x:
            i = [0] 
            if type(i) is int: # Validates whether X is an integer.
                print("Real Integers Only.")
                i += 1
            else:
                print(sort_n)
        break

x = [5, 3, 2, 6, 7]
print(retrieve_second_largest_integer(x))
