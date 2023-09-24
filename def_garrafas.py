T = int(input())

for i in range(T):
          
    n , k  = input().split(' ')#O que isso?
  
    a = int(n)
    b = int(k)
    
    if b > a:
      print(a)
    else:
      print((a // b)+ (a % b))