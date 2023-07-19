def Count_Sort_algorithm(array):
    result=[0 for _ in  range(10)]
    ans=[]
    n=len(array)
    for i in range(n):
        result[array[i]]+=1
    for i in range(len(result)):
         while result[i]>0:
             ans.append(i)
             result[i]-=1
    return ans

array=list(map(int,input().split()))
print(*Count_Sort_algorithm(array))