def solution(A , K):
    lenArray = len(A) # return the array if empty
    if lenArray == 0:
        return A
    
    K = K % lenArray #To avoid redundant rotation

    rotated = [0] * lenArray # declare rotated array
    for i in range(lenArray):
        print(i)
        index = (i + K) % lenArray # 
        rotated[index] = A[i] #place the values in the right place
    return rotated 

N = [3, 8, 9, 7, 6]
K = 3
solution(N, K)