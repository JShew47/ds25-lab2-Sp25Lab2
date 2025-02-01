
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    if not lst:
        return True
    increasing = decreasing = True
    for i in range(1, len(lst)):
        if lst[i]>lst[i-1]:
            decreasing = False
        elif lst[i]<lst[i-1]:
            increasing = False
    return increasing or decreasing
test_cases = [
    [1, 1, 3, 100],
    [11, 1, -9, -10],
    [2, 3, 2, 3],
    []
]
for test in test_cases:
    print(f"List: {test} -> Monotonic: {monotonic(test)}")