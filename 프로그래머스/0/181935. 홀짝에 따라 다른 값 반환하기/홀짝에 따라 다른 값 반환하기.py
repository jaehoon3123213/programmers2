def solution(n):
    total1 = 0
    total2 = 0
    if n%2==0:
        for i in range(1,n+1,1):
            if i%2==0: 
                total1+=i**2
        return total1
    if n%2!=0:
        for i in range(1,n+1,1):
            if i%2!=0: 
                total2+=i
                print(i)
        return total2