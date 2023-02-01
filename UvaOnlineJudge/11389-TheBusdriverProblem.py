def make_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])




if __name__ == '__main__':
    inp = input().split()
    drivers = int(inp[0])
    max_route = int(inp[1])
    payment = int(inp[2])
    while drivers != 0:
        morningr = input().split()
        nightr = input().split()
        make_int(morningr)
        make_int(nightr)
        nightr.sort(reverse=True)
        morningr.sort()
        overtime = 0
        for i in range(0, drivers):
            t = morningr[i] + nightr[i]
            if t > max_route:
                overtime += (t - max_route)
        
        print(overtime * payment)


        inp = input().split()
        drivers = int(inp[0])
        max_route = int(inp[1])
        payment = int(inp[2])
