def add(a,b):
     return a+b
while(1):
   number=input("enter input:")
   number1=input("enter input:")
   if(number=="quit" and number1=="quit"):
      print("Bye!!")  
      break
   number=int(number)
   number1=int(number1)
   print(add(number,number1))
 
