## write a python program to print whether the given number is fibonacci or not.
def fibonacci(Number):
    number1=int(Number**0.5)
    return number1*number1==Number
    
while(1):
   str=input("enter input:")  
   if(str=="quit"):
      print("Bye!!")
      break      
   number=int(str) 
   result1=5*(number*number)+4
   result2=5*(number*number)-4
   if(fibonacci(result1) or fibonacci(result2)):
         print(f"'{number}' is fibonacci number")
   else:
         print(f"'{number}'is not fibonacci number")
        
       
##
num=121
if(121):
   print("yes")
else:
   print("no")
