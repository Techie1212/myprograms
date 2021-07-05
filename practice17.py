while(1):
  command=input("enter input:")
  if(command=="quit"):
       print("Bye!!")
       exit()
  list1=[]
  number=int(command)
  for i in range(1,number+1):
       list1.append(i)
  for i in list1:
     count=0  
     for j in range(1,i+1):
        if(i%j==0):
           count=count+1
     if(count==2):
        print(i)
  print(list1)

      
