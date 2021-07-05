## print even numbers in given range.

number=int(input("enter value of number:"))
count=0
for i in range (1,number+1): 
  if(i%2==0):
     count=count+1
     print(f'i={i}')
print(f'count={count}')

## print odd numbers in given range.

number=int(input("enter value of number:"))
count=0
for i in range(1,number+1):
    if(i%2!=0):
      count=count+1
      print(f'i={i}')
print(f'count={count}')

## print sum of first n numbers.

number=int(input("enter value of number:"))
sum=0
for i in range(1,number+1):
    sum=sum+i
print(sum)

## write a program whether he eligible for vote or not.
 
age=int(input("enter age:"))
if(age>=18):
   print("he/she is eligible for vote")
else:
   print("not eligible for vote")
