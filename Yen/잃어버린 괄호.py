# '-'를 만날떄 가장 큰수를 빼면 가장 작은 수 

# '-'를 기준으로 분리 
arr = input().split('-')


#첫 숫자 계산 ( '-'를 만나기 전의 앞의 수 )
s=0
for i in arr[0].split('+') :
  s += int(i)


# '-' 이후의 값들 모두 '-'
for i in arr[1:] :
  for j in i.split('+') :
    s -= int(j)
    
print(s)
