def chocolatedistribution(arr):
    n = len(arr)
    stack = [(0, 0)]                  
    while stack:
        l, total = stack.pop()
        if l == n:
            print(total, end=" ")
            continue
        stack.append((l + 1, total + arr[l]))   
        stack.append((l + 1, total))             

arr = [5, 4, 3]
chocolatedistribution(arr)