# For the algorithms created

# Pigeonhole Principle - Sorting algorithms where there are elements which are identical.

def pigeonhole(x):
    max_n = max(x)
    min_n = min(x)
    sort_n  = max_n - min_n + 1
    holes = [0] * sort_n
    while True:
        for i in x:
            i = [0]
            if type(i) is int:
                print("Real Integers Only.")
                i += 1
            else:
                print(sort_n)
        break

x = [5, 3, 2, 6, 7]
print(pigeonhole(x))

# Challenge - sort and retrieve the second largest integers.
def sort_hole(x):
    max_n = max(x)
    min_n = min(x)
    sort_n = max_n - min_n + 1
    holes = [0] * sort_n
    while True:
        s = sorted(x)
        for n in s:
            print(n)
            
        for i in x:
            i = [0]
            if type(i) is int:
                print("Real Integers Only.")
                i += 1
            else:
                print("The second largest integer is " + str(sort_n))
        break

x = [5, 3, 2, 6, 7]
print(sort_hole(x))
