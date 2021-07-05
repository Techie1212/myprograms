number=int(input("enter number:"))
sum=0
sum1=0
while(number!=0):
   remainder=number%10
   number=int(number/10)
   sum=sum*10+remainder
print(f'sum={sum}')
while(sum!=0):
   remainder=sum%10
   sum=int(sum/10)
   sum1=sum1*10+remainder
   print(f'remainder={remainder}')
print(f'sum1={sum1}')


   
   
