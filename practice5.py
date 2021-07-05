number=int(input("enter value of n:"))
sum=0
Number=number
count=0
while(number!=0):
  remainder=number%10
  number=int(number/10)
  sum=sum+remainder*remainder*remainder
  count=count+1
  print(f'remainder={remainder}')  
  print(f'number={number}')
  print(f'sum={sum}')
  
  print('______') 
  print(f'loop count={count}')

if(sum==Number):
  print("it is an armstrong")
else:
  print("not")
