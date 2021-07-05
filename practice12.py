while(1):
   str=input("enter input:")  
   if(str=="quit"):
      print("Bye!!")
      break 
   number=int(str) 
   result1=5*(number*number)+4
   result2=5*(number*number)-4
   Number1=result1 
   Number2=result2  
   number1=int(Number1**0.5)
   number2=int(Number2**0.5)
   if(number1*number1==Number1 or number2*number2==Number2):
         print(f"'{number}' is fibonacci number")
   else:
         print(f"'{number}'is not fibonacci number")
