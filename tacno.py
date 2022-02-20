def tacno(arr,x=1):
    sum=x
    for i in arr:
        sum =  sum+i
        if sum< 1:
            x += abs(sum)+1
            return tacno(arr,x) 
    
    return x
print(tacno([24,2,3,4]))
print(tacno([-2, 3, 1, -5]))
print(tacno([-10,40,-1,4,-44,-5]))
print(tacno([100,-200,-100]))
print(tacno([500,-60,-500,100,-40,-10000,234,12])) 