T=int(input())

for tc in range (1, T+1):
    N=list(map(int, input().split()))
    my_sum=0
    len_range=0

    for i in N:
        my_sum+= i
        len_range+=1
       
        
        

    result = round(my_sum/len_range)
    print (f'#{tc} {result}')
           
        
        

