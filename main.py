import math
print("addition:1| subtraction:2| multiplication:3| division:4| exponent:5|")
print("_______________________________________________________")
c = (input("what calculation do you want to use? "))
P = int(input("how many numbers in the equation? "))
if P==2:
  N1 = int(input("what is the first number? "))
  N2 = int(input("what is the second number? "))
  if c=="addition":
    a = int(N1 + N2)
    print("the answer is:")
    print("________________")
    print(a)
  elif c=="subtraction":
    a = int(N1-N2)
    print("the answer is:")
    print("________________")
    print(a)
  elif c=="multiplication":
    a = int(N1*N2)
    print("the answer is:")
    print("________________") 
    print(a)
  elif c=="division":
    a = int(N1/N2)
    print("the answer is:")
    print("________________")
    print(a)    
  elif c=="exponent":
    a = int(N1**N2)
    print("the answer is:")
    print("________________")
    print(a)
  else:
    print("learn to spell! ")

elif P==3:
   N1 = int(input("what is the first number? "))
   N2 = int(input("what is the second number? "))
   N3 = int(input("what is the third number? "))
   if c == "addition":
    a = int(N1 + N2 + N3)
    print("the answer is:")
    print("________________")
    print(a)
   elif c=="subtraction": 
    a = int(N1-N2-N3)
    print("the answer is:")
    print("________________")
    print(a)
   elif c=="multiplication":
      a = int(N1*N2*N3)
      print("the answer is:")
      print("________________") 
      print(a)
   elif c=="division":
      a = int(N1/N2/N3)
      print("the answer is:")
      print("________________")
      print(a)
   elif c=="exponent":
      a = int(N1**N2**N3)
      print("the answer is:")
      print("________________")
      print(a)
   else:
    print("learn to spell! ")
  

