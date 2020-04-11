def digital_root(n):
    
    res = list(map(int, str(n)))
    temp = 0
    
    for x in range(len(res)):
        if((x+1) == len(res)):
            break
        if(x == 0):
            temp = res[x] + res[x+1]
        else:
            temp = temp + res[x+1]
    
    if (len(str(temp)) != 1):
        return digital_root(temp)
    else:
        return temp
