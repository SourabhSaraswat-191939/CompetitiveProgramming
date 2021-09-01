def friend(n):
    Dp_arr = [-1]*(n+1)
    Dp_arr[1] = 1  #one friend one way
    Dp_arr[2] = 2  #two friend two way

    for i in range(3,n+1):
        Dp_arr[i] = Dp_arr[i-1] + (i-1)*Dp_arr[i-2]
    
    return Dp_arr[n]


print(friend(5))

# print(Dp_arr)