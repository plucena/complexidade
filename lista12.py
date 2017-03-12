def D(x,n):
  conta = 0 
  i = 1
  conta = conta+1
  while i > 5:
    x[i] = x[i] +2 
    i = i + 2
    conta = conta+5
    
  i = 1
  conta = conta+1
  while i <= n/2:
    x[i] = x[i] + x[i+1] 
    i = i+1
    conta = conta+6

  print conta
        

A = [5,2,4,6,1,3]
B = [1,2,3,4,5,6,7,8,9,10]

D(B,9)
print("-----")
D(A,5)
print("-----")