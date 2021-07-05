while(1):
   command=input("enter string:")  

   if(command=="quit"):
       print("Bye!!")
       exit()
   number=int(command)
   count=0
   for i in range(1,number+1):
       if(number%i==0):
          count=count+1
   if(count==2):
       print(f"{number} is prime")
   else:
       print(f"{number} is not prime")
