## print reverse of a given number 

number=int(input("enter value of n:"))
sum=0
while(number!=0):
    remainder=number%10
    number=int(number/10)
    sum=sum*10+remainder
print(f'sum={sum}')

## check palindrome number

number=int(input("enter value of n:"))
sum=0
Number=number
while(number!=0):
   remainder=number%10
   number=int(number/10)
   sum=sum*10+remainder
if(sum==Number):
   print("it is palindrome")
else:
   print("is not")
