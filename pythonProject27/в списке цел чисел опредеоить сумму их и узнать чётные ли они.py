def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(odd_or_even([0,1,4]))
