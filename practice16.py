while(1):
   command=input("enter input:")
   if(command=="quit"):
       print("Bye!!")
       exit()
   number=int(command)
   for i in range(1,number+1):
        if(i%2==0):
          print(i)
