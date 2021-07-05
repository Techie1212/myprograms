## print whether the given string is palindrome or not.
 
while(1):
   string=input("enter input:")
   string1=string[::-1] 
   if(string==string1):
      print(f" '{string}' is a palidrome")   
   elif(string=="quit"):
      print("Bye!!!") 
      break
   else:
      print(f" '{string}' is not a palindrome")



