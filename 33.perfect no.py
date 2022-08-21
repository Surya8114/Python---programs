# Python program to check perfect number

# take inputs
N = int(input("Enter a number: "))

# check perfect number
sum = 0 
for i in range(1,N): 
   if(N%i == 0):
      sum = sum+i

# display result
if(sum == N): 
   print(N, "is a perfect number")
else: 
   print(N, "is not a perfect number")
