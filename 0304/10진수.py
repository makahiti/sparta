decimal = 149

binary = 0 

arr=[]

while decimal != 0:
    #2로 나눈 몫이 2보다 작아질때까지
    arr.append(decimal%2)
    #다음에 나눌 숫자는 2로 나눈 몫
    decimal = decimal // 2
    
arr.reverse()
print(arr)

#비트연산자
def bit_print(dec):
    output=""
    #2진수로 만든 결과
    for i in range(7):
        if dec & (1 << i):
            output += "1"
        else:
            output += "0"
    return output

print(bit_print(149))
######################################################
bit="00000000"
N=len(bit)

for i in range(0,N,7):
    ith_bin = bit[i:i+7]
    
    decimal = 0
    
    for j in range(6,-1,-1):
        decimal += int(ith_bin[j]) * 2 ** (6 - j)
        
    print(decimal, ",")