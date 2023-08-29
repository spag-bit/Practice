def solution(N):
    
    binary = format(N, 'b') #Convert integer to string 
    max_gap = 0
    current_gap = 0

    for i in binary:
        if i == '1':
            max_gap = max(max_gap, current_gap) #return the max gap between 1 and zeroes
            current_gap = 0 # reset the current gap
        else:
            current_gap += 1 # count the zero(es)
    print(max_gap)
    return max_gap # return the max gap between 1 and 0

solution(66561)